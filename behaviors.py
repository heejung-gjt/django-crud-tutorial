from django.db import models
import time

class Timestampable(models.Model):
  create_at = models.TextField(default=time.time())
  update_at = models.TextField(null=True, blank=True)

  class Meta:
    abstract = True


class Nameable(models.Model):
  name = models.CharField(max_length=32)

  class Meta:
    abstract = True