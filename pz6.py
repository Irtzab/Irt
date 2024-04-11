import argparse
def triangle(args):
    for i in range(1, args.n + 1):
        print('   ' * (args.n - i) + ' * ' * (2 * i - 1))

def square(args):
    if args.n>0:
        for i in range (args.n):
            print(args.n*' * ')

def trapezoid(args):
    for i in range(1, args.n+1):
        print('   ' * (args.n - i) + ' * ' * (2 * i))

def hexagon(args):
    for i in range(2 * args.n - 1):
        if i < args.n:
            print('   ' * (args.n - i - 1) + ' * ' * (2 * i + 1))
        else:
            print('   ' * (i - args.n) + ' * ' * (4 * args.n - 2 * i - 1))

parser = argparse.ArgumentParser("Choose a pz6 to run")
subparsers = parser.add_subparsers(title="The programm generates one of 4 figures: triangle, square, trapezoid, hexagon. Please write python pz6.py your_figure size", dest="The programm generates one of 4 figures: triangle, square, trapezoid, hexagon. Please write python pz6.py your_figure size")
# Subparser for triangle
triangle_parser = subparsers.add_parser("triangle", help="Triangle figure")
triangle_parser.add_argument('n', type=int, help='Size your figure')
triangle_parser.set_defaults(func=triangle)
# Subparser for square
square_parser = subparsers.add_parser("square", help="Square figure")
square_parser.add_argument('n', type=int, help='Size your figure')
square_parser.set_defaults(func=square)
# Subparser for trapezoid
trapezoid_parser = subparsers.add_parser("trapezoid", help="Trapezoid figure")
trapezoid_parser.add_argument('n', type=int, help='Size your figure')
trapezoid_parser.set_defaults(func=trapezoid)
# Subparser for hexagon
hexagon_parser = subparsers.add_parser("hexagon", help="Hexagon figure")
hexagon_parser.add_argument('n', type=int, help='Size your figure')
hexagon_parser.set_defaults(func=hexagon)

args = parser.parse_args()
args.func(args)