import struct
from models import DnsHeader


class DnsParser:

    def __init__(self,packet):
        self.packet = packet
        self.flags_dict = {}
        self.domain = None

    def parse(self):
        self.unpack_header()
        self.unpack_flags()
        self.unpack_domain()


    def unpack_header(self):
        header = struct.unpack("!6H",self.packet[:12])
        self.header = DnsHeader(*header)


    def unpack_flags(self):
        bin_flags = format(self.header.flags,"016b")
        print(f"flags in binary is {bin_flags}")
    
        self.flags_dict["QR"] = bin_flags[0]
        self.flags_dict["OP_CODE"] = bin_flags[1:5]
        self.flags_dict["TC"] = bin_flags[6:7]
        self.flags_dict["RD"] = bin_flags[7:8]
    

    def unpack_domain(self):
        offset = 12
        remaining_data = self.packet[offset:]
        label = remaining_data[0]

        domain = []
        while True:
            length = self.packet[offset]
            if length == 0:
                offset+=1
                break
            offset+=1
            label = self.packet[offset:offset+length].decode()
            domain.append(label)
            offset+=length
        
        self.domain =  ".".join(domain)

    def get_domain(self):
        return self.domain
    
    def get_flags_dict(self):
        return self.flags_dict
    
    def get_headers(self):
        return self.header
    
    def get_raw_packets(self):
        return self.packet