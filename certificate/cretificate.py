

class certificategenerator:
  def __init__(self,name,course,all_assignment,all_class):
    self.name=name
    self.course=course
    self.all_assignment=all_assignment
    self.all_class=all_class
    
  
  
  def generatecertificate(self):
    if self.all_assignment.lower()=='yes'and self.all_class.lower()=='yes':
      dicts={'name':self.name,'course':self.course,'certificate':f"you certificate for {self.course} generated"}
      return dicts
    else:
      massage="Please complete all class and assignment"
      return massage
      