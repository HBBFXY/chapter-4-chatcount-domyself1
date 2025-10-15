# main.py
def main():
    s = input()

    letters = 0
    digits = 0
    spaces = 0
    others = 0

    for ch in s:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            letters += 1
        elif '0' <= ch <= '9':
            digits += 1
        elif ch == ' ':
            spaces += 1
        else:
            others += 1

    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")


if __name__ == "__main__":
    main()
