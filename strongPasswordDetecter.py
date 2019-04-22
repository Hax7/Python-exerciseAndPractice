import re
import sys

# ase for strong passwords
length_regex = re.compile(r'''(
    .{8,} # 8 charachters long
    )''', re.VERBOSE)
capital_regex = re.compile(r'[A-Z]')
digit_regex = re.compile(r'\d')


def detect(password):
    if length_regex.search(password):
        if capital_regex.search(password):
            if digit_regex.search(password):
                print("Its Good!")
    else:
        print("Password should be 8 letters length and have at least\
one capital letter and a digit")


def main():
    detect(sys.argv[1])


if __name__ == "__main__":
    main()
