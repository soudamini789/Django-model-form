from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
'''
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse('topic created')
    return render(request,'insert_topic.html')'''

'''
def insert_topic(request):
        TO=TopicForm()
        d={'TO':TO}
        if request.method=='POST':
            TOO=TopicForm(request.POST)
            if TOO.is_valid():
                tn=TOO.cleaned_data
                to=topic.objects.get_or_create(topic_name=tn)[0]
                to.save()
                return HttpResponse('topicdata submitted')
            else:
                return HttpResponse('invalid data')
        return render(request,'insert_topic.html',d)#using django forms
    
def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        cr=request.POST['cr']
        to=topic.objects.get(topic_name=tn)
        wo=webpage.objects.get_or_create(topic_name=tn,name=na,creater=cr)[0]
        wo.save()
        return HttpResponse('wp created')
    return render(request,'insert_webpage.html')

def School(request):
    SCL=schoolform()
    d={'SCL':SCL}
    if request.method=='POST':
        SCLO=schoolform(request.post)
        if SCLO.is_valid():
            print(SCLO.cleaned_data)
            return HttpResponse('data submitted')
        else:
            return HttpResponse('invalid data')
    return render(request,'school.html',d)'''

#using django model form
def insert_topic(request):
        TO=TopicForm()
        d={'TO':TO}
        if request.method=='POST':
            TOO=TopicForm(request.POST)
            if TOO.is_valid():
                TOO.save()
                return HttpResponse('topicdata submitted')
            else:
                return HttpResponse('invalid data')
        return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('wp created')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_webpage.html',d)

def insert_AccessRecords(request):
     ARFO=AccessRecordForm()
     d={'ARFO':ARFO}
     if request.method=='POST':
            ARFD=AccessRecordForm(request.POST)
            if ARFD.is_valid():
                 ARFD.save()
                 return HttpResponse('AR created')
            else:
                 return HttpResponse('invalid data') 
     return render(request,'insert_accessrecords.html',d)



    