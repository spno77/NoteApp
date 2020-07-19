from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Note
from .serializers import NoteSerializer

from rest_framework import generics

class NoteList(generics.ListCreateAPIView):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer


