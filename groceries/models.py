from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Store(models.Model):
    store_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30, null=True)
    store_notes = models.CharField(max_length=300, null=True, blank=True)
## w/ charFields add blank=True, null=True isn't needed -- w/out blank=True, form would still require input.

    def __str__(self):
        return self.store_name

    def active_items(self):
        return self.item_set.filter(completed=False)

    def active_item_count(self):
        return self.item_set.filter(completed=False).count()


class Item(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User')
    completed = models.BooleanField(default=False)
    item_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(blank=False, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)

    def complete(self):
        self.date_completed = timezone.now()
        self.completed = True
        self.save()
        #instead of having completed as a model boolean field, just check to see if the attribute is true. 

    def __str__(self):
        return self.item_name
