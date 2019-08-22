class car:

    def __init__(self, company, color):

        self.color=color
        self.company=company
    def display(self):
        print("this is",self.color,self.company)

object=car('Ferrari','Red')
print(object.company)
print(object.color)
print(object.display())
