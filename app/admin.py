from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(PhoneAuth)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(ChatRoom)
admin.site.register(Post)