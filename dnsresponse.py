import socket

class DnsResponse:


    def __init__(self,domain,upstream_dns):
        self.domain = domain
        self.upstream_dns = upstream_dns


    def query_from_upstream(self,packet):
        PORT = 53

        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.settimeout(2)
        s.sendto(packet,(self.upstream_dns,PORT))

        res,_ = s.recvfrom(512)
        print(f"res we got from upstream is \n {res}")
        return res



