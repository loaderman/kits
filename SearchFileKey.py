keyword = "example"  # 设置要搜索的关键字
file_path = "example.txt"  # 设置文件路径

# 打开文件并读取内容
with open(file_path, 'r') as file:
    content = file.read()

# 检查关键字是否在文件内容中
if keyword in content:
    print(f"The keyword '{keyword}' was found in the file.")
else:
    print(f"The keyword '{keyword}' was not found in the file.")

import json

# 定义list
my_list = [1, 2, 3, 'a', 'b', 'c']

# 将list转换为JSON字符串
json_data = json.dumps(my_list)

# 将JSON字符串保存到文件
with open('my_data.json', 'w') as file:
    file.write(json_data)

with open('my_data.json', 'r') as file:
    data = json.load(file)
    print(data)
    for item in data:
        print(item)