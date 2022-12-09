class Color:

    def __init__(self,r = 0,g = 0,b = 0) -> None:
            self.r = r
            self.g = g
            self.b = b

    def greenText(self,text : str):
        return "\x1B[38;2;0;200;51m"+ text +"\x1b[0m"
    
    def coloredText(self,text : str,color) -> str:
        try:
            r = color.r
            g = color.g
            b = color.b
            return f"\x1B[38;2;{r};{g};{b}m"+ text +"\x1b[0m"
        except:
            return text
            
class Colors:

   green = Color(0,200,51)
   yellow = Color(253,253,150)