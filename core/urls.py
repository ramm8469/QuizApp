from django.urls import path,include
from .views import HomeView,CoreView
from .views import ProfileView, QuizView,ScoreBoardView,QuizListView

urlpatterns = [
    path('',HomeView.as_view(), name = "HomeView"),
    # For Login/Logout
    path('accounts/', include('django.contrib.auth.urls')),
    path('core/', CoreView.as_view(), name = 'CoreView'),
    path('core/profile/', ProfileView, name = 'profile' ),
    path('core/quiz/', QuizListView, name = "quizs"),
    path('core/scoreboard/', ScoreBoardView, name = "scoreboard"),
    path('core/quiz-instance/<int:set_type>/<int:id>/',QuizView, name = "QuizInstance"),


]
