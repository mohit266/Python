import argparse
import sys


def calc(args):

    if args.x == 45 and args.y == 3 and args.o == 'mul':
        ans = 555.0
        return f"{ans}\n"

    elif args.x == 56 and args.y == 9 and args.o == 'add':
        ans = 77.0
        return f"{ans}\n"
    elif args.x == 56 and args.y == 6 and args.o == 'div':
        ans = 4.0
        return f"{ans}\n"

    elif args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number.This is a utility for calculation")
    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number.This is a utility for calculation")
    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

