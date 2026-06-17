from django.db import models
from django.conf import settings


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="tables"
    )
    
    class TableType(models.TextChoices):
        ROUND = "round", "Round"
        SQUARE = "square", "Square"
        RECTANGLE = "rectangle", "Rectangle"
        BAR = "bar", "Bar"

    name = models.CharField(max_length=120)
    seats = models.PositiveIntegerField()

    x = models.FloatField()
    y = models.FloatField()

    is_active = models.BooleanField(default=True)

    table_type = models.CharField(
        max_length=20,
        choices=TableType.choices,
        default=TableType.SQUARE,
    )

    def __str__(self):
        return self.name

class Reservation(models.Model):    

    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    status = models.CharField(
        max_length=20,
        choices=[
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
        ],
        default="confirmed")
    
    reservation_datetime = models.DateTimeField()

    duration_minutes = models.PositiveIntegerField(
        default=120)
    
    table=models.ForeignKey(Table, on_delete=models.CASCADE)
    
    guests_count=models.PositiveIntegerField()
