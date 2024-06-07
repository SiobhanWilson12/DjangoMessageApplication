from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'timestamp']

    def validate_content(self, value):
        if len(value) >= 100:
            raise serializers.ValidationError("Content is too long, must be less than 100 characters.")
        return value    
