# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ShoppingList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ShoppingListItem(models.Model):
    CHECKED = 'checked'
    UNCHECKED = 'unchecked'
    STATUS_CHOICES = (
        (CHECKED, 'Checked'),
        (UNCHECKED, 'Unchecked')
    )
    name = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=UNCHECKED
    )
    shopping_list = models.ForeignKey(
        ShoppingList, 
        on_delete=models.CASCADE,
        related_name="items"
    )

    def __str__(self):
        return self.name
