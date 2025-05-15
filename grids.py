#This code prints 2x2 grid with horizontal and vertical lines
def print_horizontal():
    print('+ - - - - + - - - - +')

def print_vertical():
    for i in range(4):# loop to print vertical lines
        print('|         |         |')

def print_grid():
    print_horizontal()
    print_vertical()
    print_horizontal()
    print_vertical()
    print_horizontal()

print_grid()

# This code prints 8*8 grid with horizontal and vertical lines
def print_horizontal():
    print('+ - - - - - - - - + - - - - - - - - +')

def print_vertical():
    for i in range(8):# loop to print vertical lines
        print('|                 |                 |')

def print_grid():
    print_horizontal()
    print_vertical()
    print_horizontal()
    print_vertical()
    print_horizontal()
    print_vertical()
    print_horizontal()
    print_vertical()

print_grid()   