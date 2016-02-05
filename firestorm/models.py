# -*- coding: utf-8 -*-
# pylint: disable=no-member, no-init, invalid-name
"""This file contains the custom models and managers used within the firestorm
project."""
from __future__ import unicode_literals
import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email):
        """Creates and saves a User with the given email"""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        #user.set_password('python_utah_north')
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """Creates and saves a superuser with the given email"""
        user = self.create_user(email)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """This is a custom user model

    According to the Django docs, only fields related directly to user
    authentication should exist here.
    """
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        return self.email


class Topic(models.Model):
    """docs"""
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    description = models.TextField()
    DEPTH_BEGINNER = 'Beginner'
    DEPTH_INTERMEDIATE = 'Intermediate'
    DEPTH_EXPERT = 'Expert'
    DEPTH_CHOICES = (
        ('B', DEPTH_BEGINNER),
        ('I', DEPTH_INTERMEDIATE),
        ('E', DEPTH_EXPERT),
    )
    depth = models.CharField(max_length=1, choices=DEPTH_CHOICES)
    suggested_by = models.ForeignKey('User')
    suggested_date = models.DateField(default=datetime.date.today)
    user_prefs = models.ManyToManyField(User,
                                        related_name='topic_prefs',
                                        through='UserPreferences')

    def __unicode__(self):
        """useful for debugging..  actually see what the instance is"""
        return self.subject


class UserPreferences(models.Model):
    """UserPreferences is a "through" table for the topic/user combination.
    This table has additional fields called users_topic_interest_level which
    contains how interested a user is in receiving this information as a
    presentation.
    The table also has a field called users_current_skill_level which documents
    how good this person might be at presenting on this topic.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    users_topic_interest_level = models.PositiveSmallIntegerField()
    users_current_skill_level = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return "{}'s preferences in {}".format(self.user, self.topic)


class Presentation(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic)
    presenter = models.ForeignKey(User)
    when = models.DateField()
    feedback = models.ManyToManyField(
        User, related_name='presentation_feedback', through='Feedback')


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    presentation = models.ForeignKey(Presentation,
                                     related_name='feedback_presentation')
    received_by = models.ForeignKey(User)
    prep_level = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(9),
            MinValueValidator(1)
        ]
    )
    comments = models.TextField()
