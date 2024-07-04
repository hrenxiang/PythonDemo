def func(input):
    assert isinstance(input, list), 'input must be type of list'
    if len(input) == 1:
        # 处理长度为1的列表
        print(input, 1)
        pass
    elif len(input) == 3:
        # 处理长度为2的列表
        print(input, 2)
        pass
    else:
        # 处理其他长度的列表
        print(input, 3)
        pass


# 测试
func([1, 2, 3])  # 正常执行
func("not a list")  # 抛出 AssertionError
