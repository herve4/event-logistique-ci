from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from accounts.models import User
from accounts.models.user import Eglise, Materiel, Membres_logistique
from calendarapp.models import Event


class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "calendarapp/dashboard.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.get_all_events(user=request.user)
        running_events = Event.objects.get_running_events(user=request.user)
        latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
        completed_events = Event.objects.get_completed_events(user=request.user)
        upcoming_events = Event.objects.get_upcoming_events(user=request.user)
        total_user_events = User.objects.all().count()
        total_eglise = Eglise.objects.all().count()
        total_materiel = Materiel.objects.all().count()
        total_membre_logistique = Membres_logistique.objects.all().count()
        context = {
            "total_event": events.count(),
            "running_events": running_events,
            "latest_events": latest_events,
            "completed_events": completed_events.count(),
            "upcoming_events": upcoming_events,
            "total_user_events": total_user_events,
            "total_eglise": total_eglise,
            "total_materiel": total_materiel,
            "total_membre_logistique": total_membre_logistique,
        }
        return render(request, self.template_name, context)
