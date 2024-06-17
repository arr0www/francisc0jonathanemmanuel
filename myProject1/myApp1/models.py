from django.db import models

# Create your models here.
class Notes(models.Model):
    body = models.TextField(max_length=200)
    status = models.IntegerField(default = 1)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __st__(self):
        return self.body[0:20]
    class Meta:
        ordering = ['-updated']