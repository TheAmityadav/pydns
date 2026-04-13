from dataclasses import dataclass

@dataclass
class DnsHeader:
    tid : int
    flags : int
    questions : int
    answer_rr : int
    authority_rr : int
    additional_rr : int
