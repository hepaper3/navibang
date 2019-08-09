from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('intro','pub_date','confirmation','rent_term','start_date','end_date','price','floor','room_type','area','host_stuff','parking','pet','elevator','option','detail','main_img','other_img','room_img', 'address1', 'address2', 'address3', 'address4')

        def __init__(self, *args, **kwargs):
          super(RoomForm, self).__init__(*args, **kwargs)
          self.fields['file'].required = False

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
             'rent_term': forms.Select(
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
             'room_type': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'area': forms.TextInput(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'host_stuff': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
             'parking': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
              'pet': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
              'elevator': forms.Select(
                attrs={
                        'class': 'form-control',
                      }
            ),
              'option': forms.Select(
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
                'address1':forms.TextInput(
                attrs={
                    'type':'text' ,
                    'id' :'sample3_postcode' ,
                    'placeholder' : '우편번호',
                    }
            ),

            'address2':forms.TextInput(
                attrs={
                    'type':'text' ,
                    'id' :'sample3_address' ,
                    'placeholder' : '주소',
                }
        ),
            'address3':forms.TextInput(
                attrs={
                    'type':'text' ,
                    'id' :'sample3_detailAddress' ,
                    'placeholder' : '상세주소',
                }
        ),

            'address4':forms.TextInput(
                attrs={
                    'type':'text' ,
                    'id' :'sample3_extraAddress' ,
                    'placeholder' : '참고항목',
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
                    'address1' : '우편번호',
                    'address2' : '주소',
                    'address3' : '상세주소',
                    'address4' : '참고항목',
                 }
