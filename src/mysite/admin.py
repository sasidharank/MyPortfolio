from django.contrib import admin
from .models import visitors,contact,visitormails
# Register your models here.

admin.site.register(visitors)
admin.site.register(contact)
admin.site.register(visitormails)

