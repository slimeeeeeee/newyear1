#from django.template import loader
#from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

#def index(request):
#    # return HttpResponse("Привет, народ! Здесь проводятся опросы.")
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.all()[:1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#def detail(request, question_id):
#    # return HttpResponse(f"Вы смотрите на вопрос №{question_id}.")
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Вопрос не существует")
#    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

#def vote(request, question_id):
#    return HttpResponse(f"Вы ответили на вопрос №{question_id}.")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = Choice()
    choice.question = question
    choice.choice_text = request.POST['choicetext']
    choice.choice_text2 = request.POST['choicetext2']
    choice.choice_text3 = request.POST['choicetext3']
    choice.choice_text4 = request.POST['choicetext4']
    choice.save()
    question.votes += 1
    question.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#def results(request, question_id):
#    response = f"Вы смотрите на ответы по вопросу №{question_id}."
#    return HttpResponse(response)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = Choice.objects.filter(question=question).latest('id')
    return render(request, 'polls/results.html', {'question': question, 'choice': choice })
