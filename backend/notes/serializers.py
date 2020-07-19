from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Note

class NoteSerializer(serializers.ModelSerializer):

	user = serializers.PrimaryKeyRelatedField(source='user.username',queryset=get_user_model().objects.all())

	class Meta:
		model = Note
		fields = ['title','body','date_created','user']



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = get_user_model()
		fields = '__all__'
