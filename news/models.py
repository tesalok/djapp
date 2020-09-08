from django.db import models

class Journalist(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE,related_name="articles")
    description = models.CharField(max_length = 200)
    title = models.CharField(max_length = 120)
    body = models.TextField()
    location = models.CharField(max_length = 120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True)
    updatetd_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return f"{self.author} {self.title}"
    