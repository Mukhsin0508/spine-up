import uuid

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Conversation, Message, RAGResponse, CustomSender
from .serializers import ConversationSerializer, MessageSerializer
import requests
import json


def get_rag_response(query, conversation_history):
    url = "https://api.mukhsin.space/rag-query"
    headers = {"Content-Type":"application/json"}
    data = {
        "query":query,
        "conversation_history":conversation_history
        }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


class ConversationListCreateView(generics.ListCreateAPIView):

    permission_classes = ()
    authentication_classes = ()

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def perform_create(self, serializer):
        # Create a sample sender if not provided
        sender, _ = CustomSender.objects.get_or_create(
            username=f"sample_user_{uuid.uuid4().hex[:8]}",
            defaults={'is_sample_sender':True}
            )
        serializer.save(sender=sender)


class MessageListCreateView(generics.ListCreateAPIView):

    permission_classes = ()
    authentication_classes = ()

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()

        # Get the last 15 messages from this conversation
        conversation = message.conversation
        recent_messages = Message.objects.filter(conversation=conversation).order_by('-timestamp')[:15]

        conversation_history = []
        for msg in reversed(recent_messages):
            conversation_history.append({"role": "user", "content": msg.content})
            if hasattr(msg, 'rag_response'):
                conversation_history.append({"role": "assistant", "content": msg.rag_response.response_txt})

        # Get RAG response with conversation history
        rag_response = get_rag_response(message.content, conversation_history)
        RAGResponse.objects.create(message=message, response_text=rag_response['response'])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Get the RAG response
        rag_response = RAGResponse.objects.get(message=serializer.instance)

        return Response(
            {
                'message':serializer.data,
                'response':rag_response.response_text
                }, status=status.HTTP_201_CREATED, headers=headers
            )