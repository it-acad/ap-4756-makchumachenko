from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "str_user", "str_book", "created_at",
                    "planned_end_at", "end_at"]
    fieldsets = [
        (
            None,
            {
                "fields": ["user", "book", "planned_end_at"],
            },
        ),
        (
            "Actual return date",
            {
                "fields": ["end_at"],
            },
        ),
    ]

    @admin.display(description="User")
    def str_user(self, obj):
        return str(obj.user)

    @admin.display(description="Book")
    def str_book(self, obj):
        return str(obj.book)