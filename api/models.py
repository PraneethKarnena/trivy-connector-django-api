from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-created_at']