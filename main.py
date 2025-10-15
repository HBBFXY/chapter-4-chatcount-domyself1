# main.py
import sys
import string

def main():
    try:
        s = input()
    except EOFError:
        s = ""

    ascii_letters = set(string.ascii_letters)
    digits = set(string.digits)

    letter_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    for ch in s:
        if ch in ascii_letters:
            letter_count += 1
        elif ch in digits:
            digit_count += 1
        elif ch == ' ':
            space_count += 1
        else:
            other_count += 1

    print(f"英文字符: {letter_count}")
    print(f"数字: {digit_count}")
    print(f"空格: {space_count}")
    print(f"其他字符: {other_count}")

if __name__ == "__main__":
    main()

