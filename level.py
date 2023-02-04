class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.array = [[0 for x in range(101)] for y in range(101)]
    
    def describe_level(self):
        print(self.array)