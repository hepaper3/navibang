from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta: 
        model = Room
        fields = ['intro','pub_date','confirmation','rent_term','start_date','end_date','price','floor','room_type','area','host_stuff','parking','pet','elevator','option','detail','main_img','other_img','room_img']

        widgets = {
            'intro': forms.TextInput( 
                attrs={ 
                        'class': 'form-control', 
                        'placeholder': '방 소개글을 작성해 주세요.', 
                      } 
            ), 
            'pub_date': forms.DateInput( 
                attrs={ 
                        'class': 'form-control', 
                        'type':  'date', 
                      } 
            ),
             'confirmation': forms.FileInput( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
             'rent_term': forms.RadioSelect( 
                attrs={ 
                        'class': 'form-control',
                      } 
            ),
             'start_date': forms.DateInput( 
                attrs={ 
                        'class': 'form-control', 
                        'type':  'date', 
                      } 
            ),
             'end_date': forms.DateInput( 
                attrs={ 
                        'class': 'form-control', 
                        'type':  'date', 
                      } 
            ),
             'price': forms.TextInput( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
             'floor': forms.TextInput( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
             'room_type': forms.RadioSelect( 
                attrs={ 
                        'class': 'form-control',  
                      } 
            ),
             'area': forms.TextInput( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
             'host_stuff': forms.RadioSelect( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
             'parking': forms.RadioSelect( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
              'pet': forms.RadioSelect( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
              'elevator': forms.RadioSelect( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
              'option': forms.CheckboxInput( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
               'detail': forms.Textarea( 
                attrs={ 
                        'class': 'form-control', 
                        'rows': '5',
                      } 
            ),
               'main_img': forms.FileInput( 
                attrs={    
                        'class': 'form-control', 
                      } 
            ),
               'other_img': forms.FileInput( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
               'room_img': forms.FileInput( 
                attrs={ 
                        'class': 'form-control', 
                      } 
            ),
        }

        labels = { 
                    'intro': '소개글',
                    'pub_date': '등록일', 
                    'confirmation': '확인서',
                    'rent_term': '임대유형',
                    'start_date': '임대 시작 날짜', 
                    'end_date': '임대 종료 날짜',
                    'price': '가격',
                    'floor': '층', 
                    'room_type': '방 유형',
                    'area': '면적(평)',
                    'host_stuff': '집주인 짐', 
                    'parking': '주차장',
                    'pet': '애완동물 동반',
                    'elevator': '엘리베이터', 
                    'option': '옵션',
                    'detail': '상세소개',
                    'main_img': '대표 사진', 
                    'other_img': '화장실, 주방 사진',
                    'room_img': '방별 사진',
                 }