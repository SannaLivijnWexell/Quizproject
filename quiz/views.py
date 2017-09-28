

# Create your views here.
from quiz.models import Quiz
from django.shortcuts import render
from django.shortcuts import redirect

# quizzes = [
# 	{
# 		"quiz_number": 1,
# 		"name": "Jorden runt på 15 rätter",
# 		"description": "Ramen, shakshuka och haggis – har du kolla?"
# 	},
# 	{
# 		"quiz_number": 2,
# 		"name": "Jorden runt på 15 rätter",
# 		"description": "Kan du dina lag?"
# 	},
# 	{
# 		"quiz_number": 3,
# 		"name": "Världens mest kända hackare",
# 		"description": "Kan du din hackerhistoria?"
# 	},
# ]




def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "start.html", context)


def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz.html", context)




def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[question_number - 1]
	context = {
    		"question_number": question_number,
    		"question": question.question,
	    	"answer1": question.answer1,
    		"answer2": question.answer2,
	    	"answer3": question.answer3,
	    	"quiz": quiz,
		"quiz_number": quiz_number,
	}
	return render(request, "question.html", context)





def completed(request, quiz_number):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "result.html", context)





def answer(request, quiz_number, question_number):
	answer = request.POST["answer"]
	saved_answers = request.session.get(str(quiz_number), {})
	saved_answers[question_number] = int(answer)
	request.session[quiz_number] = saved_answers
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	num_questions = quiz.questions.count()
	if num_questions <= question_number:
		return redirect("completed_page", quiz_number)
	else:
		return redirect("question_page", quiz_number, question_number + 1)













