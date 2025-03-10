from django.forms import ModelForm, DateInput

from accounts.models.user import Responsable, Membres_logistique, User, Materiel, CategorieMateriel, \
    SousCategorieMateriel
from calendarapp.models import Event, EventMember
from django import forms

class MaterielForm(forms.Form):
    model = Materiel
    fields = ['__all__']

class MaterielAddForm(ModelForm):
    class Meta:
        model = Materiel
        fields = ["nom", "categorie","sous_categorie", "eglise", "etat","image","description"]
        # datetime-local is a HTML5 input type
        widgets = {
            "nom": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Baffle JBL RX45"}
            ),
            "categorie": forms.Select(
                attrs={"class": "form-control"}
            ),
            "sous_categorie": forms.Select(
                attrs={"class": "form-control"}
            ),
            "eglise": forms.Select(
                attrs={"class": "form-control"}
            ),
            "etat": forms.Select(
                attrs={"class": "form-control"}
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event description",
                }
            ),

        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "start_time", "end_time"]
        # datetime-local is a HTML5 input type
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event description",
                }
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]


from django import forms


class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = ['nom', 'prenom', 'email', 'phone','image']


class MembreForm(forms.ModelForm):
    class Meta:
        model = Membres_logistique
        fields = ['nom', 'prenom', 'email', 'phone','responsable','dprt','description','eglise','image']
        widgets = {
            "nom": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "prenom": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "responsable": forms.Select(
                attrs={"class": "form-control"}
            ),
            "dprt": forms.Select(
                attrs={"class": "form-control"}
            ),
            "eglise": forms.Select(
                attrs={"class": "form-control"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event description",
                }
            ),

        }


class RespLogistiqueForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'phone', 'dprt', 'eglise', 'image','password']
        widgets = {
            "nom": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Entrer votre nom"}
            ),
            "prenom": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Entrer votre prénom"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Entrer votre email"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Entrer votre numéro de téléphone"}
            ),
            "dprt": forms.Select(
                attrs={"class": "form-control"}
            ),
            "eglise": forms.Select(
                attrs={"class": "form-control"}
            ),
            "password": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Entrer votre mot de passe"}
            ),

        }


class CategorieForm(forms.ModelForm):
    class Meta:
        model = CategorieMateriel
        fields = ['nom']
        widgets = {
            "nom": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Sono"}
            )
        }

class SousCategorieForm(forms.ModelForm):
    class Meta:
        model = SousCategorieMateriel
        fields = ['nom','categorie']
        widgets = {
            "nom": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Sono"}
            ),
            "categorie":forms.Select(
                attrs={"class":"form-control"}
            )
        }