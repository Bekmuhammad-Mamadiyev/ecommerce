from django.core.exceptions import ValidationError
import re

def instagram_story_validator(value):
    instagram_story_regex = r'^https:\/\/(www\.)?instagram\.com\/stories\/[A-Za-z0-9._-]+\/\d+\/?$'
    if not re.match(instagram_story_regex, value):
        raise ValidationError(
            "Invalid Instagram story URL. It must be in the format: https://www.instagram.com/stories/<username>/<story_id>/"
        )
