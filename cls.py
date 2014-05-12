import datetime
import time

'''Implement a class that keeps records of hours employees have worked on various projects in office.'''

class EmployeeWorkLog(object):
	emp_dict={}
	emp_list=[]
	pjt_list=[]
	def __init__(self):
		self.name=''
		self.pjt=''
	def addEmployee(self,name):
		if name not in EmployeeWorkLog.emp_list:
			EmployeeWorkLog.emp_list.append(name)
		else:
			print 'name already exist.'
	def displayEmpName(self):
		print EmployeeWorkLog.emp_list
	def addProject(self,pjt):
		if pjt not in EmployeeWorkLog.pjt_list:
			EmployeeWorkLog.pjt_list.append(pjt)
		else:
			print 'name already exist.'
	def displayPjtName(self):
		print EmployeeWorkLog.pjt_list
	def configEmployeeProjects(self,name,list_pjt):
		if(name in EmployeeWorkLog.emp_list and set(list_pjt).issubset(set(EmployeeWorkLog.pjt_list))):
			if( name not in EmployeeWorkLog.emp_dict.keys()):
				EmployeeWorkLog.emp_dict.update({name:list_pjt})
			else:
				for i in list_pjt:
					if(i not in EmployeeWorkLog.emp_dict[name]):
						EmployeeWorkLog.emp_dict[name].extend(list_pjt)
					else:
						print i,'already assigned'
		else:
			print'no such a match'
	def empPjtDetails(self):
		print EmployeeWorkLog.emp_dict
class LogWork(EmployeeWorkLog):
	time_dict={}
	def __init__(self):
		self.stime=0.0
		self.etime=0.0
		EmployeeWorkLog.__init__(self)
	def startLog(self,name,pjt):
		d=datetime.datetime.now()
		h=str(d.hour)
		m=str(d.minute)
		self.stime=float('.'.join([h,m]))
		time.sleep(60)
		
	def endLog(self,name,pjt):
		li=(name,pjt)
		d=datetime.datetime.now()
		l=[]
		h=str(d.hour)
		m=str(d.minute)
		self.etime=float('.'.join([h,m]))
		t=self.etime-self.stime
		l.append(t)
		if(li not in LogWork.time_dict.keys()):
			LogWork.time_dict.update({li:l})
		else:
			LogWork.time_dict[li].append(t)
		
	
	def printSummary(self,name):
		sum=0.0
		print 'employeename:' ,name
		k=LogWork.time_dict.keys()
		v=LogWork.time_dict.values()
		for i in k:
			if(i[0]==name):
				print 'project name:',i[1],
				for j in LogWork.time_dict[i]:
					sum=sum+j
				print ' total time spend',sum
		
	
		
		
