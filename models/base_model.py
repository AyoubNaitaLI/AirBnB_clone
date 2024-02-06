#!/usr/bin/python3
"""Defines a class BaseModel"""
import models
import uuid
from datetime import datetime


class BaseModel:
	""" This is the BaseModel class
	It defines all the attributes """
	def __init__(self, *args, **kwargs):
		
