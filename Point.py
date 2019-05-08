import random
import math
class Point():
    def __init__(self,neastInterval,finishInterval):
        self.be_random(neastInterval,finishInterval)
        self.centroid = -1
        
    def getX(self):
        return self.x
    
    def show(self):
        print("X:",self.x,"Y",self.y)

    def be_random(self,neastInterval,finishInterval):
        self.x= random.uniform(neastInterval, finishInterval)
        self.y= random.uniform(neastInterval, finishInterval)
    
    def distance(self,point):
        return math.sqrt(math.pow(self.x - point.x,2) + math.pow(self.y - point.y,2))
        
    
    def match(self,centroid):
        self.centroid = centroid
        
    def get_match(self):
        return self.centroid
 
