from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class teams(models.Model):
    team = models.CharField(verbose_name="Team",max_length=20,null=False)
    
    class Meta:
        db_table = "Teams"
        verbose_name ="Team"
        verbose_name_plural = "Teams"
    def __str__(self) -> str :
        return self.team

class profile(models.Model):
    name = models.CharField(verbose_name="Name",max_length=40)
    role = models.CharField(verbose_name="Role",max_length=20)
    id_team = models.ForeignKey(teams, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "Profiles"
        verbose_name ="Profile"
        verbose_name_plural = "Profiles"
    
class tickets(models.Model):
    title = models.CharField(verbose_name="title",max_length=50,null=False,blank=False)
    description = models.TextField(verbose_name="Descriptios",max_length=500)
    type_error = models.CharField(verbose_name="Type Error",max_length=20)
    client = models.CharField(verbose_name="Client",max_length=30)
    email = models.CharField(verbose_name="Email",max_length=50)
    contact = models.CharField(verbose_name="Phone",max_length=30)
    state = models.CharField(verbose_name="State",max_length=30)
    id_user = models.ForeignKey(profile,on_delete=models.CASCADE)
    id_grupo = models.ForeignKey(teams,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Tickets"
        verbose_name ="Ticket"
        verbose_name_plural = "Tickets"
    
    