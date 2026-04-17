import logging
import struct
from dnsparser import DnsParser
from utils import get_bytes

logger = logging.Logger(__name__)
logger.info("Debug started")

class DnsResponse():

    def __init__(self,parser):
        self.req_header = parser.header

        self.res_header = None
        self.res_question = None

        self.final_response = None


        self.set_header()
        self.set_quesion()

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
        TC = "0"
        RD = "1"
        RA = "1"
        Z = "000"
        RCODE = "0"

        flags += QR
        flags += OP_CODE
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
        packet = parser.get_raw_packets()
