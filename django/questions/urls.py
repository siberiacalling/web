from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ask/', views.ask, name='ask'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path(r'question/<int:q_id>', views.one_question, name='one_question'),
    path('tag/<slug:tag_name>', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
    path('settings/', views.settings, name='settings'),
]
