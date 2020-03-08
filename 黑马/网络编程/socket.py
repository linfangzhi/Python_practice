'''

'''

import socket

def main():
    #创建一个tcp
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    # 从键盘输入数据
    sned_data = input('输入')

    #使用套接字收发
    udp_socket.sendto(sned_data.encode('utf-8'), ('192.168.50.1',8080))
    #关闭

    udp_socket.close()




if __name__ =='__main__':
    main()