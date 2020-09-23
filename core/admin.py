from django.contrib import admin
from .models import Quizs, QuestionSet10,Questions,ScoreBoardModel
from .models import QuizDestributorModel_10,QuizDestributorModel_5,QuestionSet5

# Register your models here.
admin.site.register(Quizs)
admin.site.register(QuestionSet10)
admin.site.register(Questions)
admin.site.register(ScoreBoardModel)
admin.site.register(QuizDestributorModel_10)
admin.site.register(QuizDestributorModel_5)
admin.site.register(QuestionSet5)