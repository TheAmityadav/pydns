import logging
import struct
from dnsparser import DnsParser
from utils import get_bytes

logger = logging.Logger(__name__)
logger.info("Debug started")

class DnsResponse():

    def __init__(self,parser):
        self.req_header = parser.header
        self.parser = parser
        self.res_header = None
        self.res_question = None
        self.res_answer = None


        self.set_header()
        self.set_quesion()
        self.set_answer()
        print(f"res answer is {self.res_answer}")
        
        self.final_response = self.res_header + self.res_question + self.res_answer

        print(f"final reposne is made_---{self.final_response}")


    def get_response(self):
            return self.final_response


    ####HEADER SECTION ##################

    def set_header(self):
        tid = self.set_reply_tid()
        flags = self.set_reply_flags()
        bytes_flags = int(flags,2)
        qd = self.set_qd_count()
        ans = self.set_ans_count()
        ns = self.set_NSCOUNT()
        ar = self.set_ARCOUNT()
        self.res_header = struct.pack("!HHHHHH",tid,bytes_flags,qd,ans,ns,ar)


        print(f"1------set header init tid is {tid}")
        print(f"2----set header init bytes_flags is {bytes_flags}")
        print(f"3----set header init bytes_qd is {qd}")
        print(f"4----set header init ans_bytes is {ans}")
        print(f"5----set header init ns_bytes is {ns}")
        print(f"6----set header init ar_bytes is {ar}")
        print(f"self.res_header is {self.res_header}")

    def set_reply_tid(self):
        tid = self.req_header.tid
        print(f"tid is {tid}")
        return tid

    def set_reply_flags(self):
        flags = ""

        QR = "1"
        OP_CODE = "0000"
        AA = "0"
        TC = "0"
        RD = "1"
        RA = "1"
        Z = "000"
        RCODE = "0000"

        flags += QR
        flags += OP_CODE
        flags += AA
        flags += TC
        flags += RD
        flags += RA
        flags += Z
        flags += RCODE

        return flags

    def set_qd_count(self):
        QD = self.req_header.questions
        return QD

    def set_ans_count(self):
        ANS_COUNT = 1
        return ANS_COUNT

    def set_NSCOUNT(self):
        NSCOUNT = 0
        return NSCOUNT

    def set_ARCOUNT(self):
        ARCOUNT = 0
        return ARCOUNT
    
#################HEADERS END #######################

    


###################DNS Questions   #################

    def set_quesion(self):
        packet = self.parser.get_raw_packets()
        self.res_question = packet[12:28]
        print(f"packet 12th valus is {packet[12]}")


    def set_answer(self):
        name = 0xc00c
        type = 0x0001
        dns_class = 0x0011
        ttl = 0x0000003c
        rdlength = 0x0004
        rdata = 0x99999999

        self.res_answer = struct.pack("!HHHIHI",name,type,dns_class,ttl,rdlength,rdata)
