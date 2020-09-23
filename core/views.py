from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse

from django.urls import reverse_lazy
# from .forms import TechQuizForm,QuestionSet10Form,QuestionForm

# For prevention of clickjacking in case of iframe used
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_sameorigin,xframe_options_deny

from users.models import CustomUserModel

from core.models import Quizs
from .models import ScoreBoardModel
from .models import QuizDestributorModel_10,QuizDestributorModel_5

class HomeView(TemplateView):
    template_name = 'home.htm'


class CoreView(LoginRequiredMixin,TemplateView):
    template_name = 'core.htm'


@login_required
def ProfileView(request):
    host_add = request.get_host()
    host_port = request.get_port()
    user = request.user
    user_id = request.user.id
    
    # Getting the user details from database : return :- user_object
    user_obj = CustomUserModel.objects.get(id = user_id)

    # print(user_details_from_db.username)
    # print(user_details_from_db.email)
    # print(user_details_from_db.first_name)
    # print(user_details_from_db.last_name)

    context_data = {
        'host_add' : host_add,
        'host_port' : host_port,
        'user_obj' : user_obj,

    }

    return render(request, 'profile.htm', context_data)


@login_required
def QuizListView(request):
    question_set5_instances = None
    question_set10_instances = None
    
    set_5_flag = False
    set_10_flag = False

    try:
       question_set5_instances = list(QuizDestributorModel_5.objects.filter(user__id = request.user.id))
       print("*"*50)
       print(question_set5_instances)
       set_5_flag  = True

    except:
        print(" Error Occured during fetching question_set5_instance from DB.")

    try:
        question_set10_instances =  list(QuizDestributorModel_10.objects.filter(user__id = request.user.id))
        print("*"*50)
        print(question_set10_instances)
        set_10_flag = True

    except:
        print(" Error Occured during fetching question_set10_instance from DB.")

    if set_5_flag or set_10_flag :
        return render(request, 'quizlist.htm', {'question_set5_instances' : question_set5_instances, 'question_set10_instances' : question_set10_instances})
    else:
        return render(request, 'quizlist.htm', {'question_set5_instances' : None, 'question_set10_instances' : None} )


@login_required
def QuizView(request,set_type,id):

    print("set_type = ",set_type, " type : ", type(set_type))

    question_set5_instance = None
    question_set10_instance = None
    question_list_set5 = None
    question_list_set10 = None
    set_5_flag = False
    set_10_flag = False

    if set_type == 5:

        try:
            question_set5_instance = QuizDestributorModel_5.objects.get(id = id)
                # Getting all the questions list from the perticular set
            question_list_set5 = question_set5_instance.questions_list
            set_5_flag = True

        except:
            print(" Error Occured during fetching question_set5_instance from DB.")

    elif set_type == 10:

        try:
            question_set10_instance = QuizDestributorModel_10.objects.get(user__id = request.user.id)
            question_list_set10 = question_set10_instance.questions_list
            set_10_flag = True
        except:
            print(" Error Occured during fetching question_set10_instance from DB.")

        
    print("flag_5 : ", set_5_flag, " - ", "flag_10 : ", set_10_flag)

    user = request.user

    
    print(user.username)
    print(question_list_set5, " - ", question_list_set10)
    print("*"*50)
    print(question_set5_instance)

        

    if set_5_flag:

        if request.method == 'POST':

            answers_set5 = {
                'answer_1'  : request.POST.get('question_1'),
                'answer_2'  : request.POST.get('question_2'),
                'answer_3'  : request.POST.get('question_3'),
                'answer_4'  : request.POST.get('question_4'),
                'answer_5'  : request.POST.get('question_5'),
            }
            
            correct_answers_set5 = {
                'answer_1'  : question_list_set5.question_1.correct_option,
                'answer_2'  : question_list_set5.question_2.correct_option,
                'answer_3'  : question_list_set5.question_3.correct_option,
                'answer_4'  : question_list_set5.question_4.correct_option,
                'answer_5'  : question_list_set5.question_5.correct_option,
            }

            score = 0
            for key in answers_set5.keys():
                if answers_set5[key] == correct_answers_set5[key]:
                    # print(answers[key] ,'== ', correct_answers[key])
                    score += 1    

            # print('score : ', score)
            # Add score to score board
            score_board = ScoreBoardModel.objects.create(score = score, max_score=5, quiz = question_list_set5.name, user_id = user.id)
            score_board.save()
            
            
            context_data = {'user' : user, 'score' : score, 'max_score':5}
            return render(request, 'score.htm', context_data)
        

        context_data = {'id': id, 'set_type':set_type, 'question_set5_instance' : question_set5_instance, 'question_list_set5' : question_list_set5, 'user' : user} 
        return render(request, 'quizview_set5.htm', context_data)
    elif not set_10_flag:
        context_data = {'question_set5_instance' : None, 'all_users_in_set5' : None, 'question_list_set5' : None, 'user' : user} 
        return render(request, 'quizview_set5.htm', context_data)
    

    if set_10_flag:

        if request.method == 'POST':

            answers_set10 = {
                'answer_1'  : request.POST.get('question_1'),
                'answer_2'  : request.POST.get('question_2'),
                'answer_3'  : request.POST.get('question_3'),
                'answer_4'  : request.POST.get('question_4'),
                'answer_5'  : request.POST.get('question_5'),
                'answer_6'  : request.POST.get('question_6'),
                'answer_7'  : request.POST.get('question_7'),
                'answer_8'  : request.POST.get('question_8'),
                'answer_9'  : request.POST.get('question_9'),
                'answer_10'  : request.POST.get('question_10'),
            }

            correct_answers_set10 = {
                'answer_1'  : question_list_set10.question_1.correct_option,
                'answer_2'  : question_list_set10.question_2.correct_option,
                'answer_3'  : question_list_set10.question_3.correct_option,
                'answer_4'  : question_list_set10.question_4.correct_option,
                'answer_5'  : question_list_set10.question_5.correct_option,
                'answer_6'  : question_list_set10.question_6.correct_option,
                'answer_7'  : question_list_set10.question_7.correct_option,
                'answer_8'  : question_list_set10.question_8.correct_option,
                'answer_9'  : question_list_set10.question_9.correct_option,
                'answer_10'  : question_list_set10.question_10.correct_option,
            }

            score = 0
            for key in answers_set10.keys():
                if answers_set10[key] == correct_answers_set10[key]:
                    # print(answers[key] ,'== ', correct_answers[key])
                    score += 1    

            # print('score : ', score)
            # Add score to score board
            score_board = ScoreBoardModel.objects.create(score = score,max_score=10, quiz = question_list_set10.name, user_id = user.id)
            score_board.save()

            context_data = {'user' : user, 'score' : score, 'max_score':10,}
            return render(request, 'score.htm', context_data)
        print("from set 10 before error")
        context_data = {'id': id, 'set_type':set_type, 'question_set10_instance' : question_set10_instance, 'question_list_set10' : question_list_set10, 'user' : user} 
        return render(request, 'quizview_set10.htm', context_data)

    else:
        print("from set 10 after error")
        context_data = {'question_set10_instance' : None, 'question_list_set10' : None, 'user' : user} 
        return render(request, 'quizview_set10.htm', context_data)

   
    

@login_required
def ScoreBoardView(request):

    user = request.user
    user_score = 0
    quiz = 0
    try:
        user_scores = ScoreBoardModel.objects.filter(user_id = user.id)
    except :
        print("Error occured, No Score for user ", user.username," found in DB")
        context_data = {'user_scores.score' : 0, 'user' : user}
        return render(request, 'scoreboard.htm', context_data)

    # print(user_scores, " - ", quizs)
    context_data = {'user_scores' : user_scores, 'user' : user}
    return render(request, 'scoreboard.htm', context_data)

