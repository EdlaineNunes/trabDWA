from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField('Nome', max_length=100)
    entryPeriod = models.CharField('Ingresso', max_length=6)
    email = models.EmailField('E-mail', max_length=100)
    note = models.IntegerField('Nota')
    situation = models.CharField('Situação', max_length=10)

    def __str__(self):
        return f'{self.name} {self.entryPeriod}'
