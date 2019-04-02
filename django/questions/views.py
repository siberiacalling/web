from django.shortcuts import render

def home_page(request):
    return render(request, 'questions/index.html', {})

def ask(request):
    return render(request, 'questions/ask.html', {})

def signup(request):
    return render(request, 'questions/signup.html', {})

def login(request):
    return render(request, 'questions/login.html', {})

def one_question(request):
    return render(request, 'questions/question.html', {})

def tag(request):
    return render(request, 'questions/tag.html', {})

def hot(request):
    return render(request, 'questions/hot_list.html', {})