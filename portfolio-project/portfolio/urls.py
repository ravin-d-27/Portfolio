
from django.contrib import admin
from django.urls import path, include

#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static

#add the following:
import skills.views
import blog.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',skills.views.home,name='home'),
    path('blog/',blog.views.bloghome,name='bloghome'),
    path('viewdetails1/',blog.views.viewdetails1,name='viewdetails1'),
    path('likecount/',skills.views.likecount,name='likecount'),
    path('count/',skills.views.count,name='count'),
    path('techstack/',skills.views.techstack,name='techstack'),
    path('stack/',skills.views.stack,name='stack'),
    path('achievements/',skills.views.achievements,name='achievements'),
    path('experience/',skills.views.experience,name='experience'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
