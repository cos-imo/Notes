# ARP - Address Resolution Protocol
---
[![Static Badge](https://img.shields.io/badge/OSI-Layer_2-orange)](Network/OSI%20Model.md)
[![Static Badge](https://img.shields.io/badge/RFC-826-blue)](https://datatracker.ietf.org/doc/rfc826/)
[![Static Badge](https://img.shields.io/badge/RFC-903-blue)](https://datatracker.ietf.org/doc/rfc903/)
[![Static Badge](https://img.shields.io/badge/RFC-2390-blue)](https://datatracker.ietf.org/doc/rfc2390/)
[![Static Badge](https://img.shields.io/badge/RFC-5227-blue)](https://datatracker.ietf.org/doc/rfc5227/)

---
# Definition

> **Address Resolution Protocol (ARP)**  
> Enables the **mapping** from a **IPv4 address** to a **link-layer (MAC) address** *within the same local network segment*

---
# Workflow

Blueprint
  : **ARP Request:** A host broadcasts a request: "Who has IP X.X.X.X?"
  : **ARP Reply**: The host with X.X.X.X IP responds with its MAC address
  : **Resolution**: The requesting host updates its [ARP cache](#arp-cache) and uses given IPv4 address

## Showcase
A **PCAP file** demonstrating a ARP request and response is provided below.  
[![Static Badge](https://img.shields.io/badge/Download-pcap_file-blue?logo=wireshark&logoColor=blue)](https://raw.githubusercontent.com/cos-imo/Notes/refs/heads/main/src/Network/Protocols/ARP/arp.pcap)   
This capture was generate using [this Python script](https://github.com/cos-imo/Notes/blob/main/src/Network/Protocols/ARP/generate_arp_pcap.py) leveraging the [scapy library](https://scapy.net/).  

---
# ARP Cache
 - Hosts store resolved IP->MAC records mappings in a **local ARP cache** to reduce repeated broadcast traffic.  
 - Entries have a **time-to-live (TTL)**
 - **Proper cache management is critical**; cf the [ARP Spoofing](#arp-spoofing) and [ARP flooding](#arp-flooding) section

---
# Proxy ARP
 - Routers may respond to ARP request on behalf of remote hosts in different subnets
 - Useful for legacy networks

---
# Common attacks

## ARP Spoofing
An attacker responds to an ARP request that was not meant for him, thus impersonating the original person

## ARP Flooding
The attacker floods the network with ARP answers; after that, every request goes to the attacker

---
# Security mitigations
 - **Static ARP entries**: Configure critical hosts to prevent spoofing
 - **Dynamic ARP inspection (DAI)**: Enforce ARP validation on managed switches
 - **Segmentation and VLANs**: Limit broadcasts to reduce attack surface
 - Disable **ARP gleaning**

---
# References and recommended readings
[![Static Badge](https://img.shields.io/badge/Varonis-ARP_Poisoning-black)](https://www.varonis.com/blog/arp-poisoning)  
[![Static Badge](https://img.shields.io/badge/SentinelOne-ARP_Spoofing-purple)](https://www.sentinelone.com/fr/cybersecurity-101/threat-intelligence/arp-spoofing/)  
[![Static Badge](https://img.shields.io/badge/OWASP-MiTM_via_ARP-orange?logo=owasp)](https://attack.mitre.org/techniques/T1557/002/)  
[![Static Badge](https://img.shields.io/badge/SANS-Packet_sniffing_in_a_switched_environment-blue)](https://www.sans.org/white-papers/244)  
[![Static Badge](https://img.shields.io/badge/Juniper-DAI-black)](https://www.juniper.net/documentation/us/en/software/junos/security-services/topics/topic-map/understanding-and-using-dai.html)
[![Static Badge](https://img.shields.io/badge/CISCO-ARP_Flooding_and_ARP_Gleaning-blue?logo=cisco)](https://www.cisco.com/c/en/us/support/docs/technical-details/222179-understand-arp-flooding-and-arp-gleaning.html#toc-hId--2107072336)
