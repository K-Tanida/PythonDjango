from django.db import models
from DBAccess import dbaccess

class M_USER(models.Model):
    user_id = models.AutoField(
        primary_key=True,
        verbose_name='ユーザーID'
    )
    user_name = models.CharField(
        max_length=32,
        verbose_name='ユーザー名'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='有効'
    )

    class Meta:
        db_table = 'm_user'
