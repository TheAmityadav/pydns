import socket

from dnsparser import DnsParser
from dnsresponse import DnsResponse
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
    reponse = DnsResponse(parser=parser)
    parser.parse()
    domain  = parser.get_domain()
    headers = parser.get_headers()
    print(f"Heders in thr Request are {headers}")


    tid_bytes = headers.tid
    print(f"tid in binary is {format(tid_bytes,"016b")}")
    print(f"Domain is {domain}")

    rep_data = tid_bytes.to_bytes(2,"big")
    print(f"rep data is {rep_data}")
    sock.sendto(rep_data,address)






