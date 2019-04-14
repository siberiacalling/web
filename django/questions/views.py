import random

from django.shortcuts import render


def home_page(request):
    data = generate_question_list(30)
    question_list = {"question_list": data}
    return render(request, 'questions/index.html', context=question_list)


def ask(request):
    return render(request, 'questions/ask.html', {})


def signup(request):
    return render(request, 'questions/signup.html', {})


def login(request):
    return render(request, 'questions/login.html', {})


def one_question(request):
    data = generate_answers_list()
    question = generate_question()
    data = {"question": question, "answers": data}
    return render(request, 'questions/question.html', context=data)


def tag(request):
    data = generate_question_list(3)
    question_list = {"question_list": data}
    return render(request, 'questions/tag.html', context=question_list)


def settings(request):
    return render(request, 'questions/settings.html', {})


def hot(request):
    data = generate_question_list(30)
    question_list = {"question_list": data}
    return render(request, 'questions/hot_list.html', context=question_list)


def generate_question_list(questions_amount):
    questions = []
    for i in range(1, questions_amount):
        tags = ['tag' + str(random.randint(1, 20)), 'tag' + str(random.randint(1, 20))]

        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'tags': tags,
            'text': 'text' + str(i),
            'rating': random.randint(1, 50),
            'answers_amount': random.randint(1, 15)

        })
    return questions


def generate_question():
    tags = ['tag' + str(random.randint(1, 20)), 'tag' + str(random.randint(1, 20))]
    i = random.randint(1, 50)
    question = {
        'title': 'title' + str(i),
        'id': i,
        'tags': tags,
        'text': 'text' + str(i),
        'rating': random.randint(1, 50),
        'answers_amount': random.randint(1, 15)
    }
    return question


def generate_answers_list():
    questions = []
    for i in range(1, 7):
        questions.append({
            'title': 'answer' + str(i),
            'id': i,
            'text': 'text answer' + str(i),
            'rating': random.randint(1, 50),
        })
    return questions
