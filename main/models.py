from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stocks = models.IntegerField()
    time = models.DateField(auto_now_add=True)

    @property
    def is_stock_ready(self):
        return self.stocks_intensity >= 1

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5