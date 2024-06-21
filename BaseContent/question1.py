e = 1
try:
    1 / 0
except ZeroDivisionError as e:
    try:
        pass
    finally:
        del e

e = 1
try:
    1 / 0
except ZeroDivisionError as e:
    pass

# 报错，因为e默认被del了
print(e)
