from django.db import models
from users.models import CustomUserModel

# Create your models here.

class Questions(models.Model):
    question = models.TextField(max_length = 300)
    option_1 = models.CharField(max_length = 30)
    option_2 = models.CharField(max_length = 30)
    option_3 = models.CharField(max_length = 30)
    option_4 = models.CharField(max_length = 30)
    correct_option = models.CharField(max_length = 30)

    def __str__(self):
        return self.question

class QuestionSet10(models.Model):
    name = models.CharField(max_length = 30)
    question_1 = models.ForeignKey(Questions, on_delete= models.CASCADE)
    question_2 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_3 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_4 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_5 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_6 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_7 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_8 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_9 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_10 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')

    def __str__(self):
        return self.name


class QuestionSet5(models.Model):
    name = models.CharField(max_length = 30)
    question_1 = models.ForeignKey(Questions, on_delete= models.CASCADE)
    question_2 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_3 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_4 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    question_5 = models.ForeignKey(Questions, on_delete= models.CASCADE, related_name= '+')
    
    def __str__(self):
        return self.name

# Depricated Code, will be removed before going live
class Quizs(models.Model):
    name = models.CharField(max_length = 50)
    author = models.ForeignKey(CustomUserModel, on_delete = models.CASCADE)
    questions_set = models.ForeignKey( QuestionSet10, on_delete= models.CASCADE,)
    # users = models.ManyToManyField(CustomUserModel)


    def __str__(self):
        return self.name


class ScoreBoardModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete = models.CASCADE)
    quiz = models.CharField(max_length = 255)
    score = models.PositiveSmallIntegerField()
    max_score = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class QuizDestributorModel_10(models.Model):
    name = models.CharField(max_length = 255)
    user = models.ManyToManyField(CustomUserModel)
    questions_list = models.ForeignKey(QuestionSet10, on_delete=models.PROTECT, related_name='+')
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='+')
    created_on = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.name

class QuizDestributorModel_5(models.Model):
    name = models.CharField(max_length = 255)
    user = models.ManyToManyField(CustomUserModel)
    questions_list = models.ForeignKey(QuestionSet5, on_delete=models.PROTECT, related_name='+')
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='+')
    created_on = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.name



