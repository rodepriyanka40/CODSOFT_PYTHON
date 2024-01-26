#calculator
class calculator:
    def __init__(self):
        self.num1=0
        self.num2=0
        self.choice=0

    def addition(self):
        self.num1=int(input("enter any number:"))
        self.num2=int(input("enter any number:"))
        print("Addition of two numbers are:",self.num1+self.num2)

    def subtraction(self):
        self.num1=int(input("enter any number:"))
        self.num2=int(input("enter any number:"))
        print("subtraction of two numbers are:",self.num1-self.num2)

    def multiplication(self):
        self.num1=int(input("enter any number:"))
        self.num2=int(input("enter any number:"))
        print("multiplication of two numbers are:",self.num1*self.num2)

    def division(self):
        self.num1=int(input("enter any number:"))
        self.num2=int(input("enter any number:"))
        print("division of two numbers are:",self.num1/self.num2)

    def menu(self):
        while (self.choice!=5):
            print("\n1.add\n2.subtract\n3.multiply\n4.divide\n5.exit")
            self.choice=int(input("enter your choice:"))

            match(self.choice):
                case 1:
                    self.addition()
                
                case 2:
                    self.subtraction()
                        
                case 3:
                    self.multiplication()

                case 4:
                    self.division()
            
                case 5:
                    print("you have been exited...")
                    break

                case _:  #default in python
                    print("invalid choice ! please enter invalid choice") 

c=calculator()
c.menu()           









        