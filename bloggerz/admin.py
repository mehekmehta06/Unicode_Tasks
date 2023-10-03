from django.contrib import admin
from .models import *

"""
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'Fname', 'Lname', 'password', 'email_id')
admin.site.register(Register, RegisterAdmin)
"""

class BlogcreationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'content', 'image', 'created_on', 'updated_on')
admin.site.register(Blogcreation, BlogcreationAdmin)