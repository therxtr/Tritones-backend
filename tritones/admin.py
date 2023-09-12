from django.contrib import admin
from .models import Member, boardMember, contactModel
# Register your models here.
admin.site.register(Member)
admin.site.register(boardMember)
admin.site.register(contactModel)
