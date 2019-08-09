from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Room, Scrap, Like
from .forms import RoomForm

# Create your views here.
def home(request):
    #메인 페이지
    return render(request, 'home.html')

def list(request):
    #등록한 방들이 보일 페이지
    roomposts = Room.objects
    return render(request, 'list.html', {'roomposts':roomposts})

def show(request, roompost_id):
    #방 세부 페이지
    roompost = get_object_or_404(Room, pk=roompost_id)
    scrap = Scrap.objects.filter(user=request.user, room_id=roompost)
    like = Like.objects.filter(user=request.user, room_id=roompost)
    return render(request, 'show.html', {'roompost' : roompost, 'scrap' : scrap, 'like' : like})

def roomupdate(request, roompost_id):
    roompost = get_object_or_404(Room, pk = roompost_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=roompost)
        if form.is_valid():
            roompost = form.save(commit=False)
            roompost.save()
            return redirect('show', roompost_id=roompost.pk)
    else:
        form = RoomForm(instance=roompost)
        return render(request, 'edit.html', {'form': form})

def register(request):
    #방 등록 페이지
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
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

def delete(request, roompost_id):
    #삭제기능
    roompost = get_object_or_404(Room, pk=roompost_id)
    roompost.delete()
    return redirect('list')


def scrap(request, roompost_id) :
    roompost = get_object_or_404(Room, pk=roompost_id)
    scrapped = Scrap.objects.filter(user=request.user, room=roompost)
    if not scrapped:
        Scrap.objects.create(user=request.user, room=roompost)
    else:
        scrapped.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def like(request, roompost_id) :
    roompost = get_object_or_404(Room, pk=roompost_id)
    liked = Like.objects.filter(user=request.user, room=roompost)
    if not liked:
        Like.objects.create(user=request.user, room=roompost)
    else:
        liked.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
