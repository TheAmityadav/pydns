import struct
import socket

from dnsparser import DnsParser
from dnsresponse import DnsResponse

ip = "0.0.0.0"
port = 8053

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))




while 1:
    print(f"Starting the server")
    data,address = sock.recvfrom(1024)
    print(f"The data is {data} and address is {address}")
    parser = DnsParser(data)
    parser.parse()
    domain  = parser.get_domain()

    responser = DnsResponse(domain,"8.8.8.8")
    response = responser.query_from_upstream()

    print(f"Domain is {domain}")
    print(f"Response form upstream server is {response}")


    sock.sendto(b"Hello World",address)