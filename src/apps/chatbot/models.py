from django.db import models
from django.contrib.auth.models import AbstractUser

from config.validators import phone_validate

from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid


class CustomSender(AbstractUser):
    phone_number = models.CharField( max_length = 15, validators =[phone_validate], blank = True, null = True )
    is_sample_sender = models.BooleanField(default=False)

    # Add unique related_names to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customsender_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customsender_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username


class Conversation(models.Model):
    """Model to represent a conversation or chat session."""
    sender = models.ForeignKey(CustomSender, on_delete=models.CASCADE, related_name='conversations')
    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation with {self.sender.username} started at {self.started_at}"


class Message(models.Model):
    """Model to store messages within a conversation."""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name = 'messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.content} in conversation {self.conversation}"

class RAGResponse(models.Model):
    """Model to store RAG model responses."""
    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='rag_response')
    response_text = models.TextField()

    def __str__(self):
        return f"RAG Response for message {self.message.id}"