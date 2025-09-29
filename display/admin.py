from django.contrib import admin
from .models import Project 
from .models import Aboutme
from .models import Profilepic
from .models import Resume
from .models import ContactMessage
# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(Resume)
admin.site.register(Project)
admin.site.register(Aboutme)
admin.site.register(Profilepic)

