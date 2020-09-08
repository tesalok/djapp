from django.db import models

# Create your models here.
class JobOffer(models.Model):
    
    company_name = models.CharField(max_length = 150)
    company_email = models.EmailField()
    job_title = models.CharField(max_length = 150)
    job_description = models.CharField(max_length = 150)
    salary = models.FloatField()
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return f"{self.company_name}"