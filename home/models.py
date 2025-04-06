from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('Deluxe', 'Deluxe'),
        ('Standard', 'Standard'),
        ('Family', 'Family'),
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default='Standard')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return f"{self.name} ({self.room_type})"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return f"{self.name}'s Review"
