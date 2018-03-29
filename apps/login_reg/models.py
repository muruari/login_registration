# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
class UsersManager (models.Manager): #UsersManager def should only be validators and return errors this then goes to views.py
    def validator(self,postData):
        EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        errors = {}
        if len(postData['FN']) < 2:
            errors['first_name'] = "Name must be longer than two characters"
        print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        if len(postData['LN']) < 2:
            errors['last_name'] = "Last name must be longer than two characters"
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        if not EMAIL_REGEX.match(postData['EML']):
            errors['email'] = "Email should be in known email format"
        print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
        print len(errors)
        return errors
        print errors
        

  
# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    objects = UsersManager() #bridge that connects Users to UsersManager
    def __repr__(self):
        return "<user object: {} {} >".format(self.full_name, self.email)
