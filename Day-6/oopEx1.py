class Player:                    # to create blueprint and no value (values of object) yet
    def __init__(self):
        print('welcome to Player Class')

    def reg(self, id, name, team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'Id:{self.id}\t Name:{self.name} \tTeam: {self.team}')

#object creation
p1=Player()
p2=Player()
p3=Player()

p1.reg(1, 'MSD', 'India')
p2.reg(2, 'R.Khan', 'Afghanistan')
p3.reg(3, 'Moin Ali', 'Afghanistan')

p1.display()
p2.display()
p3.display()

#----------------------------
# Parameterize Constructor

class Player:                    
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team


    def display(self):
        print(f'Id:{self.id}\t Name:{self.name} \tTeam: {self.team}')


    def __str__(self):                                  #string return to print
        return f'{self.id} {self.name} {self.team}'

#Object Creation
p1=Player(1, 'MSD', 'India')
p2=Player(2, 'R.Khan', 'Afghanistan')
p3=Player(3, 'Moin Ali', 'Afghanistan')

# Displaying first Player Details
p1.display()

print(p1)


