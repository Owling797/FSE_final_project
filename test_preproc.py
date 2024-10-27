"""Preprocessing test"""
import os
import sys


def main():
    """main loop"""
    if os.path.exists("./test.jpg"):
        print("OK")
    else:
        print("Error preprocessing")
        sys.exit(1)


if __name__ == "__main__":
    main()
