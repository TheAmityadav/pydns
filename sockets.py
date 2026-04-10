import struct
import socket
ip = "0.0.0.0"
port = 8053

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))


def unpack_header(data):
    header = struct.unpack("!6H",data[:12])
    tid = header[0]
    flags = header[1]
    questions = header[2]
    answer_rr = header[3]
    authority_rr = header[4]
    additional_rr = header[5]
    print(f"tid is {tid} as hex {hex(tid)} as binary {bin(tid)}")
    print(f"flags is {flags} as hex {hex(flags)} as binary {bin(flags)}")
    print(f"questions is {questions} as hex {hex(questions)} as binary {bin(questions)}")
    print(f"answer_rr is {answer_rr} as hex {hex(answer_rr)} as binary {bin(answer_rr)}")
    print(f"authority_rr is {authority_rr} as hex {hex(authority_rr)} as binary {bin(authority_rr)}")
    print(f"additional_rr is {additional_rr} as hex {hex(additional_rr)} as binary {bin(additional_rr)}")
    unpack_flags(flags)

def unpack_flags(flags):
    bin_flags = format(flags,"016b")
    print(f"flags in binary is {bin_flags}")
    QR = bin_flags[0]
    OP_CODE = bin_flags[1:5]
    TC = bin_flags[6:7]
    RD = bin_flags[7:8]

    print(f"QR is {QR} | OP_CODE is {OP_CODE} | TC is {TC} Rd is {RD}")


def get_domain(data):
    print(f"type if data is {type(data)}")
    offset = 12
    remaining_data = data[offset:]
    print(f"get_domain --1-- remaining_data {remaining_data}")
    label = remaining_data[0]
    print(f"label is {label}")

    domain = []
    while True:
        length = data[offset]
        print(f"get_domain--2--lenght {length}")
        if length == 0:
            offset+=1
            break
        offset+=1
        print(f"raw label is { data[offset:offset+length]}")
        label = data[offset:offset+length].decode()
        domain.append(label)
        offset+=length
    print(f"domains is {domain}")
    return ".".join(domain)


def unpack_req_data(data):
    unpack_header(data)
    domain = get_domain(data)
    print(f"domain is {domain}")

while 1:
    print(f"Starting the server")
    data,address = sock.recvfrom(1024)
    print(f"The data is {data} and address is {address}")
    unpack_req_data(data)

    


    sock.sendto(b"Hello World",address)