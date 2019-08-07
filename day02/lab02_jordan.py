## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour
    def __str__(self):
        return "It is %d:%d" % (self.hour, self.minutes)
    def __add__(self,minutes):
        self.minutes = int(self.minutes) + minutes
        if self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hour = int(self.hour) + 1
    def __sub__(self,minutes):
        self.minutes = int(self.minutes) - minutes
        if self.minutes < 0:
            self.minutes = self.minutes + 60
            self.hour = int(self.hour) - 1

    ## Are two times equal?
    def __eq__(self, other):

    ## Are two times not equal?
    def __ne__(self, other):
