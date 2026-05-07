class Stacks():
    def __init__(self):
        self.size = 0
        self.data = []

    def add(self, data):
        self.data.append(data)
        self.size += 1

    def pop(self):
        try:  
            self.data.pop(-1)
            self.size -= 1
        except IndexError:
            print("Its an empty list")

    def top(self):
        return(self.data[-1])
    
    def isEmpty(self):
        return False if self.size > 0 else True