from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ("done", "-datetime")

    def __str__(self):
        return (
            f"{self.content} ("
            f"datetime: {self.datetime}, "
            f"deadline: {self.deadline}, "
            f"done: {self.done})"
        )

    def get_absolute_url(self):
        return reverse("todo:task-list", args=[str(self.id)])
