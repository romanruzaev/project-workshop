from docx import Document
from docxcompose.composer import Composer
from docx.shared import Pt, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
# import PySimpleGUI as sg
import os
import mimetypes

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import *
# from .models import *

from .models import Choice, Question

# def upload_file(request):
#     if ()

# Define function to download pdf file using template
# def download_file(request, filename=''):
#     if filename != '':
#         # Define Django project base directory
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Define the full file path
#         filepath = BASE_DIR + '/filedownload/Files/' + filename
#         # Open the file for reading content
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % filename
#         # Return the response value
#         return response
#     else:
#         # Load the template
#         return render(request, 'shablons/download.html')

# def download_file(request, filename):
#     # Define Django project base directory
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # Define text file name
#     # filename = 'test.docx'
#     # Define the full file path
#     filepath = BASE_DIR + '/filedownload/Files/' + filename
#     # Open the file for reading content
#     path = open(filepath, 'r')
#     # Set the mime type
#     mime_type, _ = mimetypes.guess_type(filepath)
#     # Set the return value of the HttpResponse
#     response = HttpResponse(path, content_type=mime_type)
#     # Set the HTTP header for sending to browser
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     # Return the response value
#     return response

# def download_file(request):
#     # Define Django project base directory
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # Define text file name
#     filename = 'test.txt'
#     # Define the full file path
#     filepath = BASE_DIR + '/filedownload/Files/' + filename
#     # Open the file for reading content
#     path = open(filepath, 'r')
#     # Set the mime type
#     mime_type, _ = mimetypes.guess_type(filepath)
#     # Set the return value of the HttpResponse
#     response = HttpResponse(path, content_type=mime_type)
#     # Set the HTTP header for sending to browser
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     # Return the response value
#     return response

def calculation(param):
    professor = param['professor']# ФИО ПРЕПОДАВАТЕЛЯ
    course = param['course'] # НАЗВАНИЕ КУРСА
    # file_field = param['file_field'] # WORD ФАЙЛ
    FIO = param['FIO'] # ФИО СТУДЕНТА
    standard_chapters = param['standard_chapters'] # ОБЩИЕ ГЛАВЫ (СОДЕРЖАНИЕ, ВВЕДЕНИЕ, ЗАКЛЮЧЕНИЕ, СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ)
    own_chapters = param['own_chapters'] # УНИКАЛЬНЫЕ ГЛАВЫ
    res = {}
    res['professor'] = professor
    res['course'] = course
    res['FIO'] = FIO
    res['standard_chapters'] = standard_chapters
    res['own_chapters'] = own_chapters
    return res
    # files = ''
    # zagl = standard_chapters
    # # ['Содержание', 'Введение', 'Заключение', 'Список использованных источников']#заголовки
    # full_zagl = []#полные заголовки???
    # way = (os.path.dirname(os.path.abspath(__file__))+'/').replace('\\','/')#путь 
    # files_list= [way+'ideal.docx', '', way+'f1u8y57.docx', ''] #идеал, титульник, временный, конечный
    # # os.path.dirname(os.path.abspath(__file__))#лишнее кажется
    # zagl_user = []

    # for i in range(0, len(zagl)):#для 4 итераций (перебираем вот это: 'Содержание', 'Введение', 'Заключение', 'Список использованных источников')
    #     if (values[i+5] == True):#если поставлена галочка
    #         full_zagl.append(zagl[i])  #добавляем ключевые заголовки
    #     if (i == 1): #если заголовок введение (выше уже добавили), нужно проверить новые заголовки
    #         if (values['-INPUT-'] != ''):#если в поле для уникальных глав что-то написано
    #             zagl_user = values['-INPUT-'].split('\n')#переменная хранит уникальные главы юзера
    #             for k in range(0, len(zagl_user)):#для всех юзерских заголовков
    #                  full_zagl.append(zagl_user[k])#добавляем юзерские заголовки


    # return professor
    #-----------------------------------------------------------------------

    # way = (os.path.dirname(os.path.abspath(__file__))+'/').replace('\\','/')#путь 
    # files_list= [way+'ideal.docx', '', way+'f1u8y57.docx', ''] #идеал, титульник, временный, конечный
    # if file_field != None:#если выбран путь до альтернативного титульника
    #     # files_list[0] = file_field.path #путь до титульника равен путю до альтернативного титульника
    #     pass
    # else:#если не выбран титульник (4 вариант)
    #     # files_list[1] = (way+values[0].split(' ')[0]+' '+values[1].split(' ')[0]+'.docx').replace('\\','/')#путь до титульника равен (путь+фамилия препода+пробел+предмет+.docx)
    #     pass
    
    # with open('some/file/name.txt', 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    

def index(request):
    return render(request, 'shablons/create.html')

def create(request):
    # if request.method=='POST':
    # #    form=insform(request.POST)
    #    if form.is_valid():
    #        ag=request.POST.get('vozrast')
    #        sx=request.POST.get('pol')
    #        if request.POST.get('gip')=='on':
    #            hyp=1
    #        else:
    #            hyp=0
    #        if request.POST.get('heart')=='on':
    #            heart=1
    #        else:
    #            heart=0
    #        if request.POST.get('sem')=='on':
    #            evert=1
    #        else:
    #            evert=0
    #        work=request.POST.get('work')
    #        if request.POST.get('pro')=='on':
    #            resid=1
    #        else:
    #            resid=0
    #        smok=request.POST.get('kuru')
    #        gluk=request.POST.get('sax')
    #        w=request.POST.get('ves')
    #        h=request.POST.get('rost')
    #        ar={}
    #        ar['sx']=sx
    #        ar['ag']=ag
    #        ar['hyp']=hyp
    #        ar['heart']=heart
    #        ar['evert']=evert
    #        ar['work']=work
    #        ar['resid']=resid
    #        ar['smok']=smok
    #        ar['gluk']=gluk
    #        ar['w']=w
    #        ar['h']=h
    #        insu={}
    #        ri1=raschet(ar)
    #        ri2=round(ri1[0][0],2)
    #        if ri2>=0 and ri2<=10:
    #            aa="Все нормально. Еще поживете!"
    #        elif ri2>=10 and ri2<=50:
    #            aa="Пора задуматься о здоровье!"
    #        elif ri2>50:
    #            aa="Ничего хорошего. По краю ходим!"
    #        insu['tex']=aa
    #        insu['res']=str(ri2)
    #        insu['posts']=p
    #        return render(request, 'rezult.html', insu)#{'tex':insu['tex'], 'res':insu['res'], 'posts':p})insu
    # else:
    #     form=insform()
    #     args={}
    #     args['form']=form
    # return render(request, 'expert.html',args)

    # posts = Shablons.objects.all()
    if request.method == "POST":
        form = CreateForm(request.POST)
        # file_field = request.FILES['file_field']
        if form.is_valid():
            
            professor = request.POST.get('professor')
            course = request.POST.get('course')
            FIO = request.POST.get('FIO')
            standard_chapters = request.POST.get('standard_chapters')
            own_chapters = request.POST.get('own_chapters')
            param = {}
            param['professor'] = professor
            param['course'] = course
            # param['file_field'] = file_field
            param['FIO'] = FIO
            param['standard_chapters'] = standard_chapters
            param['own_chapters'] = own_chapters
            # res = {}
            calc = calculation(param)
            return render(request, 'shablons/result.html', {"calc": calc})
        

            # document = Document()
            # document.add_heading('Document Title', 0)

            # response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            # response['Content-Disposition'] = 'attachment; filename=download.docx'
            # document.save(response)

            # return response



            # return HttpResponseRedirect(reverse('shablons:result', args=(calc,)))
            # return render(request, 'shablons/result.html', res)
            # return HttpResponseRedirect(reverse('shablons:result'))
            # return HttpResponse("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF!")
            
            
            # file_field = request.FILES['file_field']
            # return HttpResponse("The name of uploaded file is " + str(file_field))
            # form = CreateForm()

            # if request.POST.get('file_field')!= None:                
                # file_field = request.POST.get('file_field')
                # calc = calculation(request.FILES['file_field'], param)
            # calculation(request.FILES['file_field'], param)
            # calc = calculation(param)
            # return HttpResponse("OK!!!")
        
    else:
        form = CreateForm()
    return render(request, 'shablons/create_file.html', {"form": form})

def check(request):
    return render(request, 'shablons/check_file.html')


# def result(request):
#     return render(request, 'shablons/result.html')




#-----------------------------------------------------------------------------------------
# def index(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # context = {'latest_question_list': latest_question_list}
#     return render(request, 'shablons/create.html')

# # def detail(request, question_id):
# #     question = get_object_or_404(Question, pk=question_id)
# #     return render(request, 'shablons/detail.html', {'question': question})

# def create(request):
#     # question = get_object_or_404(Question, pk=question_id)
#     form = CreateForm()
#     return render(request, 'shablons/create_file.html', {"form": form})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'shablons/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'shablons/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('shablons:results', args=(question.id,)))
    

#----------------------------------------------------------------------------------------------

# class IndexView(generic.ListView):
#     template_name = 'shablons/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'shablons/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'shablons/results.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'shablons/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('shablons:results', args=(question.id,)))