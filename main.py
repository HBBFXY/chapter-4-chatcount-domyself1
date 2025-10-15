# main.py
s = input()

letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

for ch in s:
    if ch.isalpha():        # 英文字母
        letter_count += 1
    elif ch.isdigit():      # 数字
        digit_count += 1
    elif ch.isspace():      # 空格
        space_count += 1
    else:                   # 其他字符
        other_count += 1

print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
