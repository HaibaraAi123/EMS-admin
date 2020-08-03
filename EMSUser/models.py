from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    #已有属性 id password last_login is_superuser
    # username first_name last_name email
    # is_staff is_active date_joined
    GENDER = ((1, '男'), (2, '女'))
    phone = models.CharField(max_length=20,verbose_name='电话号码')
    gender = models.IntegerField(choices=GENDER, default=1)
    info = models.CharField(max_length=100)

    class Meta:
        permissions = (
            ('user_','普通用户'),
            ('management_','管理用户'),


        )