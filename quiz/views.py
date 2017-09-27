from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



quizzes = [
	{
		"quiz_number": 1,
		"name": "Klassiska böcker",
		"description": "Hur bra kan du dina klassiker?"
	},
	{
		"quiz_number": 2,
		"name": "Största fotbollslagen",
		"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
		"name": "Världens mest kända hackare",
		"description": "Kan du din hackerhistoria?"
	},
]




def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "start.html", context)


def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[quiz_number - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz.html", context)



def question(request, quiz_number, question_number):
	return render(request, "question.html")

	

def completed(request, quiz_number):
	return render(request, "result.html")