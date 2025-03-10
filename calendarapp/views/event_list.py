from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView
from django.contrib import messages
from accounts.models import User
from accounts.models.user import Ville, Membres_logistique, Responsable, Materiel, SousCategorieMateriel, \
    CategorieMateriel
from calendarapp.forms import ResponsableForm, MembreForm, RespLogistiqueForm, MaterielForm, MaterielAddForm, \
    CategorieForm, SousCategorieForm
from calendarapp.models import Event


class AllEventsListView(ListView):
    """ All event list views """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class AjoutResponsableLogistiqueView(CreateView):
    """ Running events list view """

    template_name = "ajout-responsable.html"
    model = User
    form_class = RespLogistiqueForm
    success_url = reverse_lazy('responsables')
    def form_valid(self, form):
        return super().form_valid(form)

class AjoutMembreLogistiqueView(CreateView):
    """ Upcoming events list view """

    template_name = "ajout-membre.html"
    model = Membres_logistique
    form_class = MembreForm
    success_url = reverse_lazy('membres')

    def form_valid(self, form):
        return super().form_valid(form)
    
class CompletedEventsListView(ListView):
    """ Completed events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_completed_events(user=self.request.user)

class UsersListView(ListView):
    """ Completed events list view """

    template_name = "users.html"
    model = User

    def get_queryset(self):
        return User.objects.all()


class VillesListView(ListView):
    """ Completed events list view """

    template_name = "ville.html"
    model = Ville

    def get_queryset(self):
        return Ville.objects.all()


class MembresListView(ListView):
    """ Completed events list view """

    template_name = "membres.html"
    model = Membres_logistique

    def get_queryset(self):
        return Membres_logistique.objects.all()


class ResponsablesListView(ListView):
    """ Completed events list view """

    template_name = "responsables.html"
    model = Responsable

    def get_queryset(self):
        return Responsable.objects.all()


class MaterielsListView(ListView):
    """ Completed events list view """

    template_name = "materiels-list.html"
    model = Materiel

    def get_queryset(self):
        return Materiel.objects.all()


class MaterielView(CreateView):
    """ Materiel Add view """

    template_name = "add_materiel.html"
    model = Materiel
    form_class = MaterielAddForm

    success_url = reverse_lazy('calendarapp:materiels-logistique')

    def form_valid(self, form):
        return super().form_valid(form)

"""class CategoriesView(ListView):
  
    template_name = "categorie_page.html"
    model = SousCategorieMateriel

    def get_queryset(self):
        return SousCategorieMateriel.objects.all()"""


"""class AddCategoriesView(CreateView):

    template_name = "forms.html"
    model = Materiel
    form_class = MaterielAddForm

    success_url = reverse_lazy('calendarapp:categorie')

    def form_valid(self, form):
        new_category = None

        # Vérifie si une nouvelle catégorie a été envoyée
        new_categorie_nom = self.request.POST.get('new_categorie', '').strip()
        if new_categorie_nom:
            new_category, created = CategorieMateriel.objects.get_or_create(nom=new_categorie_nom)
            form.instance.categorie = new_category  # Associe la nouvelle catégorie

        response = super().form_valid(form)

        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = {'message': 'Matériel ajouté avec succès!', 'id': self.object.id}
            if new_category:
                data['new_category'] = {'id': new_category.id, 'nom': new_category.nom}

            return JsonResponse(data)

        return response

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'errors': form.errors}, status=400)

        return super().form_invalid(form)"""



def add_categorie(request):
    forms = SousCategorieForm
    sc = SousCategorieMateriel.objects.all()
    cat = request.POST.get('new_categorie')
    if request.method == "POST":
        if cat != None:
            print("Ok")
            CategorieMateriel.objects.create(
                nom=cat,
            )
            messages.success(request,f"Catégorie {cat} a été crée avec succès !")
            return redirect("calendarapp:add-cat")
        else:
            print("Error")
            messages.error(request,f"Catégorie {cat} n'a pas été crée !")

        forms = SousCategorieForm(request.POST)
        if forms.is_valid():
                scat = forms.save()
                messages.success(request,f"Sous-catégorie {scat.nom} a été crée avec succès !")
                return redirect("calendarapp:add-cat")
        else:
            messages.error(request,f"Une erreur est survenue lors de la création de la sous-catégorie !")
            print("--------------User limit exceed!-----------------")
    context = {"form": forms,"sc":sc}
    return render(request, "categorie_page.html", context)




