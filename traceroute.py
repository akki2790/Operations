#traceroute script

from scapy.all import *
hostname= 'goolge.com'
for i in range(1,28):
    pkt=IP(dest=hostname, ttl=i)/UDP(dport=33434)
    reply=sr1(pkt, verbose=0)
    if reply is None:
        break
    elif reply.type==3:
        print 'We have reached ' + str(reply.src)
    else:
        print '%d hops away: ' %i + str(reply.src)
