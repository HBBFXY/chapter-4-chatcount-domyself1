# 获取用户输入的一行字符
input_str = input()

# 初始化各类字符的计数器
letter_count = 0  # 英文字符（字母）计数器
digit_count = 0   # 数字计数器
space_count = 0   # 空格计数器
other_count = 0   # 其他字符计数器

# 遍历输入的每个字符，判断类型并计数
for char in input_str:
    if char.isalpha():  # 判断是否为英文字符（字母）
        letter_count += 1
    elif char.isdigit():  # 判断是否为数字
        digit_count += 1
    elif char.isspace():  # 判断是否为空格
        space_count += 1
    else:  # 不属于以上三类的为“其他字符”
        other_count += 1

# 按要求格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
