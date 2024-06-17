from django.db import models
from django.db.models import Q

from core.models.category import Category


class ProductManager(models.Manager):
    def search(self, **kwargs):
        queryset = self.get_queryset()
        query_objects = Q()
        ordering_fields = None

        for field, value in kwargs.items():
            if value:
                if field == "ordering":
                    ordering_fields = value.split(",")
                elif field == "category__name" and value.lower() == "all":
                    # Skip adding category filter if "All" is selected
                    continue
                else:
                    query_objects &= Q(**{f"{field}__icontains": value})

        if query_objects:
            queryset = queryset.filter(query_objects).distinct()

        if ordering_fields:
            queryset = queryset.order_by(*ordering_fields)

        return queryset


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    # location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    availability = models.CharField(max_length=50, blank=True)
    # size = models.CharField(max_length=100)
    # features = models.TextField()
    # completion_date = models.DateField()
    # contractor = models.CharField(max_length=255)
    # client = models.CharField(max_length=255)
    status = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
