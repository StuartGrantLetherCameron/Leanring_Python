"""argparse is used to output a error for comandline arg not being put in"""
import argparse


def add_ten(num):
    """add ten"""
    return num + 10


def main():
    """creating the argparse"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "num", help="The number you wish to add ten too", type=int)
    args = parser.parse_args()

    result = add_ten(args)
    print("the ", str(args.num), " plus ten is ", str(result))


if __name__ == "__main__":
    main()
