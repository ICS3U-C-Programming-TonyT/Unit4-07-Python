#!/usr/bin/env python3
# Created By: Tony Tran
# Date: November. 20, 2023
# This is program will print from 1000 to 2000 and will print every 5 digits.


def main():
    for count in range(1000, 2005):
        if count % 5 == 0:
            print(count)


if __name__ == "__main__":
    main()
