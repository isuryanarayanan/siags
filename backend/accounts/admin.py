from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from accounts.models.user import User
from accounts.models.profiles.teacher import teacher_profile
from accounts.models.profiles.student import student_profile
from accounts.models.profiles.administrator import administrator_profile
from django.core.exceptions import ValidationError

admin.site.site_header = 'Student management and guidance system'

admin.site.register(student_profile)
admin.site.register(teacher_profile)
admin.site.register(administrator_profile)


class user_admin(UserAdmin):
    list_display = ('email', 'mode')
    list_filter = ('mode',)

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',  'mode')}),
        ('Personal info', {'fields': ()}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'mode')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, user_admin)
