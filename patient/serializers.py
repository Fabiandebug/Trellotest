from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import p_users

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=p_users
        fields=['id','first_name','second_name','email','mobile']