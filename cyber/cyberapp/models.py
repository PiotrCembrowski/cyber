from django.db import models

# Create your models here.
class WarriorClass(models.Model):
    name = models.CharField(max_length=64)
    profession = models.CharField(max_length=64)
    level = models.IntegerField(default=1)
    health = models.IntegerField()
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    dexterity = models.IntegerField()
    condition = models.IntegerField()
    move1 = models.CharField(max_length=64)
    move2 = models.CharField(max_length=64)
    move3 = models.CharField(max_length=64)
    move4 = models.CharField(max_length=64)

    def __str__(self):
        return (f'ID: {self.id}, name:{self.name}, profession: {self.profession}, level: {self.level}, health: {self.health}, strength: {self.strength} ' )