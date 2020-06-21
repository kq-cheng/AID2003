"""
select io多路方法示例
"""

from select import select
from socket import *
from time import sleep

s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

f = open("mylog.log",'r')


print("IO监控")
sleep(5)
rs,ws,xs = select([s,f],[],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)