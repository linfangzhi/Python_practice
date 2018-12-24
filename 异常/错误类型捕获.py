# 输入整数
try:
    num = int(input('输入整数'))

    result = 8/num

    print(result)

except ZeroDivisionError:
    print('除零错误')
except Exception as result:
    print('未知错误')
    print(result)