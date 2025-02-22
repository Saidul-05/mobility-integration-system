from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ("repair", "Repair Service"),
        ("towing", "Towing Service"),
        ("parts", "Spare Parts"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
