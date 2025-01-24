from django import template
import base64
from io import BytesIO
from PIL import Image

register = template.Library()

@register.filter
def base64encode(value):
    """Convert an image or any other binary content to base64."""
    if isinstance(value, Image.Image):
        # Save the image to a BytesIO object and encode it in base64
        buffered = BytesIO()
        value.save(buffered, format="PNG")  # Save as PNG
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    return value