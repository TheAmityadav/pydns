import subprocess


class DnsResponse:


    def __init__(self,domain,upstream_dns):
        self.domain = domain
        self.upstream_dns = upstream_dns

    def query_from_upstream(self):
        cmd = f"dig {self.domain} @{self.upstream_dns}"
        status, output = subprocess.getstatusoutput(cmd)
        print(f"query_from_upstream--1--status {status}\n\
              Output is {output}")
        if status and status == 0:
            return output


    



