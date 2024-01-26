import random as r
class Password:
    def __init__(self):
        self.password=""
        self.choice=0

    def basic(self):
        self.len=int(input("enter the length of password:"))
        if(self.len>=4):
            self.store=self.len//2
            for i in range(1,self.len+1):
                if(len(self.password)< (self.store)):
                    self.password+=chr(r.randint(ord('a'),ord('z')))
                else:
                    self.password+=str(r.randint(1,9))
            print("the generated basic password is:",self.password)
            self.password=""
        else:
            print("length of password should be >=4!!")


    def strong(self):
        self.len1=int(input("enter the length of password:"))
        if(self.len>=4):
            for i in range(1,self.len1+1):
                if(len(self.password)<(self.len-3)):
                    self.password+=chr(r.randint(ord('a'),ord('z')))
                elif(len(self.password)==(self.len1-2)):
                    self.password+=chr(r.randint(ord('#'),ord('&')))
                else:
                    self.password+=str(r.randint(1,9))
            print("the generated strong password is:",self.password)
            self.password=""
        else:
            print("length of password should be >= 4!!")

    def complex(self):
        self.len2=int(input("enter the length of password:"))
        if(self.len2>=4):
            for i in range(1,self.len2+1):
                if(len(self.password)<(self.len2-4)):
                        self.password+=chr(r.randint(ord('A'),ord('Z')))
                elif(len(self.password)==(self.len2-4)):
                        self.password+=chr(r.randint(ord('a'),ord('z')))
                elif(len(self.password)==(self.len2-2)):
                        self.password+=chr(r.randint(ord('#'),ord('&')))
                else:
                        self.password+=str(r.randint(1,9))
            print("the generated complex password is:",self.password)
            self.password=""
        else:
             print("length of password should be >=4!!")


    def menu(self):
          while True:
               print("\n1.basic\n2.strong\n3.complex password\n4.exit")
               self.choice=int(input("Enter your choice:"))

               match(self.choice):
                    case 1:
                         self.basic()

                    case 2:
                         self.strong()

                    case 3:
                         self.complex()

                    case 4:
                        print("program has terminated successfully!!!!")
                        break

                    case _:
                         print("invalid syntax please enter correct values")

p=Password()
#p.basic()  
#p.strong()
#p.complex()
p.menu()

            

