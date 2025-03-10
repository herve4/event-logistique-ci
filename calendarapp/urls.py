from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from eventcalendar.views import DashboardView
from . import views
from calendarapp.views.event_list import UsersListView, VillesListView, MaterielsListView, MaterielView, \
 add_categorie
from .views.other_views import add_eventmember, event_details, EventEdit, create_event, next_day, next_week, \
    delete_event, CalendarView, CalendarViewNew, EventMemberDeleteView

app_name = "calendarapp"


urlpatterns = [
    path("", DashboardView.as_view(), name="dash"),
    path("calenders/", CalendarView.as_view(), name="calendars"),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
    path('next_week/<int:event_id>/', next_week, name='next_week'),
    path('next_day/<int:event_id>/', next_day, name='next_day'),
    path("event/new/", create_event, name="event_new"),
    path("event/edit/<int:pk>/", EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", event_details, name="event-detail"),
    path(
        "add_eventmember/<int:event_id>", add_eventmember, name="add_eventmember"
    ),
    path(
        "event/<int:pk>/remove",
        EventMemberDeleteView.as_view(),
        name="remove_event",
    ),


    path(
        "logisticiens/",
        UsersListView.as_view(),
        name="logisticiens",
    ),
    path(
        "materiels-logistique/",
        MaterielsListView.as_view(),
        name="materiels-logistique",
    ),
    path(
        "ajouter-materiel/",
        MaterielView.as_view(),
        name="materiel",
    ),



    path(
          "ajouter-categorie/",
          add_categorie,
          name="add-cat",
      ),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
