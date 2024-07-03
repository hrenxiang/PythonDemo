import objgraph

# 假设有一个列表对象
my_list = [1, 2, 3]

# 生成引用图
objgraph.show_refs([my_list], filename='refs.png')

# 统计并显示最常见的对象类型
objgraph.show_most_common_types(limit=20)