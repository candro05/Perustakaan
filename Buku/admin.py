from django.contrib import admin
from .models import Buku,Jenis_Buku,Ketegori_Buku
# Register your models here.

admin.site.register(Buku)
admin.site.register(Ketegori_Buku)
admin.site.register(Jenis_Buku)