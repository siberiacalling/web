from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ask/', views.ask, name='ask'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('question/35/', views.one_question, name='one_question'),
    path('tag/blablabla/', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
]