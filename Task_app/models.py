from django.db import models

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=255,blank=False,null=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)


    class Meta:
        verbose_name = ("task")
        verbose_name_plural = ("tasks")

    def __str__(self):
        return self.titulo

