from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):

	title  		 =	models.CharField(max_length=20)
	body 		 =	models.CharField(max_length=200)
	date_created =  models.DateField()

	user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)


