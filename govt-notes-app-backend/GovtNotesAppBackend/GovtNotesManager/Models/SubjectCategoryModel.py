import uuid
from django.db import models
from Common import constants as ct

class SubjectCategory(models.Model):
    categoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    categoryName = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "SubjectCategory"
