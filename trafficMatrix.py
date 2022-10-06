from scapy.all import *
import pandas as pd
import seaborn as sns
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
    default="matrix.pdf",
    help="output file"
)

args_parser.add_argument(
    "-s",
    type=str,
    required=False,
    default="12x14",
    help="Size of the matrix in inches (example format: 12x14)"
)


args = args_parser.parse_args()

size_x, size_y = map(int, args.s.split('x'))
packets = rdpcap(args.file)

m = []

for packet in packets:
    if packet.haslayer(IP):
        m.append([ packet[IP].src, packet[IP].dst, packet.wirelen])

pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])

df = pd.DataFrame(m, columns=['src','dst', 'size'])
df = df.groupby(["src", "dst"], group_keys=False).sum().reset_index()
somme = df["size"].sum()

df["%"] = df["size"].map(lambda x : float("{:.2f}".format((x/somme)*100)))
result = df.pivot(index='src', columns='dst', values='%')

ax = sns.heatmap(result, annot=True, cmap="PuBu", cbar=False)
ax.get_figure().set_size_inches(size_x, size_y)
ax.get_figure().savefig(args.o)