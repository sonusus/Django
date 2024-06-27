from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CustomUser) 
admin.site.register(Userregistration)
admin.site.register(Booking)
admin.site.register(Answeruser)
admin.site.register(Question)
admin.site.register(Counsilerregistration)