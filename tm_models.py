from django.db import models

class Members(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	mem_date = models.DateTimeField('member since')
	mem_id = models.CharField(max_length=30, primary_key=True)
	nickname = models.CharField(max_length=30)
	def __unicode__(self):
		return self.first_name + " " + self.last_name
		# should these all be separate?

class Roles(models.Model):
	meeting_date = models.DateTimeField('Meeting Date')
	thought_of_day = models.ForiegnKey(Members)
	ah_counter = models.ForiegnKey(Members)
	grammarian = models.ForiegnKey(Members)
	timer = models.ForiegnKey(Members)
	gen_eval = models.ForiegnKey(Members)
	speech1 = mmodels.ForiegnKey(Members)
	speech2 = mmodels.ForiegnKey(Members)
	speech3 = models.ForiegnKey(Members)
	speech4 = mmodels.ForiegnKey(Members)
	table_topics = models.ForiegnKey(Members)
	eval1 = models.ForiegnKey(Members)
	eval2 = models.ForiegnKey(Members)
	eval3 = models.ForiegnKey(Members)
	eval4 = models.ForiegnKey(Members)
	attendee1 = models.ForiegnKey(Members)
	attendee2 = models.ForiegnKey(Members)
	attendee3 = models.ForiegnKey(Members)
	attendee4 = mmodels.ForiegnKey(Members)
	attendee5 = models.ForiegnKey(Members)
	attendee6 = models.ForiegnKey(Members)
	attendee7 = models.ForiegnKey(Members)
	attendee8 = models.ForiegnKey(Members)
	attendee9 = models.ForiegnKey(Members)
	attendee10 = models.ForiegnKey(Members)

class Speeches(models.Model):
	mem_id = models.ForiegnKey(Members)
	speech_number = models.IntegerField()
	speech_title = models.CharField(max_length=128)

