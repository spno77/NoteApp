#notes/urls.py

from django.urls import path,include
from . import views
from .views import NoteList,NoteDetail

urlpatterns = [

	path('notes/',views.NoteList.as_view()),
	path('notes/<int:pk>/',views.NoteDetail.as_view()),

]
