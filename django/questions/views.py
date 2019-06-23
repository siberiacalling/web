from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from questions.models import Question, Answer


def paginate(objects_list, request, amount_objects_on_page):
    paginator = Paginator(objects_list, amount_objects_on_page)

    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)
    return objects_page


def create_page(data_list, data_on_page, page):
    paginator = Paginator(data_list, data_on_page)
    try:
        page_answers = paginator.page(page)
    except PageNotAnInteger:
        page_answers = paginator.page(1)
    except EmptyPage:
        page_answers = paginator.page(paginator.num_pages)
    return page_answers


def home_page(request):
    question_list = Question.objects.new()
    return render(request, 'questions/index.html',
                  {'questions': create_page(question_list, 10, request.GET.get('page')),
                   'title': 'New questions',
                   })


def hot(request):
    question_list = Question.objects.hot()
    return render(request, 'questions/hot_list.html',
                  {'questions': create_page(question_list, 10, request.GET.get('page')),
                   'title': 'Hot questions',
                   })


def ask(request):
    return render(request, 'questions/ask.html', {})


def signup(request):
    return render(request, 'questions/signup.html', {})


def login(request):
    return render(request, 'questions/login.html', {})


def one_question(request, q_id):
    q = Question.objects.by_id(q_id)
    answers_list = Answer.objects.new(q_id)
    return render(request, "questions/question.html",
                  {'answers': create_page(answers_list, 3, request.GET.get('page')),
                   'question': q,
                   'title': 'Hot questions',
                   })


def tag(request, my_tag):
    question_list = Question.objects.by_tags(my_tag)
    return render(request, 'questions/tag.html', {'questions': create_page(question_list, 10, request.GET.get('page')),
                                                  'title': 'Questions with tag: ' + my_tag,
                                                  'tag': my_tag,
                                                  })


def settings(request):
    return render(request, 'questions/settings.html', {})
