from django.db import models


class Entry(models.Model):
    fr = models.CharField(max_length=200)
    de = models.CharField(max_length=200)
    ru = models.CharField(max_length=200)
    ro = models.CharField(max_length=200)
    confidence = models.CharField(max_length=50, choices=(
            ("Sure", "sure"),
            ("Maybe", "maybe"),
            ("Junk", "junk")
        )
    )
