str = "Not Class Member"
class GString:
    def __init__(self):
        #지역변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그발생 (가능하면 명시하는 것이 좋다)
        print(str)

g = GString()
g.set("First Message")
g.print()
