from django.db import models
from django.utils import timezone

class StudyMaster(models.Model):
    study_id = models.IntegerField()
    study_name = models.CharField(max_length=100)
    study_description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


class FormMaster(models.Model):
	form_id = models.IntegerField()
	study_id = models.IntegerField()
	form_name = models.CharField(max_length=500)
	form_description = models.TextField()
	log_form = models.CharField(max_length=500)
	globl_library = models.CharField(max_length=10)
	globl_name = models.CharField(max_length=500)
	sdv = models.CharField(max_length=50)

