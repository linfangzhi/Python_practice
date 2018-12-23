# 输入整数
try:
    num = int(input('输入整数'))

    result = 8/num

    print(result)

except ZeroDivisionError:
    print('除零错误')
except ValueError:
    print('输入错误')