from django.http import HttpResponse
from django.shortcuts import render

from .models import Chat
import random
import string
from django.utils import timezone

def index(request):
    return render(request, 'chat/index.html')
def get_chat(request):
    unique_name =''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

    chat = Chat(unique_name=unique_name,pub_date=timezone.now())
    chat.save()
    return render(request, 'chat/get_chat.html',{'unique_name':unique_name} )

def current_ids(request):

    return HttpResponse(Chat.objects.all())

def

