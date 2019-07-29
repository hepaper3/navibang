from django.shortcuts import render
from .models import Room

# Create your views here.
def home(request):
    #메인 페이지
    return render(request, 'home.html')

def list(request):
    #등록한 방들이 보일 페이지
    return render(request, 'list.html')

def show(request):
    #방 세부 페이지
    rooms = Room.objects
    return render(request, 'show.html', {'rooms' : rooms})

def register(request):
    #방 등록 페이지
    return render(request, 'register.html')

def edit(request):
    # 수정 페이지
    return render(request, 'edit.html')

#def delete(request):
    #삭제기능
#    return render(request, 'delete.html')
