from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    cpf = models.CharField(max_length=11,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    solteiro = "solteiro"
    casado = "casado"
    CIVIL_STATE_CHOICES ={
        solteiro: "solteiro",
        casado: "casado",
    }
    civil_state = models.CharField(
        max_length=10,
        choices=CIVIL_STATE_CHOICES,
        default=solteiro,
    )
    
    def __str__(self):
        return f'{self.user.username} Profile'
