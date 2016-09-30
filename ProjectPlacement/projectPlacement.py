import numpy as np
import MySQLdb
from collections import Counter
import datetime
import operator

class projectPlacement:
	def __init__(self): 
# 		self.CPLdb=MySQLdb.connect(host="52.35.25.23" , port = 3306, user = "ITadmin",passwd = "ITadmin" ,db ="CPL") 52.66.172.140
		self.zeroLeadPenelty = 1500
		self.openViewRatioWeight = 100
		self.openViewFactor = 3

	def getProjectScore(self):
		self.CPLdb=MySQLdb.connect(host="52.66.177.232" , port = 3306, user = "ITadmin",passwd = "ITadmin" ,db ="CPL")
		cursor=self.CPLdb.cursor()
		currDate = datetime.date.today()
		prev3Month =  currDate - datetime.timedelta(days=90)
		startDate = "2016-04-01"
		endDate = "2016-06-30"
		query = "select project_id,sum(cost),sum(lead_ad),sum(ProjectOpenCount),sum(ProjectViewCount) from cost_output_july where date between \""+ str(startDate) + "\" and \"" +str(endDate)+"\" and device_name=\"computers\" group by project_id"
		cursor.execute(query)
		projectCostLeadList=[]
		for rows in cursor.fetchall():
			projectCostLeadList.append(rows)

		scoreDict = {}
		for projctInfo in projectCostLeadList:
			openViewRatio = min(1,float(projctInfo[3]) / float(projctInfo[4]+1))
			#Lead = 0
			if(projctInfo[2]  == 0):
				score = projctInfo[1] + self.zeroLeadPenelty + (1 - (openViewRatio)*self.openViewFactor)*self.openViewRatioWeight

			else:
				score = float(projctInfo[1])/float(projctInfo[2]) +  (1 - (openViewRatio)*self.openViewFactor)*self.openViewRatioWeight
			scoreDict[int(projctInfo[0])] = int(score)
		# scoreDict = sorted(scoreDict.items(), key=operator.itemgetter(1))
		self.CPLdb.close()
		return scoreDict

if __name__ == '__main__':
	p = projectPlacement()
	print p.getProjectScore()



