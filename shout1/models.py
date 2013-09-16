from django.db import models

class User (models.Model):
	#Here we can add any other user profile attributes, this is just to start
	username = models.Charfield(max_length=15)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=32)
	join_date = models.DateTimeField(auto_now_add=True)
	
	
class Message (models.Model):
	#each message belongs to a User and contains the contents of the message
	#followed by its location, radius and time stamp
	username = models.ForeignKey('User')
	content = models.CharField(max_length=150)
	
	geolat = models.DecimalField(max_digits=8, decimal_places=5)
	geolon = models.DecimalField(max_digits=8, decimal_places=5)
	radius = models.IntegerField(max_digits=2)
	
	time_stamp=models.DateTimeField(auto_now_add=True)
	

class Map(models.Model):
	#this will remain a general map for now, but eventually it needs to be
	#calibrated to work with a virtualized projection (mercator?)
	resolution = models.FloatField()
	#how big each location cell is
	messages = models.ManyToManyField('Message')
	#figure out if this is the best field to use ^
	
class Coordinate(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	map = models.ForeignKey('Map')