class Mars_time:
    __time = 0

    def __init__(self, time):
        self.Y = 668.6*88775.245
        self.East = 137.4417
        self.TZone = (self.East/360)*88775.245
        self.M_time = (time+464731200) + self.TZone
        self.__Year = self.M_time//self.Y + 1
        self.__s = ((self.M_time-((self.__Year-1)*self.Y))//88775.245)
        self.__SolY = self.__s+1
        self.__Hour =  (((self.M_time-((self.__Year-1)*self.Y))/88775.245)-self.__s)*24
        if self.__SolY < 61.2:
            self.__Month = 1
        elif self.__SolY<126.6:
            self.__Month=2
        elif self.__SolY<193.3:
            self.__Month=3
        elif self.__SolY<257.8:
            self.__Month=4
        elif self.__SolY<317.5:
            self.__Month=5
        elif self.__SolY<371.9:
            self.__Month=6
        elif self.__SolY<421.6:
            self.__Month=7
        elif self.__SolY<468.5:
            self.__Month=8
        elif self.__SolY<514.6:
            self.__Month=9
        elif self.__SolY<562.0:
            self.__Month=10
        elif self.__SolY<612.9:
            self.__Month=11
        elif self.__SolY<668.6:
            self.__Month=12


    def getYear(self):
        return self.__Year
    def getSol(self):
        return self.__SolY
    def getMonth(self):
        return self.__Month
    def  getHour(self):
        return self.__Hour

