"""eventcalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from calendarapp.views.event_list import VillesListView, MembresListView, ResponsablesListView, \
    CompletedEventsListView, AllEventsListView, AjoutResponsableLogistiqueView, \
    AjoutMembreLogistiqueView, UsersListView
from .views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("calendrier/", include("calendarapp.urls")),
    path(
          "villes/",
          VillesListView.as_view(),
          name="villes",
        ),
    path(
          "membres/",
          MembresListView.as_view(),
          name="membres",
        ),
    path(
          "responsables/",
          ResponsablesListView.as_view(),
          name="responsables",
        ),
    path("all-event-list/", AllEventsListView.as_view(), name="all_events"),
    path(
        "Ajouter-un-responsable/",
        AjoutResponsableLogistiqueView.as_view(),
        name="ajout-responsable",
    ),
    path(
        "Ajouter-un-membre/",
        AjoutMembreLogistiqueView.as_view(),
        name="ajout-membre",
    ),
    path(
        "completed-event-list/",
        CompletedEventsListView.as_view(),
        name="completed_events",
    ),
    path(
        "utilisateurs/",
        UsersListView.as_view(),
        name="users",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
