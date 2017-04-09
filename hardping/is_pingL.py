# is_pingL
# Authon:Luis Angel Lopez Mascaraque
# Date: Abr 17

import os


def is_ping(hostname):
    filename = hostname + ".txt"
    os.system("ping -n 1 " + hostname + ">" + filename)
    presente = True
    for i in open(filename).readlines():
        if i.find("inaccesible") > 0:
            presente = False
        if i.find("perdidos = 1") > 0:
            presente = False
    os.remove(filename)
    return presente


def test(ip):
    if is_ping(ip) is True:
        print ("La ip ", ip, " esta presente")
    else:
        print ("La ip", ip, "no presente")


def main():
    test("192.168.1.1")


if __name__ == "__main__":
    main()
