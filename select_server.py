"""
select实现 网络IO并发处理
重点代码

思路：
1. 必须同时关注客户端链接（监听套接字）和客户端收发消息（链接套接字）
2. 循环监控，哪个IO就绪我们就处理哪个
"""

from socket import *
from select import select

# 创建监听套接字，让客户端链接
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)

# 初始我们关注sockfd的读事件 （客户端链接事件）
rlist = [sockfd]
wlist = []
xlist = []


# 循环监控所有IO对象事件的发生
while True:
    print("在监控IO事件的发生哦")
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is sockfd:
            # 监听套接字就绪
            connfd,addr = r.accept()
            print("Connect from",addr)
            rlist.append(connfd) # 每当有一个客户端链接，就将这个链接套接字加入监控
        else:
            # 某个客户端链接套接字就绪
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r) # 不在关注这个客户端
                r.close()
                continue
            print(data)
            r.send(b'OK')



