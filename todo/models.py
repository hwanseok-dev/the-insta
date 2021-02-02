from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    join_date = models.DateTimeField()

    class Meta:
        db_table = "todo_owner"


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner,
                               on_delete=models.CASCADE,
                               related_name='owner_todo',
                               default=1)

    def _str_(self):
        return self.title
