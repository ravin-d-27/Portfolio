from django.shortcuts import render
from .models import Skill, Endorse
# Create your views here.
def home(request):
    return render(request,'skills/home.html')

def likecount(request):

    return render(request,'skills/like.html')

def count(request):
    name = request.GET['fname']
    mail = request.GET['email']
    comment = request.GET['comment']

    new_entry = Endorse(name=name, email_id=mail, endorsement=comment)

    # Save the new instance to the database
    new_entry.save()
    return render(request,'skills/count.html',{'name':name,'mail':mail,'comment':comment})

def techstack(request):
    skills = Skill.objects.all().order_by('-id')
    return render(request, 'skills/tech_stack.html',{'skills':skills})

def stack(request):
    return render(request, 'skills/stack.html')

def achievements(request):
    return render(request, 'skills/achievements.html')