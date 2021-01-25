from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(University)
admin.site.register(Unit)
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Type)
admin.site.register(Material)
admin.site.register(Book)