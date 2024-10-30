from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)


class LoanModel(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    borrower = models.ForeignKey(UserModel, related_name='loans_taken', on_delete=models.CASCADE)
    lender = models.ForeignKey(UserModel, related_name='loans_given', on_delete=models.CASCADE)
    borrower_phone = models.CharField(max_length=15)
    lender_phone = models.CharField(max_length=15)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Loan {self.amount} from {self.lender} to {self.borrower}"
