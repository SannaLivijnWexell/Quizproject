from django.db import models

# Create your models here.
class Quiz(models.Model):
	quiz_number = models.PositiveIntegerField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	def __str__(self):
		return self.name

class Question(models.Model):
	question = models.TextField()
	answer1 = models.CharField(max_length=100)
	answer2 = models.CharField(max_length=100)
	answer3 = models.CharField(max_length=100)
	correct = models.PositiveIntegerField()
	quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
