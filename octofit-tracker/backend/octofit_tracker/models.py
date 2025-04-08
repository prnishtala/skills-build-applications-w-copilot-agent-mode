# models.py
from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.type} by {self.user}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team}: {self.points} points"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
