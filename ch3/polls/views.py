from django.shortcuts import render, HttpResponse, get_object_or_404 
from .models import *


# Create your views here.
def index(request):
    data = Choice.objects.all()
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request):
    return HttpResponse("메롱")

def vote(request):
    return HttpResponse("뇸뇸")