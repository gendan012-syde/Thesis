from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('upload-media/', views.upload_media, name='upload_media'),
    path('delete-file/', views.delete_file, name='delete_file')

]