from django.urls import path
from . import views

app_name='ttg'

urlpatterns = [
    path ('subject/', views.subject, name="subject"),
    path ('room/', views.room, name="room"),
    path ('batch/', views.batch, name="batch"),
    path ('time/', views.time, name="time"),
    path ('displaySubject/', views.displaySubject, name="displaySubject"),
    path ('displayRoom/', views.displayRoom, name="displayRoom"),
    path ('displayTime/', views.displayTime, name="displayTime"),
    path ('displayBatch/', views.displayBatch, name="displayBatch"),
    path ('deleteSubject/<str:pk>/', views.deleteSubject, name="deleteSubject"),
    path ('deleteRoom/<str:pk>/', views.deleteRoom, name="deleteRoom"),
    path ('deleteTime/<str:pk>/', views.deleteTime, name="deleteTime"),
    path ('deleteBatch/<str:pk>/', views.deleteBatch, name="deleteBatch"),
    path ('displayTimetable/', views.displayTimetable, name="displayTimetable")
]