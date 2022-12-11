class Colors:
    # a=0
    # b=0
    # c=0
    # def __init__(self,r,g,b) -> None:
    #     self.r = r
    #     self.g = g
    #     self.b = b

    @property
    def green():
        print("Hello World")
        return 1

    def __str__(self) -> str:
        return "Colors"

# print(Colors.green)

def some(col : Colors):
    print(col.a)

# some(Colors.green)
Colors.green
# print(Colors.green)