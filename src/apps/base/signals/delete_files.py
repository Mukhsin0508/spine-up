from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save
from django.db.models import Model

from apps.base.services import (
    delete_file_after_object_deletion,
    delete_file_after_object_update,
)

@receiver(post_delete)
def handle_file_post_delete(sender: Model, instance: Model, **kwargs) -> None:
    """
    Signal receiver to delete files after the object is deleted.
    """
    if isinstance(instance, Model):
        try:
            delete_file_after_object_deletion(instance)
        except Exception as e:
            # Log the error but don't prevent the delete operation
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error in handle_file_post_delete: {e}")

@receiver(pre_save)
def handle_file_pre_save(sender: Model, instance: Model, **kwargs) -> None:
    """
    Signal receiver to delete files before the object is updated.
    """
    if isinstance(instance, Model) and instance.pk:
        try:
            # Get the existing instance from the database
            existing_instance = sender.objects.get(pk=instance.pk)
            # Pass the existing instance to the service function
            delete_file_after_object_update(instance, old_instance=existing_instance)
        except Exception as e:
            # Log the error but don't prevent the save operation
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error in handle_file_pre_save: {e}")
