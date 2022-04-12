from django.db import models

# Create your models here.
class person_tb(models.Model):
	"""docstring for person"""
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	Number = models.CharField(max_length=200)



class cust_tb(models.Model):
	"""docstring for person"""
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	Number = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)


class image_tb(models.Model):
	"""docstring for ClassName"""
	image=models.ImageField(upload_to='picture')
	pic=models.ImageField(upload_to='picture')


class fav_tb(models.Model):
	favactor_title =models.CharField(max_length=200)
	userid =models.ForeignKey(cust_tb, on_delete=models.CASCADE)	


class luck_tb(models.Model):
	luckyno_title =models.CharField(max_length=200)
	userid=models.ForeignKey(cust_tb, on_delete=models.CASCADE)
