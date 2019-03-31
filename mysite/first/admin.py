from django.contrib import admin

from first.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'email', 'gender', 'desc')

admin.site.register(Person, PersonAdmin)
