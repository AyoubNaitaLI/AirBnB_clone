#!/usr/bin/python3
"""this is the review module 
defines one class review()"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""this is a review about the house or the palce"""
	text= ""
	palce_id= ""
	user_id= ""

