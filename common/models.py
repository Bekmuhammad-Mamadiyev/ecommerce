from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator, URLValidator, RegexValidator

from common.utils import instagram_story_validator


class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "image", _("Image")
        VIDEO = "video", _("Video")
        MUSIC = "music", _("Music")
        FILE = "file", _("File")

    file = models.FileField(_('File'), upload_to="media/files", validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'png', 'jpeg', 'gif', 'mp4', 'mp3', 'wav', 'avi', 'doc', 'pdf'])])
    type = models.CharField(_('Type'), max_length=60, choices=MediaType.choices)

    def __str__(self):
        return f"{self.id} - {self.file.name}"

    def clean(self):
        if self.type == self.MediaType.IMAGE and not self.file.name.endswith(('.jpg', '.png', '.jpeg', '.gif')):
            raise ValidationError(_('Invalid image file format. Only jpg, png, jpeg, and gif are allowed.'))
        elif self.type == self.MediaType.VIDEO and not self.file.name.endswith(('.mp4', '.avi')):
            raise ValidationError(_('Invalid video file format. Only mp4 and avi are allowed.'))
        elif self.type == self.MediaType.MUSIC and not self.file.name.endswith(('.mp3', '.wav')):
            raise ValidationError(_('Invalid music file format. Only mp3 and wav are allowed.'))
        elif self.type == self.MediaType.FILE and not self.file.name.endswith(('.doc', '.pdf')):
            raise ValidationError(_('Invalid file file format. Only doc and pdf are allowed.'))
        else:
            return ValidationError('File type is not supported')

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Medias")


class Settings(models.Model):
    home_image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    home_title = models.CharField(_('Title'), max_length=120)
    home_subtitle = models.CharField(_('Subtitle'), max_length=120)

    def __str__(self):
        return f"{self.id} - {self.home_title}"

    class Meta:
        verbose_name = _("Settings")
        verbose_name_plural = _("Settings")


class Country(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    code = models.CharField(_('Code'), max_length=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


class Region(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class OurInstagramStory(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='instagram_stories')
    story_link = models.URLField(_('Story Link'), validators=[instagram_story_validator])

    def __str__(self):
        return f"{self.id} - {self.story_link}"

    class Meta:
        verbose_name = _("Instagram Story")
        verbose_name_plural = _("Instagram Stories")


class CustomerFeedback(models.Model):
    description = models.TextField(_('Review'), )
    rank = models.IntegerField()
    customer_name = models.CharField(_('Customer Name'), max_length=80)
    customer_position = models.CharField(_('Customer Position'), max_length=60)
    customer_image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, )

    def __str__(self):
        return f"{self.id} - {self.customer_name}"

    class Meta:
        verbose_name = _("Customer Feedback")
        verbose_name_plural = _("Customer Feedbacks")
