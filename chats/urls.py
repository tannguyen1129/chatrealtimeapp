from django.urls import path
from chats import views
from chats.views import CreateTodo, Directs, SendDirect, UserSearch, NewConversation, TodoDelete

app_name = "chats"


urlpatterns = [
    path("", views.chat, name="message"),
    path("room/<int:pk>", views.Room, name="chat-room"),
    path("join/room/<int:pk>" , views.JoinRoom , name = "join-room") ,
    path("create/room/", views.CreateRoom, name="create-room"),
    path("update/room/<int:pk>", views.UpdateRoom, name="update-room"),
    path('leave-room/<int:pk>/', views.leaveRoom, name='leave-room'),
    path('delete-message/<int:pk>.', views.deleteMessage, name='delete-message'),
    path('send-msg/<int:pk>/', views.SendMSG, name='send-message'),
    
    path("delete/todo", TodoDelete, name="delete-todo"),
    path("create/todo/", CreateTodo, name="create-todo"),

    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
    path('search/', UserSearch, name="search-users"),
    path('new/<username>', NewConversation, name="conversation"),

]
