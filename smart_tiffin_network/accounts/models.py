from django.db import models

# Create your models here.
'''
This module defines database models for user roles and user accounts, storing role details, personal information, 
unique contact credentials, passwords, optional OTP values, and role assignments to support authentication and 
authorization workflows.

'''

class UserRole(models.Model):
    '''
    Represents a user role within the system, such as 'customers', 'tiffin_provider', or 'admin'.
    '''
    user_role_id = models.AutoField(primary_key=True)
    user_role_name = models.CharField(max_length=50, unique=True)
    user_role_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_role_name
    
class User(models.Model):
    '''
    Represents a user account in the system, storing personal information, contact details, password, 
    optional OTP for verification, and a reference to the assigned user role.
    '''
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    mobile_otp = models.CharField(max_length=6, blank=True, null=True)
    email_otp = models.CharField(max_length=6, blank=True, null=True)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

    def match_passwords(self):
        '''
        Validates that the password and confirm_password fields match.
        '''
        return self.password == self.confirm_password
    
    def __str__(self):
        return self.full_name