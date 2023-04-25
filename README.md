# Socketer
It is possible to check the operation of the service over tcp and udp
пример использования:
tcp chek
Sock = Socketer.Socketer()
request = Socketer.Sock.tcp()
tcpresult = Socketer.tcp.success
udp chek
Sock = Socketer.Socketer()
request = Socketer.Sock.udp()
tcpresult = Socketer.udp.success
