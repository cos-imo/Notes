# Table des enregistrements DNS – RFC et usage opérationnel

---
# Introduction

Cette page offre une vue consolidée et structurée des différents types d’enregistrements DNS, de leur usage opérationnel et de leur conformité aux standards officiels. Elle a pour objectif de fournir aux équipes techniques et aux consultants en cybersécurité ou en infrastructure réseau un support synthétique et immédiatement exploitable pour la conception, l’audit et la maintenance des architectures DNS. L’approche adoptée privilégie la clarté, la précision et la conformité aux RFC, tout en intégrant les pratiques émergentes et propriétaires.

---

# Sommaire

1. [I. Résolution d’adresses (Web / réseau)](#i-résolution-dadresses-web--réseau)  
2. [II. Services Mail et gouvernance TLS](#ii-services-mail-et-gouvernance-tls)  
3. [III. DNSSEC – Intégrité et validation](#iii-dnssec--intégrité-et-validation)  
4. [IV. Services et applications (VoIP, SIP, découverte de services)](#iv-services-et-applications-voip-sip-découverte-de-services)  
5. [V. Administration de zone et infrastructure](#v-administration-de-zone-et-infrastructure)  
6. [VI. Obscurs ou rares (inclus pour exhaustivité)](#vi-obscurs-ou-rares-inclus-pour-exhaustivité)  
7. [VII. Non standard / propriétaires](#vii-non-standard--propriétaires)  
8. [VIII. Table synthétique consolidée](#viii-table-synthétique-consolidée)  
9. [Liens Datatracker RFC](#liens-datatracker-rfc)

---

## I. Résolution d’adresses (Web / réseau)

| Type             | Fonction principale               | RFC / Statut                   |
| ---------------- | --------------------------------- | ------------------------------ |
| **A**            | Nom → IPv4                        | RFC 1035[^1]                   |
| **AAAA**         | Nom → IPv6                        | RFC 3596[^2]                   |
| **CNAME**        | Alias vers nom canonique          | RFC 1035[^1]                   |
| **DNAME**        | Alias pour sous-arbres            | RFC 6672[^3]                   |
| **HTTPS / SVCB** | Découverte services HTTP modernes | RFC 9460 / vendor-specific[^4] |

### Remarques

- **CNAME / DNAME** : flexibilité pour alias, attention : CNAME ne peut coexister avec d’autres types sur le même nom.
    
- **HTTPS / SVCB** : standardisation récente, remplace certaines pratiques CNAME pour HTTPS.
    

---

## II. Services Mail et gouvernance TLS

|Type|Usage|RFC / Statut|
|---|---|---|
|**MX**|Routage email|RFC 1035[^1]|
|**TXT**|SPF, DKIM, DMARC via TXT|RFC 1035[^1] + RFC dédiées|
|**CAA**|Autorités de certification autorisées|RFC 8659[^5]|

---

## III. DNSSEC – Intégrité et validation

|Type|Rôle|RFC / Statut|
|---|---|---|
|**DNSKEY**|Clé publique DNSSEC|RFC 4034[^6]|
|**RRSIG**|Signature d’un RRset|RFC 4034[^6]|
|**DS**|Lien parent → enfant DNSSEC|RFC 4034[^6]|
|**NSEC / NSEC3**|Preuve de non-existence|RFC 4034 / 5155[^6][^7]|
|**TLSA**|DNS-based TLS auth (DANE)|RFC 6698[^8]|

---

## IV. Services et applications (VoIP, SIP, découverte de services)

| Type       | Usage                                         | RFC / Statut  |
| ---------- | --------------------------------------------- | ------------- |
| **SRV**    | Localisation service + port (VoIP, SIP, XMPP) | RFC 2782[^9]  |
| **NAPTR**  | Réécriture et mapping URIs (ENUM, SIP)        | RFC 3403[^10] |
| **SSHFP**  | Empreinte clé SSH serveur                     | RFC 4255[^11] |
| **LOC**    | Coordonnées géographiques                     | RFC 1876[^12] |
| **URI**    | Mapping de ressources URI                     | RFC 7553[^13] |
| **SMIMEA** | Certificat S/MIME via DNS                     | RFC 8162[^14] |

---

## V. Administration de zone et infrastructure

|Type|Usage|RFC / Statut|
|---|---|---|
|**SOA**|Métadonnées de zone (admin, timers)|RFC 1035[^1]|
|**NS**|Serveurs autoritatifs|RFC 1035[^1]|
|**PTR**|Reverse DNS (IP → nom)|RFC 1035[^1]|

---

## VI. Obscurs ou rares (inclus pour exhaustivité)

|Type|Usage|RFC|
|---|---|---|
|**AFSDB**|AFS Database|RFC 1183[^15]|
|**CERT**|Certificat générique|RFC 4398[^16]|
|**RP**|Responsible Person|RFC 1183[^15]|
|**APL**|Address Prefix List|RFC 3123[^17]|
|**HINFO**|Informations machine|RFC 1035[^1]|

---

## VII. Non standard / propriétaires

|Type|Usage|
|---|---|
|**ANAME / ALIAS**|Alias au niveau apex, résolus côté fournisseur (non RFC)|
|**SVCB / HTTPS**|Services binding modernes, adoption progressive|

---

## VIII. Table synthétique consolidée

> **Note :** La table synthétique ci-dessous reprend l’ensemble des types d’enregistrements détaillés dans les sections précédentes, en indiquant leur usage principal, leur conformité au standard DNS et la référence RFC correspondante. Elle sert de vue consolidée pour consultation rapide.

| Type         | Usage principal                         | Standard | RFC / Statut                   |
| ------------ | --------------------------------------- | -------- | ------------------------------ |
| A            | Nom → IPv4                              | Oui      | RFC 1035[^1]                   |
| AAAA         | Nom → IPv6                              | Oui      | RFC 3596[^2]                   |
| CNAME        | Alias vers nom canonique                | Oui      | RFC 1035[^1]                   |
| MX           | Routage mail                            | Oui      | RFC 1035[^1]                   |
| TXT          | Données arbitraires (SPF, DKIM, DMARC…) | Oui      | RFC 1035[^1]                   |
| NS           | Serveurs DNS autoritatifs               | Oui      | RFC 1035[^1]                   |
| SOA          | Métadonnées de zone                     | Oui      | RFC 1035[^1]                   |
| PTR          | Reverse DNS                             | Oui      | RFC 1035[^1]                   |
| SRV          | Service + port                          | Oui      | RFC 2782[^9]                   |
| CAA          | Autorités de certification autorisées   | Oui      | RFC 8659[^5]                   |
| DS           | Chaînage DNSSEC (parent → enfant)       | Oui      | RFC 4034[^6]                   |
| DNSKEY       | Clés publiques DNSSEC                   | Oui      | RFC 4034[^6]                   |
| RRSIG        | Signature DNSSEC                        | Oui      | RFC 4034[^6]                   |
| NSEC / NSEC3 | Preuve de non-existence DNSSEC          | Oui      | RFC 4034 / 5155[^6][^7]        |
| TLSA         | DANE (TLS via DNSSEC)                   | Oui      | RFC 6698[^8]                   |
| NAPTR        | Réécriture + découverte de services     | Oui      | RFC 3403[^10]                  |
| LOC          | Coordonnées géographiques               | Oui      | RFC 1876[^12]                  |
| SSHFP        | Empreintes clés SSH                     | Oui      | RFC 4255[^11]                  |
| HTTPS / SVCB | Découverte services HTTPS modernes      | Oui      | RFC 9460 / vendor-specific[^4] |
| ANAME        | Alias à l’APEX                          | Non      | Vendor-specific                |
| ALIAS        | Alias à l’APEX                          | Non      | Vendor-specific                |

---

## Liens Datatracker RFC

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