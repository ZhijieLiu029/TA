class Students:
    pass


class SRecords:
    pass

class Student(object):
    def __init__(self,stdid,name,stdclass,sex):
        self.name = name
        self.stdid = stdid
        self.stdclass = stdclass
        self.sex = sex
    def print_self(self):
        print('%s,%s,%s'%(self.stdid,self.name,self.stdclass))