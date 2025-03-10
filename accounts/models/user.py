from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _


class Departemets(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"

class Responsable(models.Model):
    nom = models.CharField(max_length=100,verbose_name="Nom")
    prenom = models.CharField(max_length=200, null=True, blank=True,verbose_name="Prénoms")
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name="Email")
    phone = models.CharField(max_length=100, null=True, blank=True,verbose_name="Téléphone")
    image = models.ImageField(upload_to='images_responsables/', blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        verbose_name = _("Responsable église")
        verbose_name_plural = _("Responsables églises")

class Ville(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"

class Eglise(models.Model):
    adresse = models.CharField(max_length=200, null=True, blank=True,verbose_name="Adresse")
    membre_eglise = models.PositiveBigIntegerField(null=True, blank=True,verbose_name="Nombre de membre de l'église")
    ville =models.ForeignKey('Ville',on_delete=models.CASCADE, related_name='eglise',null=True,blank=True)
    responsable =models.ForeignKey('Responsable',on_delete=models.CASCADE, related_name='eglise',null=True,blank=True,verbose_name="Responsable de l'église")
    image = models.ImageField(upload_to='images_eglises/', blank=True, null=True,verbose_name="Image")

    def __str__(self):
        return f"{self.ville}"

class Membres_logistique(models.Model):
    nom = models.CharField(max_length=100,verbose_name="Nom")
    prenom = models.CharField(max_length=200, null=True, blank=True,verbose_name="Prénoms")
    email = models.CharField(max_length=200, null=True, blank=True,verbose_name="Email")
    phone = models.CharField(max_length=100, null=True, blank=True,verbose_name="Téléphone")
    responsable = models.ForeignKey('Responsable',on_delete=models.CASCADE, related_name='membre_eglise',null=True,blank=True)
    dprt = models.ForeignKey("Departemets",related_name='dprt',on_delete=models.CASCADE,null=True,blank=True,verbose_name="Département")
    description = models.TextField(max_length=1000, null=True, blank=True,verbose_name="Description")
    image = models.ImageField(upload_to='images_membres_logisticiens', blank=True, null=True,verbose_name="Image")
    eglise = models.ForeignKey(Eglise, on_delete=models.CASCADE, related_name='membres_logistique', null=True,
                               blank=True, verbose_name="Eglise")
    created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class UserManager(BaseUserManager):
    """ User manager """

    def _create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        if not email:  # check for an empty email
            raise AttributeError("User must set an email address")
        else:  # normalizes the provided email
            email = self.normalize_email(email)

        # create user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes/encrypts password
        user.save(using=self._db)  # safe for multiple databases
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password=None, **extra_fields):
        """Creates and returns a new staffuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """

    email = models.EmailField(
        _("Email Address"),
        max_length=255,
        unique=True,
        help_text="Ex: example@example.com",
    )
    nom = models.CharField(_("Nom"), max_length=255, null=True, blank=True)
    prenom = models.CharField(_("Prénoms"), max_length=255, null=True, blank=True)
    phone = models.CharField(_("Téléphone"), max_length=255, null=True, blank=True, unique=True)
    dprt = models.ForeignKey("Departemets", null=True, blank=True, on_delete=models.CASCADE,verbose_name="Département")
    eglise = models.ForeignKey('Eglise', on_delete=models.SET_NULL, null=True, related_name='utilisateurs')
    image = models.ImageField(_("Image"), upload_to="users", null=True, blank=True)
    is_staff = models.BooleanField(_("Staff status"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.nom} {self.prenom}" if self.nom != "" and self.prenom != "" else self.email

    def get_short_name(self):
        return self.nom if self.nom != "" else self.email

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'


class CategorieMateriel(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class SousCategorieMateriel(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(CategorieMateriel, on_delete=models.CASCADE, related_name='sous_categories')

    def __str__(self):
        return f"{self.nom} {self.categorie}"


class Materiel(models.Model):
    ETAT_CHOICES = [
        ('BON', 'Bon'),
        ('CRITIQUE', 'critique'),
        ('INUTILISABLE', 'Inutilisable'),
    ]
    reference = models.CharField(max_length=100, unique=True, null=True, blank=True)
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(CategorieMateriel, on_delete=models.SET_NULL, null=True)
    sous_categorie = models.ForeignKey(SousCategorieMateriel, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(_("Image"), upload_to="materiels",null=True, blank=True)
    eglise = models.ForeignKey(Eglise, on_delete=models.CASCADE, related_name='materiels')
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='BON')
    description = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.reference}"

    def get_etat_css_class(self):
        if self.etat == 'BON':
            return 'bg-green-200 text-green-700'
        elif self.etat == 'CRITIQUE':
            return 'bg-orange-300 text-orange-800'
        elif self.etat == 'INUTILISABLE':
            return 'bg-red-200 text-red-700'
        return ''
