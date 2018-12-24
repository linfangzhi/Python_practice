def input_pasd():
    # 提示输入密码
    pwd = input('please input pasd')

    if len(pwd) >= 8:
        return pwd
    print('主动抛出异常')
    # 创建异常对象-可以使用错误信息字符串作为参数
    ex = Exception('密码长度不够')
    # 抛出异常
    raise ex

try:
    print(input_pasd())

except Exception as result:
    print(result)
