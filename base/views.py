from curses.ascii import HT
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.
"""
rooms = [
    {"id": 1,
    "name" :"Python"
    }, 
    {"id": 2,
    "name" :"JS"
    },
    {"id": 3,
    "name" :"R"
    },
    
]
"""

#print(rooms)
def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, 'base/home.html', context )

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    #processing

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    print('hello')
    context ={'form' :form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj' : room}
    return render(request, 'base/delete.html', context)