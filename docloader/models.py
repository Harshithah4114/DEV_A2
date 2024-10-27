
from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    createdBy = models.CharField(max_length=255)
    fileUrl = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
