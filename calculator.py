class Calculator:
    def __init__(self):
        self.memory = 0
    
    def add(self, num):
        self.memory += num
    
    def subtract(self, num):
        self.memory -= num
    
    def multiply(self, num):
        self.memory *= num
    
    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.memory /= num
    
    def root(self, n):
        self.memory **= (1/n)
    
    def reset(self):
        self.memory = 0
