from django.shortcuts import render
from .models import Skill, Endorse, Achievements, Experience
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
    xyz = Achievements.objects.all().order_by('-id')
    return render(request, 'skills/achievements.html', {'xyz':xyz})

def experience(request):
    exp = Experience.objects.all()
    return render(request, 'skills/experience.html', {'exp':exp})

# NLP Extension

def review_spot(request):
    return render(request, 'skills/review_spot.html')

def pred(request):
    return render(request, 'skills/preds.html')

def find(request):
    import re
    import pickle
    import tensorflow as tf
    import nltk
    import numpy as np
    nltk.download("stopwords")
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer 

    corpus = []
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    if request.method == 'POST':
        review = request.POST['review']
        reviews = re.sub("[^a-zA-Z]", " ", review)
        reviews = reviews.lower()
        reviews = reviews.split()
        ps = PorterStemmer()
        reviews = [ps.stem(word) for word in reviews if not word in set(all_stopwords)]
        reviews = ' '.join(reviews)
        corpus.append(reviews)

        file_open = open("skills/vectorise.dat", "rb+")
        vect = pickle.load(file_open)

        md = tf.keras.models.load_model("skills/Trained_Model.h5")
        a = vect.transform(corpus).toarray()
        p = md.predict(a)

        predict = np.argmax(p)

        st = ""
        if (predict==1):
            st = "The Given review is a Positive Review"
        else:
            st = "The Given review is a Negative Review"
        
        print(st)

    return render(request, 'skills/finder.html', {"msg":st, "rev":review})