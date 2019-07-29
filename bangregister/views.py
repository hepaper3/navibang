from django.shortcuts import render, get_object_or_404, redirect
from .models import Room
from .forms import RoomForm

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
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            roompost = form.save(commit=False)
            roompost.save()
            return redirect('list')
    else:
        form = RoomForm()
        return render(request, 'register.html', {'form':form})

def edit(request):
    # 수정 페이지
    return render(request, 'edit.html')

#def delete(request):
    #삭제기능
#    return render(request, 'delete.html')
