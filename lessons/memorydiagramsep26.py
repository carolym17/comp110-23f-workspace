"""Practice Memory Diagrams in class sep 26!"""

# Memory Diagram 1
xs: str = "123"
ys: str = "45"

x_idx: int = 0
while x_idx < len(xs):
    y_idx: int = 0
    while y_idx < len(ys):
        print(f"({xs[x_idx]},{ys[y_idx]})")
        y_idx = y_idx + 1
    x_idx = x_idx + 1


# Memory Diagram 2
def main():
    """Main code of program"""
    y: float = double(2.0)
    print(halve(y))

def halve(x: float) -> float: 
    """Returns half the value of x"""
    print(f"halve{x})")
    return x / 2.0

def double(x: float) -> float: 
    """Double a value"""
    print(f"double({x})")
    return x * 2.0 

main()
