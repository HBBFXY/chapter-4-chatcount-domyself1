input_str = input()

# 初始化四类字符的计数器
letter_count = 0  # 英文字符（字母，含Unicode字母）
digit_count = 0   # 数字字符
space_count = 0   # 空格字符
other_count = 0   # 其他字符

# 遍历每个字符并分类统计
for char in input_str:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

# 严格按格式输出（英文冒号+空格，键名准确）
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
