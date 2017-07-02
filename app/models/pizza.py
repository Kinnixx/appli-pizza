from django.db import models


class Pizza(models.Model):
    ingredients = models.ManyToManyField('Ingredient',
                                 blank=True)
    label = models.CharField(max_length=200,
                             null=True,
                             blank=True,
                             default=None)
    taille = models.CharField(max_length=100,
                              null=True,
                              blank=True,
                              default=None)
    prix = models.FloatField(default=0,
                              blank=True,
                              null=True)

    def __str__(self):
        return "{} - {} : {} €".format(self.label, self.taille, self.prix)