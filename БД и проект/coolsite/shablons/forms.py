from django import forms
# from .models import *

prepods = [('Данилова','Данилова Л.Ф.'), ('Самков','Самков T.Л.'), ('Пушкарева','Пушкарева Г.B.'), ('Моргунов','Моргунов A.B.'), ('Полетайкин','Полетайкин A.Н.')]
# tuple_prepods = tuple(prepods)
course = [('МБП','МБП'), ('ПИ','ПИ'), ('БД','БД'), ('OC','OC'), ('ИнфИПрог','ИнфИПрог'), ('Web-технологии','Web-технологии'), ('Проектный практикум','Проектный практикум')]
# tuple_course = tuple(course)

chapters = [('C', 'Содержание'), ('В', 'Введение'), ('З', 'Заключение'), ('СИИ', '\tСписок использованных источников')]
# chapters = [('C', ' '), ('В', ' '), ('З', ' '), ('СИИ', ' ')]

# tuple_chapters = tuple(chapters)
# required=False
class CreateForm(forms.Form):
    professor = forms.ChoiceField(label='Преподаватель:', choices=prepods)
    course = forms.ChoiceField(label='Предмет:', choices=course)
    file_field = forms.FileField(label = 'Выберите файл:', required=False)
    FIO = forms.CharField(label = 'Введите ФИО:')
    # save = forms.UUIDField()
    standard_chapters = forms.ChoiceField(label = 'Выберите необходимые главы:', widget=forms.CheckboxSelectMultiple(attrs= {'class':'choice__place'}), choices=chapters)
    own_chapters = forms.CharField(label = 'Введите названия глав по вашей теме. Каждое название c новой строки.', widget=forms.Textarea(attrs={'rows':'6', 'style':'width: 100%; font-size: 16px; background-color: #444951; border-radius: 8px; padding: 5px 5px 5px 5px; color: #fff;'}))





    # Soderzanie = forms.BooleanField(required = False)
    # Vvedenie = forms.BooleanField(required = False)
    # Zakluchenie = forms.BooleanField(required = False)
    # List_of_use_sources = forms.BooleanField(required = False)

    # work = forms.ChoiceField(label='Тип работы:', widget=forms.RadioSelect(attrs={'class': 'Radio'}), 
    #                          choices=[('0','ребенок'),('1','бюджетник'),('2','безработный'),('3','фирма'),('4','частный предприниматель')])
    # widget=forms.CheckboxSelectMultiple
    # choices=tuple_chapters

    # vozrast = forms.ChoiceField(label='Введите Ваш возраст:', choices=[(x,x) for x in range(0, 120)])
    # pol = forms.ChoiceField(label='Выберите Ваш пол:', widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[('1','М'),('0','Ж')])
    # gip = forms.BooleanField(label='Гипертония', required = False)
    # heart = forms.BooleanField(label='Болезни сердца', required = False)
    # sem = forms.BooleanField(label='Семейный(ая)', required = False)
    # pro = forms.BooleanField(label='Городской(ая)', required = False)
    # work = forms.ChoiceField(label='Тип работы:', widget=forms.RadioSelect(attrs={'class': 'Radio'}), 
    #                          choices=[('0','ребенок'),('1','бюджетник'),('2','безработный'),('3','фирма'),('4','частный предприниматель')])
    # sax= forms.FloatField(label='Уровень сахара:')
    # kuru = forms.ChoiceField(label='Отношение к курению:', widget=forms.RadioSelect(attrs={'class': 'Radio'}), 
    #                          choices=[('0','не курю'),('1','ранее курил'),('2','неизвестно'),('3','курю')])
    # ves= forms.IntegerField(label='Вес (целое число)')
    # rost= forms.IntegerField(label='Рост (целое)')