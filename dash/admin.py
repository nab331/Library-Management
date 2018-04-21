# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Type
from .models import book,bookInstance,Issued
from django.contrib import admin

admin.site.register(Type)
admin.site.register(book)
admin.site.register(bookInstance)
admin.site.register(Issued)
# Register your models here.
