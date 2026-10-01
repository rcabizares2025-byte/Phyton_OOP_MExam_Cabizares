class player:      
    
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        
    def add_points(self, points):
        self.score += points
        return self.score
    
ana = player("Ana", 10)
ben = player("Ben",)  

ana.add_points(5)
ben.add_points(7)

print(ana.score)
print(ben.score)