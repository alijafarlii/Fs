from django.contrib import admin
from core.models import *

admin.site.register([User, Recipe, Story, Category, Comment, Tag, Contact,])