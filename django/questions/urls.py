from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ask/', views.ask, name='ask'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    #path
    url(r'^question/(?P<q_id>[0-9]+)$', views.one_question, name='one_question'),
    path('tag/(?P<tag_name>[\w\-]+)', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
    path('settings/', views.settings, name='settings'),
]