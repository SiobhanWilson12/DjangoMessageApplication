from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer
from django.shortcuts import render

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def message_list_view(request):
    messages = Message.objects.all()
    return render(request, 'messages_app/message_list.html', {'messages': messages})
  
@api_view(['DELETE'])
def clear_messages(request):
    if request.method == 'DELETE':
        count, _ = Message.objects.all().delete()
        return Response({"message": f"{count} messages deleted."}, status=status.HTTP_204_NO_CONTENT)  
