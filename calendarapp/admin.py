from django.contrib import admin
from calendarapp import models
from accounts.models import User
from django.utils.html import format_html
from accounts.models.user import Departemets, CategorieMateriel, SousCategorieMateriel, Eglise, Ville, \
    Membres_logistique, Responsable, Materiel


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]


@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ["id", "event", "user", "created_at", "updated_at"]
    list_filter = ["event"]


class LogisticiensAdmin(admin.ModelAdmin):
    list_display = ("nom","phone" ,"email","image")
    list_filter = ["email","nom"]
    # Recherche sur les champs spécifiés
    search_fields = ('nom',)  # Recherche par titre et contenu

    # Afficher une miniature de l'image
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "Pas d'image"

    image_preview.short_description = 'Image'

admin.site.register(User, LogisticiensAdmin)
admin.site.register(Departemets)
admin.site.register(CategorieMateriel)
admin.site.register(SousCategorieMateriel)
admin.site.register(Eglise)
admin.site.register(Ville)
admin.site.register(Membres_logistique)
admin.site.register(Responsable)
admin.site.register(Materiel)
