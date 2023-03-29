from django.db import models

# Create your models here.


class StudentDetails(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female")
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)

    def __str__(self):
        return self.name
