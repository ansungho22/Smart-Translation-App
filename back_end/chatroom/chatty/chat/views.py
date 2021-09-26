from django.shortcuts import render
from .models import Message

# Create your views here.
def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    username = request.GET.get("username", "Anonymous")
    messages = Message.objects.filter(room=room_name)[0:25]
    messages_list = []
    for context in messages:
        messages_list.append(context)

    return render(
        request,
        "chat/room.html",
        {"room_name": room_name, "username": username, "messages": messages_list},
    )
