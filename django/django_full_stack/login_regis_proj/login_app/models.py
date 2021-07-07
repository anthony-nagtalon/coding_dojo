from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def registration_validator(self, postData):
        errors = {}

        if len(postData['first-name']) < 2:
            errors["first-name"] = "First name should be at least 2 characters!"
        if len(postData['last-name']) < 2:
            errors["last-name"] = "Last name should be at least 2 characters!"
        if not self.EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address!"
        if len(postData['pw']) < 8:
            errors["pw-length"] = "Password should be at least 8 characters!"
        if not postData['pw'] == postData['pw-confirm']:
            errors["pw-confirm"] = "Password inputs must match!"
        if len(User.objects.filter(email = postData['email'])) > 0:
            errors["unique-email"] = "There is already an account registered with this email!"
        return errors

    def login_validator(self, postData):
        errors = {}

        if not self.EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address!"
        if len(postData["pw"]) < 8:
            errors["pw"] = "Password is at least 8 characters!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()