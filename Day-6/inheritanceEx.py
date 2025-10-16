# Upper / Base / parent Class
class Emp:
    def reg(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(f'Id: ',{self.id})
        print(f'Name: ',{self.name})

# Inherited Class
class Dev(Emp):
    def welcome(self):
        print('Welcome to developer')


d=Dev()
d.welcome()
d.reg(1, 'sam')
d.display()

e=Emp()
e.reg(102, 'Raj')
e.display()