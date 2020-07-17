from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    return render(request,'home/base.html')
def other(request):
    context={
        'k1':'welcome to the second page'
    }
    return render(request,'home/others.html',context)
def about(request):
    time=datetime.datetime.now()
    return render(request,'home/about.html',{'time':time})