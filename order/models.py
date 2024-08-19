from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=20, decimal_places=16)
    lon = models.DecimalField(max_digits=20, decimal_places=16)
    eta = models.CharField(max_length=10)  # Adjust length as needed
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=10,
                                      choices=(
                                              ('card', 'Card'),
                                              ('cash', 'Cash'),
                                              ('paypal', 'Paypal'),
                                          ),
                                      default='card'
                                      )
    status = models.CharField(max_length=10,
                              choices=(
                                      ('waiting', 'Waiting'),
                                      ('processing', 'Processing'),
                                      ('delivered', 'Delivered')
                                  ),
                              default='waiting'
                              )

    def __str__(self):
        return f"{self.user} lon: {self.lon} lat: {self.lat}"


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.product} qty: {self.quantity}"
