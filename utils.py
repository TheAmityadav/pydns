import socket


upstream_dns = "8.8.8.8"
PORT = 53

def query_from_upstream(packet):

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.settimeout(2)
    s.sendto(packet,(upstream_dns,PORT))

    res,_ = s.recvfrom(512)
    print(f"res we got from upstream is \n {res}")
    return res

