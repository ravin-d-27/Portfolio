from django.contrib import admin
from .models import Skill, Endorse, Achievements, Experience
# Register your models here.


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_date', 'to_date', 'order')
    list_editable = ('order',)

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill)
admin.site.register(Endorse)
admin.site.register(Achievements)

