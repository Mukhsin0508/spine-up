import logging
from typing import Type, Tuple

from django.core.files.storage import default_storage
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import FileField, ImageField, Model

logger = logging.getLogger(__name__)

def delete_file_after_object_deletion(
    instance: Model,
    field_types: Tuple[Type[FileField], ...] = (FileField, ImageField)) -> None:
    """
    Delete file from storage after the object is deleted.
    """
    for field in instance._meta.get_fields():
        if isinstance(field, field_types):
            file_field = getattr(instance, field.name, None)
            # Skip if file field is None or doesn't have a name
            if not file_field or not file_field.name:
                continue

            try:
                # Check if the file exists before trying to delete it
                if default_storage.exists(file_field.name):
                    # Delete file from storage
                    default_storage.delete(file_field.name)
                    logger.info(f"File '{file_field.name}' deleted successfully.")
                else:
                    logger.warning(f"File '{file_field.name}' does not exist in storage.")
            except Exception as e:
                logger.error(f"Error deleting file '{file_field.name}': {e}")


def delete_file_after_object_update(
    instance: Model,
    field_types: Tuple[Type[FileField], ...] = (FileField, ImageField),
    old_instance: Model = None) -> None:
    """
    Delete old file from storage when a file field is updated.

    Args:
        instance: The new instance being saved
        field_types: Types of fields to check for files
        old_instance: The existing instance from the database (optional)
                     If not provided, it will be fetched from the database
    """
    # If old_instance is not provided, fetch it from the database
    if old_instance is None:
        try:
            old_instance = instance.__class__.objects.get(pk=instance.pk)
        except ObjectDoesNotExist:
            logger.error(f"Object with pk {instance.pk} does not exist.")
            return

    for field in instance._meta.get_fields():
        if isinstance(field, field_types):
            old_file_field = getattr(old_instance, field.name, None)
            # Check if the file field has changed
            new_file_field = getattr(instance, field.name, None)

            # Skip if old file field is None or doesn't have a name
            if not old_file_field or not old_file_field.name:
                continue

            # Skip if new file field is None
            if new_file_field is None:
                continue

            # If the file field has changed (different name)
            if old_file_field.name != new_file_field.name:
                try:
                    # Check if the file exists before trying to delete it
                    if default_storage.exists(old_file_field.name):
                        default_storage.delete(old_file_field.name)
                        logger.info(f"File '{old_file_field.name}' deleted successfully.")
                    else:
                        logger.warning(f"File '{old_file_field.name}' does not exist in storage.")
                except Exception as e:
                    logger.error(f"Error deleting the old file '{old_file_field.name}': {e}")
