from rest_framework import serializers
from django.utils import timezone
from chat.models import ChatMessage, Thread
from users.api.serializers import UserSerializer

class ChatMessageSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    class Meta:
        model = ChatMessage
        fields = ('id','maint_request', 'author', 'message', 'date_posted')