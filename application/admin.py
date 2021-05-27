from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(University)
admin.site.register(Unit)
admin.site.register(Course)
admin.site.register(Year_Of_Study)
admin.site.register(File)