from scapy.all import Ether, ARP, wrpcap

packets_data = [
    {
        "src_mac": "00:11:22:33:44:55",
        "dst_mac": "ff:ff:ff:ff:ff:ff",
        "src_ip": "10.0.0.1",
        "dst_ip": "10.0.0.2",
        "op": 1  # 1 = ARP request, 2 = ARP reply
    },
    {
        "src_mac": "66:77:88:99:AA:BB",
        "dst_mac": "00:11:22:33:44:55",
        "src_ip": "10.0.0.2",
        "dst_ip": "10.0.0.1",
        "op": 2
    }
]

packets = []

for pkt in packets_data:
    arp_pkt = Ether(src=pkt["src_mac"], dst=pkt["dst_mac"]) / ARP(
        op=pkt["op"],
        hwsrc=pkt["src_mac"],
        psrc=pkt["src_ip"],
        hwdst=pkt["dst_mac"],
        pdst=pkt["dst_ip"]
    )
    packets.append(arp_pkt)

wrpcap("arp.pcap", packets)
