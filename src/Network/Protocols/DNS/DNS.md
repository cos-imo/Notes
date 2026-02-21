# DNS - Domain Name System

---
[![Static Badge](https://img.shields.io/badge/RFC-1034-blue)](https://datatracker.ietf.org/doc/rfc1034/)
[![Static Badge](https://img.shields.io/badge/RFC-1035-blue)](https://datatracker.ietf.org/doc/rfc1035/)
[![Static Badge](https://img.shields.io/badge/RFC-9499-blue)](https://datatracker.ietf.org/doc/rfc9499/)

---
# Definition

> **Domain Name System (DNS)**  
> Enables the **translation** from a **human-readable domain name** to a **machine-readable IP address**

*Example*
google.com -> 142.251.167.100

*Command*
nslookup (e.g., `$ nslookup google .com)

---
## Algorithm

Operates using a recursive, hierarchical lookup, sequentially querying each domain level until the authoritative record is retrieved.

![DNS Algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/DNS_iterations.svg/960px-DNS_iterations.svg.png)

*From [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/DNS_iterations.svg/960px-DNS_iterations.svg.png)*


**In given example**
	1. The user attempts to access `fr.wikipedia.org`, triggering a DNS resolution request.  
	2. The DNS resolver queries the `root NS`, or *root rame server* (here `a.root-servers.net`) to identify `.org` top-level domain authority.  
	3. `root NS`(`a.root-servers.net`) replies specifying the authoritative server for `.org` domain names (`a0.org.afilias-nst.info`).  
	4. The resolver queries said server (`a0.org.afilias-nst.info`) for `fr.wikipedia.org.   
	5. `a0.org.afilias-nst.info` answers `ns0.wikimedia.org` is in charge of `wikipedia.org` domain.  
	6. The resolver queries `ns0.wikimedia.org` for `fr.wikipedia.org`'s IP address.  
	7. `ns0.wikimedia.org` returns `91.198.174.232`.  
	8. The resolver delivers the IP address to the end user.  

*Note* : In the referenced diagram, the `DNS resolver` is labeled `Serveur DNS récursif`

---
## Structure

The DNS architecture is based on a distributed, tree-like model, structured around root servers, top-level domains, and authoritative name servers.

![DNS Schema](https://upload.wikimedia.org/wikipedia/commons/f/f2/Structure_DNS.jpg)

*From [Wikipedia](https://fr.wikipedia.org/wiki/Domain_Name_System#/media/Fichier:Structure_DNS.jpg)*

