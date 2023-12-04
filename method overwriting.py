class vechicle:
    def __init__(self,name):
        self.name=name
    def getdetails(self):
        print("name: ",self.n)
class bus:
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def getdetails(self):
        print("model: ",self.model)
        print("color: ",self.color)
b1=bus("vovel","red")
b1.getdetails()