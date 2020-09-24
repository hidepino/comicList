from django.db import models

# Create your models here.

class Comic(models.Model):
  """漫画"""
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  main_title = models.CharField(max_length=255)
  home_link = models.CharField(max_length=255)
  update_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.main_title
