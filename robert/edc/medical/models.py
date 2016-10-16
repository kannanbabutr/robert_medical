from django.db import models
from django.utils import timezone

class StudyMaster(models.Model):
    study_id = models.IntegerField()
    study_name = models.CharField(max_length=100)
    study_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#Todo: Study ID need to be linked
class FormMaster(models.Model):
	form_id = models.IntegerField()
	study_id = models.IntegerField()
	form_name = models.CharField(max_length=500)
	form_description = models.TextField()
	log_form = models.CharField(max_length=500)
	globl_library = models.CharField(max_length=10)
	globl_name = models.CharField(max_length=500)
	sdv = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

#Todo: Study ID need to be linked, global library should be boolean
class CodeListMaster(models.Model):
	row_id = models.IntegerField()
	study_id = models.IntegerField()
	code_list_name = models.CharField(max_length=500)
	code_list_description = models.TextField()
	code_list_table_name = models.CharField(max_length=200)
	code_global_library = models.CharField(max_length=10)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


class CodeListCodeName(models.Model):
	row_id = models.IntegerField()
	code_name = models.CharField(max_length=100)
	decode_name = models.CharField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


#Todo: Study ID,site Id need to be linked, global library should be boolean
#Clarification - why in study master Study id is in integer but here it's character
class SdvStatusForAllStudy(models.Model):
	row_id = models.IntegerField()
	study_id = models.IntegerField()
	site_id = models.IntegerField()
	site_cluster_id = models.IntegerField()
	visit_id = models.CharField(max_length=200)
	patient_id = models.CharField(max_length=200)
	form_name = models.CharField(max_length=250)
	log_form = models.CharField(max_length=250)
	column_number = models.IntegerField()
	sdv_complete = models.CharField(max_length=1)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


#Clarification: How this field need to be mapped? It's bit difficult to handle..
class ReasonForChange(models.Model):
	reason_for_change = models.CharField(max_length=1000)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)











