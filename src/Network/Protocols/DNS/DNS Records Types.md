# DNS Record Types Table
---
[![Static Badge](https://img.shields.io/badge/DNS-Main_page-brown)](DNS.md)

---
# Introduction

This page provides an overview of the different DNS record types, their operational usage, and their compliance with official standards.
Links to the relevant RFC pages are available at the bottom of this document.

---

# Table of Contents

1. [Address Resolution (Web / Network)](#address-resolution-web--network)  
2. [Mail Services and TLS Governance](#mail-services-and-tls-governance)  
3. [DNSSEC – Integrity and Validation](#dnssec--integrity-and-validation)  
4. [Services and Applications (VoIP, SIP, Service Discovery)](#services-and-applications-voip-sip-service-discovery)  
5. [Zone Administration and Infrastructure](#zone-administration-and-infrastructure)  
6. [Rare Types](#rare-types)  
7. [Non-standard / Proprietary](#non-standard--proprietary)  
8. [Summary Table](#summary-table)  
9. [RFC Datatracker Links](#rfc-datatracker-links)

---

## Address Resolution (Web / Network)

| Type             | Primary Function                    | RFC / Status                   |
| ---------------- | ----------------------------------- | ------------------------------ |
| **A**            | Name → IPv4                         | RFC 1035[^1]                   |
| **AAAA**         | Name → IPv6                         | RFC 3596[^2]                   |
| **CNAME**        | Alias to canonical name             | RFC 1035[^1]                   |
| **DNAME**        | Alias for subtrees                  | RFC 6672[^3]                   |
| **HTTPS / SVCB** | Modern HTTP service discovery       | RFC 9460 / vendor-specific[^4] |

### Notes

- **CNAME / DNAME**: Provide aliasing flexibility; a CNAME cannot coexist with other record types on the same name.
- **HTTPS / SVCB**: Recently standardized, replacing certain CNAME-based practices for HTTPS.

---

## Mail Services and TLS Governance

| Type | Usage                              | RFC / Status                   |
| ---- | ---------------------------------- | ------------------------------ |
| **MX** | Email routing                    | RFC 1035[^1]                   |
| **TXT** | SPF, DKIM, DMARC via TXT records | RFC 1035[^1] + RFC dédiées  |
| **CAA** | Authorized certification authorities | RFC 8659[^5]               |

---

## DNSSEC – Integrity and Validation

| Type | Role                               | RFC / Status                   |
| ---- | ---------------------------------- | ------------------------------ |
| **DNSKEY** | DNSSEC public key             | RFC 4034[^6]                   |
| **RRSIG** | RRset signature               | RFC 4034[^6]                   |
| **DS** | Parent → child DNSSEC linkage     | RFC 4034[^6]                   |
| **NSEC / NSEC3** | Proof of non-existence | RFC 4034 / 5155[^6][^7]        |
| **TLSA** | DNS-based TLS authentication (DANE) | RFC 6698[^8]              |

---

## Services and Applications (VoIP, SIP, Service Discovery)

| Type       | Usage                                      | RFC / Status  |
| ---------- | ------------------------------------------ | ------------- |
| **SRV**    | Service location + port (VoIP, SIP, XMPP)  | RFC 2782[^9]  |
| **NAPTR**  | URI rewriting and mapping (ENUM, SIP)      | RFC 3403[^10] |
| **SSHFP**  | SSH server key fingerprints                | RFC 4255[^11] |
| **LOC**    | Geographic coordinates                     | RFC 1876[^12] |
| **URI**    | URI resource mapping                       | RFC 7553[^13] |
| **SMIMEA** | S/MIME certificate via DNS                 | RFC 8162[^14] |

---

## Zone Administration and Infrastructure

| Type | Usage                                   | RFC / Status |
| ---- | --------------------------------------- | ------------ |
| **SOA** | Zone metadata (admin, timers)        | RFC 1035[^1] |
| **NS** | Authoritative name servers             | RFC 1035[^1] |
| **PTR** | Reverse DNS (IP → name)               | RFC 1035[^1] |

---

## Rare Types

| Type | Usage                    | RFC |
| ---- | ------------------------ | --- |
| **AFSDB** | AFS Database | RFC 1183[^15] |
| **CERT** | Generic certificate   | RFC 4398[^16] |
| **RP** | Responsible Person       | RFC 1183[^15] |
| **APL** | Address Prefix List     | RFC 3123[^17] |
| **HINFO** | Host information      | RFC 1035[^1] |

---

## Non-standard / Proprietary

| Type | Usage |
| ---- | ----- |
| **ANAME / ALIAS** | Apex-level aliasing, provider-resolved (non-RFC) |
| **SVCB / HTTPS** | Modern service bindings, progressive adoption |

---

## Summary Table

> The table below aggregates all DNS record types detailed in the previous sections, indicating their primary usage, DNS standard compliance, and corresponding RFC references.

| Type         | Primary Usage                        | Standard | RFC / Status                   |
| ------------ | ------------------------------------ | -------- | ------------------------------ |
| A            | Name → IPv4                          | Yes      | RFC 1035[^1]                   |
| AAAA         | Name → IPv6                          | Yes      | RFC 3596[^2]                   |
| CNAME        | Alias to canonical name              | Yes      | RFC 1035[^1]                   |
| MX           | Mail routing                         | Yes      | RFC 1035[^1]                   |
| TXT          | Arbitrary data (SPF, DKIM, DMARC…)   | Yes      | RFC 1035[^1]                   |
| NS           | Authoritative DNS servers            | Yes      | RFC 1035[^1]                   |
| SOA          | Zone metadata                        | Yes      | RFC 1035[^1]                   |
| PTR          | Reverse DNS                          | Yes      | RFC 1035[^1]                   |
| SRV          | Service + port                       | Yes      | RFC 2782[^9]                   |
| CAA          | Authorized certification authorities | Yes      | RFC 8659[^5]                   |
| DS           | DNSSEC chaining (parent → child)     | Yes      | RFC 4034[^6]                   |
| DNSKEY       | DNSSEC public keys                   | Yes      | RFC 4034[^6]                   |
| RRSIG        | DNSSEC signature                     | Yes      | RFC 4034[^6]                   |
| NSEC / NSEC3 | DNSSEC proof of non-existence        | Yes      | RFC 4034 / 5155[^6][^7]        |
| TLSA         | DANE (TLS via DNSSEC)                | Yes      | RFC 6698[^8]                   |
| NAPTR        | Rewriting + service discovery        | Yes      | RFC 3403[^10]                  |
| LOC          | Geographic coordinates               | Yes      | RFC 1876[^12]                  |
| SSHFP        | SSH key fingerprints                 | Yes      | RFC 4255[^11]                  |
| HTTPS / SVCB | Modern HTTPS service discovery       | Yes      | RFC 9460 / vendor-specific[^4] |
| ANAME        | Apex alias                           | No       | Vendor-specific                |
| ALIAS        | Apex alias                           | No       | Vendor-specific                |

---

## RFC Datatracker Links

[^1]: RFC 1035 – Domain Names – Implementation and Specification  
[^2]: RFC 3596 – DNS Extensions to Support IPv6  
[^3]: RFC 6672 – DNAME Redirection in the DNS  
[^4]: RFC 9460 – Service Binding (SVCB) and HTTPS RR  
[^5]: RFC 8659 – Certification Authority Authorization (CAA)  
[^6]: RFC 4034 – Resource Records for the DNS Security Extensions  
[^7]: RFC 5155 – DNSSEC NSEC3  
[^8]: RFC 6698 – The DNS-Based Authentication of Named Entities (DANE) Protocol  
[^9]: RFC 2782 – A DNS RR for Specifying the Location of Services  
[^10]: RFC 3403 – Naming Authority Pointer (NAPTR) RR  
[^11]: RFC 4255 – Using DNS to Securely Publish SSH Key Fingerprints  
[^12]: RFC 1876 – DNS Encoding of Geographic Locations  
[^13]: RFC 7553 – The URI DNS Resource Record  
[^14]: RFC 8162 – S/MIME Certificate Distribution via DNS  
[^15]: RFC 1183 – AFSDB / Responsible Person (RP)  
[^16]: RFC 4398 – CERT RR – Certification Authority RR  
[^17]: RFC 3123 – Address Prefix List (APL)