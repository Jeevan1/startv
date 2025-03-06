from django.db import models
from shortuuidfield import ShortUUIDField

class BaseModel(models.Model):
    idx = ShortUUIDField(unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True