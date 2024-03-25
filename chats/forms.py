from django import forms
from chats.models import Chatroom


class ChatRoomForm(forms.ModelForm) : 
    class Meta : 
        model = Chatroom
        fields = "__all__"
        exclude = ["host" ,"participants"]
