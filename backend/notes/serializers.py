from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Note

class NoteSerializer(serializers.ModelSerializer):

	user = serializers.PrimaryKeyRelatedField(source='user.username',queryset=get_user_model().objects.all())

	class Meta:
		model = Note
		fields = ['id','title','body','date_created','user']


	def update(self,instance,validated_data):
		instance.id        = validated_data.get('id', instance.id)
		instance.title     = validated_data.get('title', instance.title)
		instance.body      = validated_data.get('body', instance.body)
		instance.date_created      = validated_data.get('date_created', instance.date_created )
		instance.user  = validated_data.get('user.username', instance.user)
		instance.save()
		return instance
		


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = get_user_model()
		fields = '__all__'
