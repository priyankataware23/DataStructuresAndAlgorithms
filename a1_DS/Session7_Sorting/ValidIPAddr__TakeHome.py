import string
def validIPAddr (ip):
    if ip==None:
        return -1
    if check_ipv4 (ip):
        return "IPv4"
    elif check_ipv6 (ip):
        return "IPv6"
    else:
        return "Neither"

def check_ipv4(ip):
    split_group=ip.split(".")
    if len(split_group)==0 or len(split_group)<4:
        return False
    for group in split_group:
        if not group.isdigit() or int(group)<0 or int(group)>255:
            return False
        if group[0]=='0' and len(group)>=1:
            return False
        if len(group)==0:
            return False
    return True

def check_ipv6(ip):

    split_gr = ip.split(":")
    if len(split_gr)==0 or len(split_gr)<8:
        return False
    for group in split_gr:
        if len(group)<1 or len(group)>4:
            return False
        for chars in group:
            if chars not in string.hexdigits:
                return False
    return True


test_data = [   "172.16.254.1",
                "2001:0db8:85a3:0:0:8A2E:0370:7334",
                "1e1.4.5.6",
                "01.01.01.01",
                "2001:0db8:85a3:00000:0:8A2E:0370:7334",
                "20EE:FGb8:85a3:0:0:8A2E:0370:7334",
                "1081:db8:85a3:01:-0:8A2E:0370:7334",
                "2001:db8:85a3:0::8a2E:0370:7334"
            ]

# expected output:
'''
IPv4
IPv6
Neither
Neither
Neither
Neither
Neither
'''

for data in test_data:
  print(validIPAddr(data))




