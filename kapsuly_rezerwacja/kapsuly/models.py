from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kapsula(models.Model):
    STANDARD_CHOICES = [("PREMIUM", "premium"), ("RELAX", "relax"), ("BASIC", "basic")]
    POZIOM_CHOICES = [("GORNY", "gorny"), ("DOLNY", "dolny")]
    PLEC_CHOICES = [("FEMALE", "female"), ("MALE", "male"), ("FAMILY", "family")]

    standard = models.CharField(max_length=16, choices=STANDARD_CHOICES, default="PREMIUM")
    poziom = models.CharField(max_length=16, choices=POZIOM_CHOICES, default="DOLNY")
    plec = models.CharField(max_length=16, choices=PLEC_CHOICES, default="FEMALE")

    @property
    def is_reserved(self):
        try:
            rez = self.rezerwacja
        except Rezerwacja.DoesNotExist:
            return False
        else:
            return True

    class Meta:
        verbose_name_plural = "Kapsuly"

    def __str__(self):
        return f"{self.id}_{self.standard}_{self.poziom}_{self.plec}"

class Rezerwacja(models.Model):
    kapsula = models.OneToOneField(Kapsula, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.kapsula}"

    class Meta:
        verbose_name_plural = "Rezerwacje"
        unique_together = ('kapsula', 'user')

class Meta:
    unique_together = ('kapsula.id', 'rezerwacja.id')
