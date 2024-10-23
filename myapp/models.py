from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    bank_account = models.OneToOneField(
        "BankAccount",
        on_delete=models.CASCADE,
        related_name="person",
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name


class BankAccount(models.Model):
    account_number = models.CharField(max_length=100)
    balance = models.IntegerField()

    def __str__(self):
        return self.account_number
