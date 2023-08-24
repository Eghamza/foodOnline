from django.core.exceptions import ValidationError
import os

def allow_only_image_validators(value):
    #get the extansions of the image
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext in valid_extensions:
        raise ValidationError(" unsupported image extension. " + str(valid_extensions))