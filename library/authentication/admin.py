from django import forms
from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id", "email", "full_name", "role",
        "is_active", "last_login",
    ]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "first_name", "middle_name", "last_name",
                    "email", "password", "role", "is_active",
                ],
            },
        ),
        (
            "User information",
            {
                "classes": ["collapse"],
                "fields": [
                    "created_at", "updated_at", "last_login",
                    "is_superuser", "is_staff",
                ],
            },
        ),
    ]

    readonly_fields = [
        "created_at", "updated_at", "is_superuser",
        "is_staff", "last_login",
    ]

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "password":
            kwargs["widget"] = forms.PasswordInput()
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    @admin.display(description="Full Name")
    def full_name(self, obj):
        return " ".join(
            i for i in (obj.first_name, obj.last_name)
            if i is not None
        )