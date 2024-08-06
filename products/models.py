from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media
from ckeditor.fields import RichTextField
from products.utitls import validate_rating


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    price = models.FloatField(_("Price"), )
    short_description = models.TextField(_("short Description"))
    description = models.TextField(_("Description"))
    quantity = models.IntegerField(_("Quantity"))
    instructions = RichTextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True)
    in_stock = models.BooleanField(_("in stock"), default=True)
    brand = models.CharField(_("Brand"), max_length=255, null=True)
    discount = models.IntegerField(_("Discount"), help_text=_("in percentage"), null=True)

    def __str__(self):
        return f"{self.name}"


class ProductColour(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colours")
    colour = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Product {self.product.id}"


class ProductSize(models.Model):
    value = models.CharField(_('Value'), max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")

    def __str__(self):
        return f"Product {self.product.id} -Size {self.value}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=255)
    review = models.TextField(_("review"))
    rank = models.IntegerField(_("rank"), validators=[validate_rating])
    email = models.EmailField(_("email"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return f"Product: {self.product.id}|User: {self.user.id}"


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlists')
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="wishlists")

    def __str__(self):
        return f"Product: {self.product.id}|User: {self.user.id}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Product: {self.product.id}|Image: {self.image.id}"
