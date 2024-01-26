#strip=does not count space and readline=ii used to count lines
class ToDoList:
    def __init__(self):
        self.task=[] 
    def addTask(self):
        self.a=int(input("enter how many task you want to add:"))
        for i in range(1,self.a+1):
            self.li=str(input("enter your task:"))
            self.task.append(self.li)
            with open("task.txt",'a')as file:
                file.write(self.li+"\n")
        print("task added successfully")
    def displayTask(self):
        print("task present are:")
        self.file=open("task.txt",'r')
        self.c=0
        while True:
            self.line=self.file.readline().strip()
            self.c+=1 
            if not self.line:
                break
            print(self.c,".",self.line)
    def updateTask(self):
        print("your scheduled task:")
        for a in range(0,len(self.task)):
            print(a+1,".",self.task[a])
        self.index1=int(input("which task number you want to update:"))
        if self.index1>len(self.task)or self.index1<0:
            print("please enter the valid index:")
        else:
            self.newTask=str(input("enter your new task:"))                
            self.oldTask=self.task[self.index1-1]
            self.task.remove(self.oldTask)
            self.task.insert(self.index1-1,self.newTask)
            print("your task has been updated")

    def delTask(self):
        for a in range(0,len(self.task)):
            print(a+1,".",self.task[a])
        self.delIndex=int(input("which task you want to delete:"))
        if self.delIndex>len(self.task)or self.delIndex<0:
            print("please enter the valid index:")  
        else:
            self.oldTask=self.task[self.delIndex-1]
            self.task.remove(self.oldTask)
            print("your task has been deleted successfully")

    def fetchData(self):
        fetch=open("task.txt",'r')
        while True:
            self.line=fetch.readline().strip()
            if not self.line:
                break
            self.task.append(self.line)

    def saveTask(self):
        file1=open("task.txt",'w')
        file1.write("")
        file1.close()
        file=open("task.txt",'a')
        for a in range(0,len(self.task)):
            file.write(self.task[a])
            file.write("\n")
        print("your task has been saved successfully")
        file.close()

    def menu(self):
        while (self.choice!=5):
            print("-----TO DO LIST-----")
            print("\n1.Add task\n2.show task\n3.update task\n4.delete task\n5.save task")
            self.choice=int(input("enter the choice"))
            
            match(self.choice):
                case 1:
                    self.addTask()

                case 2:
                    self.displayTask()

                case 3:
                    self.updateTask()

                case 4: 
                    self.delTask()

                case 5:
                    self.saveTask()

t=ToDoList()
t.addTask()        
t.displayTask()
t.updateTask()
t.delTask()
t.saveTask()



