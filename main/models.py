from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stocks = models.IntegerField()

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5