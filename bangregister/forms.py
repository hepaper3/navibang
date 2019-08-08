from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    option = forms.CharField(widget=forms.RadioSelect(choices=((0,'냉장고'),(1,'선풍기'),(2,'에어컨'))))
    class Meta: 
        model = Room
        fields = ('intro','pub_date','confirmation','rent_term','start_date','end_date','price','floor','room_type','area','host_stuff','parking','pet','elevator','option','detail','main_img','other_img','room_img')

        def __init__(self, *args, **kwargs):
          super(RoomForm, self).__init__(*args, **kwargs)
          self.fields['file'].required = False

        