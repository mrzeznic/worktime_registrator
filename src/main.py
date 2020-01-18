

class time_register:
    count = 0
    def __init__(self,date,proj,task):
        self.date = date
        self.proj = proj
        self.task = task
        time_register.count += 1
