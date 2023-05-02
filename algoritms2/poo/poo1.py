class Point:
    def setx(self, coordx):

        self.x = coordx

    def sety(self, coordy):

        self.y = coordy
    
    def get(self):
        return (self.x, self.y)
        
    def move(self, dx, dy):

        self.x += dx
        self.y += dy

        babyoda = Point()
        babyoda.setx(3)
        babyoda.sety(4)
        babyoda.get()
        (3, 4)

        cat = Point()
        cat.setx(5)
        cat.sety(-2)





