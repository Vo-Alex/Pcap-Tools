from scapy.all import *
import graphviz
from socket import getservbyport

import argparse

args_parser = argparse.ArgumentParser()

args_parser.add_argument(
    "file",
    help="pcap file"
)

args_parser.add_argument(
    "-o",
    type=str,
    required=False,
    default="service_dependencies",
    help="output file"
)


args_parser.add_argument(
    "-T",
    type=str,
    required=False,
    default="pdf",
    help="output format"
)

args_parser.add_argument(
    "-p",
    type=int,
    required=False,
    default=10000,
    help="upper limit of the port range used for the analysis "
)

args = args_parser.parse_args()

packets = rdpcap(args.file)

max_port = args.p
m = set()

for packet in packets:
    if packet.haslayer(IP):
        if packet.haslayer(TCP)and packet[TCP].dport < max_port:
            m.add((packet[IP].src, packet[IP].dst, packet[TCP].dport))
        if packet.haslayer(UDP) and packet[UDP].dport < max_port:
            m.add((packet[IP].src, packet[IP].dst, packet[UDP].dport))


dot = graphviz.Digraph(args.o)  

for c in m:
    try:
        label = getservbyport(c[2])
    except:
        label = str(c[2])
    dot.edge(str(c[0]), str(c[1]), label=label)

dot.render(format=args.T)