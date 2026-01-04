from django.contrib import admin
from .models import Company, Client, Interaction


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company", "owner")
    search_fields = ("name", "email")
    list_filter = ("company",)
    ordering = ("name",)


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("client", "user", "date")
    search_fields = ("client__name", "notes")
    list_filter = ("date",)
