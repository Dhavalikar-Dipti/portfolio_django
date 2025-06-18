from django.shortcuts import render,HttpResponse
from home.models import Contact

def home(request):
    #return HttpResponse("This is my home page")
    context ={'name':'Dipti','about':'learning django'}
    return render(request,'home.html',context)
def about(request):
    #return HttpResponse("This is my about page")
    return render(request,'about.html')
def projects(request):
    #return HttpResponse("This is my projects page")
    return render(request,'projects.html')
def contact(request):
    #return HttpResponse("This is my contact page")
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        ins= Contact(name=name,email=email,desc=desc)
        ins.save()
        print("the data has been written into the db")
    return render(request,'contact.html')

# Create your views here.
