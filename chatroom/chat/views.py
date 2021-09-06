from django.shortcuts import render
from .models import Message
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/Code/chatroom/chatty/smarth-322600-e26f149eb53f.json"
translate_client = translate.Client()

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


@csrf_exempt
def test(request):
    if request.method == "POST":
        text = request.body.decode("utf-8")
        textjson = json.loads(text)
        mess = textjson["num"]
        result = translate_client.translate(textjson, "EN")
        print(result)
        return JsonResponse(mess, status=200, safe=False)
