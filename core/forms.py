from .models import QuestionSet10
from django import forms
from .models import Quizs,QuestionSet10,Questions

class QuizForm(forms.ModelForm):
    
    class Meta:
        model = Quizs
        fields = '__all__'


class QuestionSet10Form(forms.Form):
    # quiz = Quizs.objects.get(id = 2)
    # question_set = quiz.questions_set

    CHOICES = (('1','opt_1'),('2', 'opt_2'),('3', 'opt_3'),('4', 'opt_4'))
    option_1 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_2 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_3 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_4 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_5 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_6 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_7 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_8 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_9 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)
    option_10 = forms.ChoiceField(  widget=forms.RadioSelect, choices=CHOICES)


# class QuestionForm(forms.Form):
#     question = forms.CharField(max_length=300)
#     option_1 = forms.CharField(max_length = 30)
#     option_2 = forms.CharField(max_length = 30)
#     option_3 = forms.CharField(max_length = 30)
#     option_4 = forms.CharField(max_length = 30)

#     class Meta:
#         model = Questions
#         fields = ['question','option_1', 'option_2', 'option_3', 'option_4']

