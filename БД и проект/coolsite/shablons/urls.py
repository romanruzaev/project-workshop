from django.urls import path

from . import views

app_name = 'shablons'
urlpatterns = [
    #http://127.0.0.1:8000/
    path('', views.index, name='index'),
    #http://127.0.0.1:8000/create_file/
    path('create_file/', views.create, name = 'create'),
    #http://127.0.0.1:8000/check_file/
    path('check_file/', views.check, name = 'check'),
    # path('result/', views.result, name = 'result'),
    # path('upload/', views.upload_file, name = 'upload'),
    
    # ex: /polls/1/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/1/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/1/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]