from django.db import models

# Create your models here.


class Student(models.Model):


	nickname = models.CharField(max_length=200)
	university = models.CharField(max_length=200)
	ig_handle = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	phone_privacy = models.BooleanField(default=True)

	def __str__(self):
		return str(self.nickname) + ' ' + str(self.university)