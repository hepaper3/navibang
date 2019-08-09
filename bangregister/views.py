from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Room, Scrap, Like
from .forms import RoomForm, CommentForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    #메인 페이지
    return render(request, 'home.html')

def list(request):
    roomposts = Room.objects
    return render(request, 'list.html', {'roomposts':roomposts})

def result(request):
    post_object = Room.objects #Post 모델안의 모든 객체를 post_object 변수 안에 담는다.
    query = request.GET.get('query','') #query라는 name값을 '' 뒤에 담아오겠다.
    if query: #쿼리 값이 존재한다면
        post_object = post_object.filter(intro__endswith=query)
    #쿼리값과 일치하는, 즉 쿼리값으로 끝나는 타이틀을 가진 객체를 필터링 하여 post_object에 담는다.
    return render(request, 'result.html', {'result':post_object})

def show(request, roompost_id):
    #방 세부 페이지
    roompost = get_object_or_404(Room, pk=roompost_id)

    if User.is_anonymous:
        scrap=None
        like=None
    else:
        scrap = Scrap.objects.filter(user=request.user, room_id=roompost)
        like = Like.objects.filter(user=request.user, room_id=roompost)

    if roompost.creator == request.user :
        user_authority = True
    else : 
        user_authority = False

    return render(request, 'show.html', {'roompost' : roompost, 'scrap' : scrap, 'like' : like, 'user_authority' : user_authority })

@login_required
def roomupdate(request, roompost_id):
    roompost = get_object_or_404(Room, pk = roompost_id) 
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=roompost) 
        if form.is_valid():
            roompost = form.save(commit=False) 
            roompost.creator = request.user
            roompost.save() 
            return redirect('show', roompost_id=roompost.pk)
    else: 
        if roompost.creator == User.objects.get(username=request.user.get_username()) :
            form = RoomForm(instance=roompost)
            return render(request, 'edit.html', {'form': form})
        else :
            return render(request, 'home.html')

@login_required
def register(request):
    #방 등록 페이지 
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            roompost = form.save(commit=False)
            roompost.creator = request.user
            roompost.save()
            return redirect('list')
    else:
        form = RoomForm() 
    return render(request, 'register.html', {'form':form})

@login_required
def edit(request):
    # 수정 페이지
    return render(request, 'edit.html')

@login_required
def delete(request, roompost_id):
    #삭제기능
    roompost = get_object_or_404(Room, pk=roompost_id)

    if roompost.creator == User.objects.get(username=request.user.get_username()) :
        roompost.delete()
        return redirect('list')
    else :
        return render(request, 'home.html')

@login_required
def scrap(request, roompost_id) :
    roompost = get_object_or_404(Room, pk=roompost_id)
    scrapped = Scrap.objects.filter(user=request.user, room=roompost)
    if not scrapped:
        Scrap.objects.create(user=request.user, room=roompost)
    else:
        scrapped.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def like(request, roompost_id) :
    roompost = get_object_or_404(Room, pk=roompost_id)
    liked = Like.objects.filter(user=request.user, room=roompost)
    if not liked:
        Like.objects.create(user=request.user, room=roompost)
    else:
        liked.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def commentcreate(request, roompost_id): 
    roompost = get_object_or_404(Room, pk=roompost_id) 
    if request.method=='POST': 
        form = CommentForm(request.POST) 
        if form.is_valid(): 
            comment = form.save(commit=False)
            comment.room = roompost 
            comment.save() 
            return redirect('show', roompost_id=roompost.pk) 
        else: 
            redirect('list') 
    else: 
        form = CommentForm() 
        return render(request, 'show.html', {'form': form, 'roompost': roompost})


