from django.db import models


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

    def __str__(self):
        return f"{self.status} - {self.text}"
