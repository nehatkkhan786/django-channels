from unicodedata import name
from django.shortcuts import render
from .models import Rooms


def index_view(request):
    rooms = Rooms.objects.all()
    return render(request, 'index.html', {'rooms':rooms})


def room_view(request, room_name):
    chat_room, created = Rooms.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {'room':chat_room})
