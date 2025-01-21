from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class teams(models.Model):
    TEAMS_CHOICES = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Red o Internet', 'Red o Internet'),
        ('Seguridad', 'Seguridad'),
        ('Otro', 'Otro'),
    ]
    team = models.CharField(verbose_name="Team",max_length=20,null=False,choices=TEAMS_CHOICES)
    
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
  
    STATE_CHOICES = [
        ('NEW', 'Nuevo'),
        ('IN_PROGRESS', 'En progreso'),
        ('RESOLVED', 'Resuelto'),
        ('CLOSED', 'Cerrado'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title = models.CharField(verbose_name="title",max_length=50,null=False,blank=False)
    description = models.TextField(verbose_name="Descriptios",max_length=500)
    client = models.CharField(verbose_name="Client",max_length=30)
    email = models.CharField(verbose_name="Email",max_length=50)
    contact = models.CharField(verbose_name="Phone",max_length=30)
    priority = models.CharField(
        verbose_name="Priority", 
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='LOW'
        )
    date = models.DateTimeField(auto_now_add=True,verbose_name="Date")
    area = models.CharField(verbose_name="Area",max_length=70,null=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tickets_created',null=True, blank=True)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tickets_assigned', null=True, blank=True)
    type_error = models.ForeignKey(teams,on_delete=models.CASCADE,verbose_name="Tipo de error",max_length=30)
    state = models.CharField(
        verbose_name="State",
        max_length=20,  
        choices=STATE_CHOICES,
        default='NEW'
    )

    class Meta:
        db_table = "Tickets"
        verbose_name ="Ticket"
        verbose_name_plural = "Tickets"
    
    