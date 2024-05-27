from django import forms
from app.models import *
'''
#using django form
g=[('MALE','male'),('FEMALE','female')] 
c=[('PYTHON','python'),('SQL','sql')]
class schoolform(forms.Form):
    sname=forms.CharField(max_length=10)
    sage=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    spassword=forms.CharField(widget=forms.PasswordInput)
    saddress=forms.CharField(widget=forms.Textarea(attrs={'cols':8,'rows':3}))
    #sgender=forms.ChoiceField(choices=g)
    sgender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
class TopicForm(forms.Form):
    topic_name=forms.CharField()'''

#using django modelform
class TopicForm(forms.ModelForm):
    class Meta:
        model=topic
        fields="__all__"

class WebpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields="__all__"

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields="__all__"#shows all col
        #fields=['author','type']#only shows mentioned cols
        #exclude=['type']#excludes the column
        help_texts={'name':'no integers'}
        labels={'author':'writer'}#you can change attribute/colname
        widgets={'type':forms.PasswordInput,'name':forms.Textarea}




