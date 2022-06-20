from django.contrib import admin
from miapp.models import BlogModel
from miapp.views import blogs, index, nosotros, register
# Register your models here.


admin.site.register(blogs)

admin.site.register(index)

admin.site.register(nosotros)

admin.site.register(register)