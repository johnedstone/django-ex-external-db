from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Customer(models.Model):
    ''' Typical Oracle schema used by DB team '''
    tcp_address = models.CharField(max_length=100, primary_key=True)
    sid_nm = models.CharField(max_length=30)
    full_nm = models.CharField(max_length=100)
    email_address = models.CharField(max_length=150)
    work_phone_nbr_txt = models.CharField(max_length=50)

    class Meta:
        db_table = settings.DB_TABLE_NAME
        ordering = ['full_nm']

    def __unicode__(self):
        return self.tcp_address

    def __str__(self):
        return self.tcp_address
