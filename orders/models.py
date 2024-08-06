from django.db import models
from django.utils.translation import gettext_lazy as _


class Card(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='cards')
    card_number = models.CharField(_('Card number'), max_length=16)
    card_name = models.CharField(_('card name'), max_length=120)
    expiry_date = models.DateField(_('Expiration date'))
    cvv = models.CharField(_('CVV'), max_length=3)

    def __str__(self):
        return f"{self.user.id} | card number {self.card_number}"


class CartItem(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(_('quantity'))
    subtotal = models.FloatField(_('subtotal'))

    def __str__(self):
        return f"User id:{self.user.id}  | Product : {self.product.name}"


class Discount(models.Model):
    code = models.CharField(_('code'), max_length=60)
    max_limit_price = models.FloatField(_('max limit price'))
    percentage = models.FloatField(_('Percentage'))
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))
    max_limit = models.IntegerField(_('max limits'))

    def __str__(self):
        return f"{self.code}"


class Branch(models.Model):
    name = models.CharField(_('name'), max_length=120)
    region = models.ForeignKey('common.Region', on_delete=models.CASCADE, related_name='branches')
    zip_code = models.CharField(_('zip_code'), max_length=10)
    street = models.CharField(_('street'), max_length=120)
    address = models.TextField(_('address'))
    longitude = models.FloatField(_('longitude'))
    latitude = models.FloatField(_('latitude'))

    def __str__(self):
        return f"Name {self.name} | Region {self.region.name}"


class DeliveryTariff(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='delivery_tariffs')
    price = models.FloatField(_('price'))
    high = models.FloatField(_('high'))
    width = models.FloatField(_('width'))
    weight = models.FloatField(_('weight'))
    regions = models.ManyToManyField('common.Region', related_name='delivery_tariffs')
    delivery_time = models.TimeField(_('delivery time'))

    def __str__(self):
        return f"Branch {self.branch.name} | Price {self.price}"


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        CREATED = "created", _("Created")
        IN_PROGRESS = "in_progress", _("In progress")
        DELIVERED = "delivered", _("Delivered")
        CANCELLED = "cancelled", _("Cancelled")
        FINISHED = "finished", _("Finished")

    class PaymentStatus(models.TextChoices):
        CREATED = "created", _("Created")
        PENDING = "pending", _("Pending")
        PAID = "paid", _("Paid")
        CANCELLED = "cancelled", _("Cancelled")

    class PaymentMethod(models.TextChoices):
        CASH = "cash", _("Cash")
        PAYME = "payme", _("Payme")
        CLICK = "click", _("Click")

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(_("Status"), max_length=60, choices=OrderStatus.choices, default=OrderStatus.CREATED)
    items = models.ManyToManyField(CartItem, related_name="orders")
    total_price = models.FloatField(_('Total Price'))
    address = models.ForeignKey("accounts.UserAddress", on_delete=models.CASCADE, related_name="orders")
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    payment_status = models.CharField(_("Payment Status"), max_length=60, choices=PaymentStatus.choices, null=True,
                                      blank=True)
