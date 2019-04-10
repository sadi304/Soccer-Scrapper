from django.db import models


class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_at = models.DateTimeField('date published')
  image_url = models.CharField(max_length=200)
  def __str__(self):
    return self.title

# class Choice(models.Model):
#   question = models.ForeignKey(Question, on_delete=models.CASCADE)
#   choice_text = models.CharField(max_length=200)
#   votes = models.IntegerField(default=0)