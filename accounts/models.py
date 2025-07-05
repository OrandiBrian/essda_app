from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN', _('Super Admin')
        PASTOR = 'PASTOR', _('Pastor')
        DEPARTMENT_HEAD = 'DEPARTMENT_HEAD', _('Department Head')
        TREASURER = 'TREASURER', _('Treasurer')
        MEMBER = 'MEMBER', _('Member')
        
        
    role = models.CharField(
        max_length=20,
        choices = Role.choices,
        default = Role.MEMBER
    )
    
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"
    
    @property
    def is_pastor(self):
        return self.role == self.Role.PASTOR
    
    @property
    def is_department_head(self):
        return self.role == self.Role.DEPARTMENT_HEAD
    
    @property
    def is_treasurer(self):
        return self.role == self.Role.TREASURER
    
    @property
    def is_super_admin(self):
        return self.role == self.Role.SUPER_ADMIN