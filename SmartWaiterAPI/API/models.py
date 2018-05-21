from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Order(models.Model):
    tablenumber = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    datetime = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Orders"

class Menu(models.Model):
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    price = models.DecimalField(validators=[MinValueValidator(0.01)], decimal_places=2, max_digits=3)
    allergy = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Menu items"

class OrderLine(models.Model):
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    menuitem = models.ForeignKey(Menu, on_delete=models.CASCADE)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderlines_relation')

    class Meta:
        verbose_name_plural = "Order lines"

class GoesWellWith(models.Model):
    menuitem1 = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="Primary item+")
    menuitem2 = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="Second item+")

    class Meta:
        verbose_name_plural = "Matches"
