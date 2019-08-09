from django.db import models
from django.contrib.auth.models import User

RENT_TERM_CHOICES = (
   ('장기(2주이상)', '장기(2주이상)'),
   ('단기(2주미만)', '단기(2주미만)')
)
ROOM_TYPE_CHOICES = (
    ('원룸', '원룸'),
    ('투룸', '투룸'),
    ('복층형 원룸', '복층형 원룸'),
    ('쓰리룸+', '쓰리룸+')
)
HOST_STUFF_CHOICES=(
    ('있음', '있음'),
    ('없음', '없음')
)
PARKING_CHOICES=(
    ('있음', '있음'),
    ('없음', '없음')
)
PET_CHOICES=(
    ('가능', '가능'),
    ('불가능', '불가능')
)
ELEVATOR_CHOICES=(
    ('있음', '있음'),
    ('없음', '없음')
)
OPTION_CHOICES=(
    ('에어컨', '에어컨'),
    ('냉장고', '냉장고'),
    ('세탁기', '세탁기'),
    ('책상', '책상'),
    ('침대', '침대'),
    ('침대', '싱크대')
)
# Create your models here.
class Room(models.Model):
    intro = models.CharField(max_length=200)                                                                #방 한줄 소개
    pub_date = models.DateField(null=True, auto_now=False, auto_now_add=False)                                         #등록 일자
    confirmation = models.FileField(null=True)                                                              #확인서 파일 첨부
    rent_term = models.CharField(choices=RENT_TERM_CHOICES, max_length=128)                                 #거래 유형(장/단기), #라디오버튼
    start_date = models.DateField(null=True)                                  #임대 시작 날짜
    end_date = models.DateField(null=True)                                    #임대 종료 날짜
    price = models.CharField(max_length=200)                                                                #임대 가격
    floor = models.CharField(max_length=200)                                                                #층
    room_type = models.CharField(choices=ROOM_TYPE_CHOICES, max_length=128)                                 #방 구조, #라디오버튼
    area = models.CharField(max_length=200)                                                                 #면적(평/m2)
    host_stuff = models.CharField(choices=HOST_STUFF_CHOICES, max_length=128)                               #집주인 물건 유무, #라디오버튼
    parking = models.CharField(choices=PARKING_CHOICES, max_length=128)                                     #주차장 유무, #라디오버튼
    pet = models.CharField(choices=PET_CHOICES, max_length=128)                                             #애완동물 동반 가능 여부, #라디오버튼
    elevator = models.CharField(choices=ELEVATOR_CHOICES, max_length=128)                                   #엘베유무, #라디오버튼
    option = models.CharField(choices=OPTION_CHOICES, max_length=128)                                       #옵션(에어컨, 냉장고, 세탁기, 책상, 침대, 싱크대),#체크박스
    detail = models.TextField()                                                                             #상세설명
    main_img = models.ImageField(null=True, height_field=None, width_field=None)                            #대표사진(1장, 필수)
    other_img = models.ImageField(null=True, height_field=None, width_field=None)                           #기타사진(주방/화장실, 필수)
    room_img = models.ImageField(null=True, height_field=None, width_field=None)                            #방별사진(방당 1장, 선택)
    address1 = models.CharField(null=True, max_length=128)
    address2 = models.CharField(null=True, max_length=128)
    address3 = models.CharField(null=True, max_length=128)
    address4 = models.CharField(null=True, max_length=128)

    #media 만들기

    #스크랩
    users = models.ManyToManyField(User, through='Scrap')
    users = models.ManyToManyField(User, through='Like')

    def __str__(self):
        return self.intro





class Scrap(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)