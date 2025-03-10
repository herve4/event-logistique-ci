from django.db.models.signals import pre_save
from django.dispatch import receiver

import uuid

from accounts.models.user import Materiel


@receiver(pre_save, sender=Materiel)
def generate_reference_number(sender, instance, **kwargs):
    if not instance.reference:
        # Générer un numéro de référence unique
        # Vous pouvez personnaliser cette logique en fonction de vos besoins
        instance.reference = f"REF-{uuid.uuid4().hex[:8].upper()}"
