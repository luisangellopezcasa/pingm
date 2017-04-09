# hardping
# author: Luis Angel Lopez Mascaraque
# date: Abr-2017
import os
import is_pingL
import sys


def getmac(hostname):
    filename = "arp_" + hostname + ".txt"
    os.system("arp -a " + hostname + ">" + filename)
    a = open(filename).readlines()
    if (len(a) > 3):
        mac = a[3].split()[1].replace("-", ":").upper()
    else:
        mac = "00:00:00:00:00:00"
    os.remove(filename)
    return mac


def hardping(ip):
    if is_pingL.is_ping(ip) is True:
        return getmac(ip)
    return False


def test(ip):
    print (ip, hardping(ip))


def main():
    if len(sys.argv) < 2:
        print(sys. argv[0], "ip")
    else:
        test(sys.argv[1])


if __name__ == "__main__":
    main()
