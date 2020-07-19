from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Note

class NoteSerializer(serializers.ModelSerializer):

	user = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Note
		fields = ['title','body','date_created','user']
