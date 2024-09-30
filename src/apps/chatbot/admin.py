from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Conversation, Message, RAGResponse, CustomSender

class MessageInline(admin.StackedInline):  # Use StackedInline for a chat-like appearance
    model = Message
    readonly_fields = ('display_message',)
    extra = 0
    can_delete = False

    def display_message(self, obj):
        if obj.sender.is_sample_sender:
            # Styling for the sender (align left)
            return format_html('<div style="text-align: left;"><strong>{}</strong>: {}</div>', obj.sender.username, obj.content)
        else:
            # Styling for the recipient (align right)
            return format_html('<div style="text-align: right;"><strong>{}</strong>: {}</div>', obj.sender.username, obj.content)

    display_message.short_description = "Conversation"  # This will be the column header

    class Media:
        css = {
            'all': ('custom_admin.css',)  # You can include custom CSS for styling
        }

class RAGResponseInline(admin.StackedInline):
    model = RAGResponse
    readonly_fields = ('response_text',)
    extra = 0
    can_delete = False

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'started_at', 'view_conversation_link')
    list_filter = ('started_at', 'sender')
    search_fields = ('sender__username', 'sender__email')
    inlines = [MessageInline]

    def view_conversation_link(self, obj):
        # Create a link to the conversation change view (where messages are displayed)
        url = reverse('admin:chatbot_conversation_change', args=[obj.id])  # Replace 'appname' with your app name
        return format_html('<a href="{}">View Conversation</a>', url)

    view_conversation_link.short_description = "Conversation Details"

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'content', 'timestamp')
    list_filter = ('timestamp', 'sender')
    search_fields = ('content', 'sender__username', 'sender__email')
    readonly_fields = ('conversation', 'sender', 'content', 'timestamp')
    inlines = [RAGResponseInline]

@admin.register(CustomSender)
class CustomSenderAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_sample_sender')
    list_filter = ('is_sample_sender',)
    search_fields = ('username', 'email', 'phone_number')
