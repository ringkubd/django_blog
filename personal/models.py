from django.db import models

# Create your models here.
PRIORITY = [
    ("H", "High"),
    ("M","Medium"),
    ("L","Low")
]


class Question(models.Model):
    title = models.CharField(max_length=250)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=50, choices=PRIORITY)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "The Question"
        verbose_name_plural = "Peoples Questions"
