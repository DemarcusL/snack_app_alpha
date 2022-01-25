from django.contrib import admin
from django.db import models 

# Register your models here.
from .models import Snack

admin.site.register(Snack)
