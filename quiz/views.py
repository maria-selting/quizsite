# coding: utf-8

from django.shortcuts import render

quizzes={
	"movies":{
		"name":u"Movies of the 80´s",
		"description": "Can you recall what song belongs to what movie?"
	},
	"musicians":{
		"name":u"Musicians",
		"description":u"How well do you know the great musicians of the 80's?"

	},
	"fashion":{
		"name":u"Fashion",
		"description":u"Do you remember the fashion of the 80´s?"

	},
}

# Create your views here.
def startpage(request):
	context = {
		"quizzes":quizzes,
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request, slug):
	context = {
		"quiz": quizzes[slug], 
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
		"question_number": number, 
		"question": u"Hur många bultar har ölandsbron?",
		"answer1": u"12",
		"answer2": u"66 400",
		"answer3": u"7 428 954",
		"quiz_slug": slug, 
	}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
		"correct": 12, 
		"total": 20, 
		"quiz_slug": slug, 
	}
	return render(request, "quiz/completed.html", context)
