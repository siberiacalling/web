import random
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response


def paginate(objects_list, request):
    paginator = Paginator(objects_list, settings.AMOUNT_OBJECTS_ON_PAGE)

    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)
    return objects_page


def home_page(request):
    question_list = generate_question_list_by_amount(30)
    questions = paginate(question_list, request)
    return render_to_response('questions/index.html', {"questions": questions})


def hot(request):
    question_list = generate_question_list_by_amount(30)
    questions = paginate(question_list, request)
    return render_to_response('questions/hot_list.html', {"questions": questions})


def ask(request):
    return render(request, 'questions/ask.html', {})


def signup(request):
    return render(request, 'questions/signup.html', {})


def login(request):
    return render(request, 'questions/login.html', {})


def one_question(request, q_id):
    question = generate_question(q_id)
    answers_list = generate_answers_list(random.randint(1, 25))
    answers = paginate(answers_list, request)
    return render(request, "questions/question.html", {"question": question, "answers": answers})


def tag(request, tag_name):
    data = generate_question_list_by_tag(tag_name)
    return render(request, 'questions/tag.html', {"question_list": data, "tag": tag_name})


def user_settings(request):
    return render(request, 'questions/settings.html', {})


def generate_question_list_by_tag(tag_name):
    questions = []
    for i in range(1, settings.QUESTIONS_AMOUNT_PER_TAG):
        tags = ['tag' + str(random.randint(1, 20)), 'tag' + str(random.randint(1, 20)), tag_name]

        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'tags': tags,
            'text': 'text' + str(i),
            'rating': random.randint(1, 50),
            'answers_amount': random.randint(1, 15)

        })
    return questions


def generate_question_list_by_amount(questions_amount):
    questions = []
    for i in range(1, questions_amount):
        tags = ['tag' + str(random.randint(1, 20)), 'tag' + str(random.randint(1, 20)), ]

        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'tags': tags,
            'text': 'text' + str(i),
            'rating': random.randint(1, 50),
            'answers_amount': random.randint(1, 15)

        })
    return questions


def generate_questions(questions_amount):
    questions = []
    for i in range(1, questions_amount):
        questions.append('title' + str(i))
    return questions


def generate_question(q_id):
    tags = ['tag' + str(random.randint(1, 20)), 'tag' + str(random.randint(1, 20))]
    question = {
        'title': 'title' + str(q_id),
        'id': q_id,
        'tags': tags,
        'text': 'text' + str(q_id),
        'rating': random.randint(1, 50),
        'answers_amount': random.randint(1, 15)
    }
    return question


def generate_answers_list(answers_amount):
    questions = []
    for i in range(answers_amount):
        questions.append({
            'title': 'answer' + str(i),
            'id': i,
            'text': 'text answer' + str(i),
            'rating': random.randint(1, 50),
        })
    return questions
