from django.contrib import admin
from .models import Blog
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':50})},
    }



admin.site.register(Blog , ModelAdmin)

