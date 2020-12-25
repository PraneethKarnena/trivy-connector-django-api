from uuid import uuid4

from django.contrib.postgres.fields import JSONField
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class ScanResult(BaseModel):
    target = models.CharField(max_length=255)
    result = JSONField(null=True, blank=True)

    SUCCESS = 'SCS'
    PENDING = 'PEN'
    FAILED = 'FLD'
    SCAN_STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (SUCCESS, 'Success'),
        (FAILED, 'Failed'),
    )
    status = models.CharField(max_length=3, choices=SCAN_STATUS_CHOICES, default=PENDING)

    has_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['target']

    def __str__(self):
        return f'{self.id} - {self.target}'