from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    CHOICES = (
        ("new", "New"),
        ("process", "Process"),
        ("made", "Made")
    )
    text = models.CharField(verbose_name="Text", max_length=500, null=False, blank=False)
    status = models.CharField(verbose_name="Status", max_length=50, null=False, default="New", choices=CHOICES)
    completion_data = models.TextField(verbose_name="Date of completion", null=True, default=None)
    description = models.TextField(verbose_name="Description", max_length=1500, null=True)
    is_delete = models.BooleanField(verbose_name="Delete", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name="Date of delete", null=True, default=None)

    def __str__(self):
        return f"{self.status} - {self.text}"

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_delete = True
        self.save()

    class Meta:
        verbose_name = "To-do"
        verbose_name_plural = "To-does"
