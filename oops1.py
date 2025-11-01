class employee:
    def __init__(self):
        self.id=101
        self.designation="SDE"
        self.salary=50000

    def travel(self,destination):
        print(f"Employee is traveling to {destination}")


sam = employee()#object creation
print("ID:", sam.id)
sam.travel("Chennai")