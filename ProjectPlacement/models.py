'''
Created on 28-Jul-2016

@author: prateek
'''

# from __future__ import unicode_literals
# 
# from django.db import models
# 
# class CostOutputJuly(models.Model):
#     date = models.DateField()
#     project_id = models.IntegerField()
#     cost = models.CharField(max_length=20)
#     lead_ad = models.IntegerField()
#     projectopencount = models.IntegerField(db_column='ProjectOpenCount')  # Field name made lowercase.
#     projectviewcount = models.IntegerField(db_column='ProjectViewCount')  # Field name made lowercase.
#     clientid = models.CharField(db_column='ClientId', max_length=255)  # Field name made lowercase.
#     device_name = models.CharField(max_length=10)
# 
#     class Meta:
#         managed = False
#         db_table = 'cost_output_july'