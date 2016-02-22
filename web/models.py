from django.db import models


class Company(models.Model):
    """会社"""
    name = models.CharField('会社名', max_length=255)
    companycd = models.CharField('会社コード', max_length=255)


    def __str__(self):
        return self.name
