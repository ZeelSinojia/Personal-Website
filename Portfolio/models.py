from django.db import models

class Project(models.Model):
	project_title = models.CharField(max_length = 50)
	project_decription = models.TextField()

	def __str__(self):
		return self.project_title


class TechnicalSkill(models.Model):
	technical_skill = models.CharField(max_length = 50)

	def __str__(self):
		return self.technical_skill


class PersonalWebsite(models.Model):
	personal_website = models.CharField(max_length = 50)
	personal_website_description = models.TextField()

	def __str__(self):
		return self.personal_website 


class Education(models.Model):
	education = models.CharField(max_length = 50)
	institute = models.CharField(max_length = 50)
	grade = models.DecimalField(max_digits = 3, decimal_places = 2)

	def __str__(self):
		return self.education

	class Meta:
		verbose_name_plural = 'Education'


class Activity(models.Model):
	activity = models.CharField(max_length = 50)
	activity_description = models.TextField()

	def __str__(self):
		return self.activity

	class Meta:
		verbose_name_plural = 'activities'