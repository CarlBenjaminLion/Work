# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.template import loader

# Create your views here.
# ###############################################################################
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
# ###############################################################################


def index(request):
    # return HttpResponse("Hello, World.You're at polls index.\n"+str(request))
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    '''
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    :param request:
    :param question_id:
    :return: render(request, 'polls/detail.html', {'question': question})
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # The get_object_or_404() function takes a Django model as its first argument and
    # an arbitrary number of keyword arguments, which it passes to the get()
    # function of the model’s manager. It raises Http404 if the object doesn’t exist.


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

