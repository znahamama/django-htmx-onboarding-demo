from django.db import models

class Application(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('employer', 'Employer')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES) 
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self): 
        return self.name 