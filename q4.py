import turtle
class Point:

    def __init__(self,x,y):
      self.x=x
      self.y=y
    def __str__(self):
      print(self.x,self.y)
    def draw():
      turtle.goto(self.x,self.y)
      turtle.dot()
    def add(self, another_point):
       #make function to add point 1 and point 2 x value is 100 and y value is 200
       

origin=Point(0,0)
point1=Point(0,100)
point2=Point(100,100)
point3=Point(100,0)

new_point=point1.add(point2)# for this 

    
    

















