from django.shortcuts import render, HttpResponse
from polls.models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request):
    return HttpResponse("안녕")

def results(request):
    return HttpResponse("메롱")

def vote(request):
    return HttpResponse("뇸뇸")