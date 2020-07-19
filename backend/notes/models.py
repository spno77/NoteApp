from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):

	title  		 =	models.CharField(max_length=20)
	body 		 =	models.CharField(max_length=200)
	date_created =  models.DateField(auto_now_add=True)

	#user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

	def __str__(self):
		return self.title
