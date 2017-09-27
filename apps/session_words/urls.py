from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index), #/session_words
        url(r'^add_word', views.add), #/session_words/add_word
        url(r'^clear', views.clear), #/session_words/clear
]
