from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Note
from .serializers import NoteSerializer
from .permissions import IsCreator

from rest_framework import generics

class NoteList(generics.ListCreateAPIView):
	serializer_class = NoteSerializer
	#queryset = Note.objects.all()


	def get_queryset(self):
		user = self.request.user
		return Note.objects.filter(user=user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsCreator,]
	queryset = Note.objects.all()
	serializer_class = NoteSerializer


