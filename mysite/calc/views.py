from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def home(request):
     return render(request,"home.html",{'name':'Irfan Hussain'})
def results(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val=val1+val2
    return render(request,"result.html",{'name':'Irfan Hussain','results':val})

