from django.shortcuts import render
from .models import Skill
# Create your views here.
def home(request):
    return render(request,'skills/home.html')

def likecount(request):

    return render(request,'skills/like.html')

def count(request):
    name = request.GET['fname']
    mail = request.GET['email']
    comment = request.GET['comment']

    lst = [name,mail,comment]
    f=open('commentdetails.txt','a+')
    for i in lst:
        f.write(i)
        f.write('\n')
    f.close()
    return render(request,'skills/count.html',{'name':name,'mail':mail,'comment':comment})

def techstack(request):
    skills = Skill.objects.all().order_by('-id')
    return render(request, 'skills/tech_stack.html',{'skills':skills})

def stack(request):
    return render(request, 'skills/stack.html')