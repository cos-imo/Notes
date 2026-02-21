# TLS/SSL
---
**Related pages**  
[![Static Badge](https://img.shields.io/badge/OSI-Layer_6-orange)](../../OSI%20Model.md)  
**Related RFCs**  
[![Static Badge](https://img.shields.io/badge/RFC-5246-blue)](https://datatracker.ietf.org/doc/rfc5246/)
[![Static Badge](https://img.shields.io/badge/RFC-6347-blue)](https://datatracker.ietf.org/doc/rfc6347/)
[![Static Badge](https://img.shields.io/badge/RFC-4346-blue)](https://datatracker.ietf.org/doc/rfc4346/)
[![Static Badge](https://img.shields.io/badge/RFC-2246-blue)](https://datatracker.ietf.org/doc/rfc2246/)
[![Static Badge](https://img.shields.io/badge/RFC-6101-blue)](https://datatracker.ietf.org/doc/rfc6101/) 
[![Static Badge](https://img.shields.io/badge/Wikipedia-RFC_list-white?logo=wikipedia)](https://en.wikipedia.org/wiki/Transport_Layer_Security#IETF_Request_for_comments) 

---
# Summary
1. [Definition](#definition)
2. [Requests](#requests)
3. [Status codes](#status-codes)
4. [Responses](#responses)

---
# Definition

> **Transport Layer Security (TLS)**  
> Cryptographic **protocol** providing **confidentiality, integrity and authentication** for communications over a **computer network**.  
> **TLS** is the successor of the now depreciated **Secure Socket Layer (SSL)**; while the terms are commonly used indistinctly, **TLS is the protocol currently standardized and deployed**

**Key characteristics**
 - Relies on a **three-way handshake**
 - **Session-oriented** protocol
 - Provides **end-to-end encryption** and **peer authentication**
 - **Multiple protocol versions**: SSL 1.0, SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

### Protocol versions
#### Deprecated and insecure versions
 - **SSL 1.0** - Never released
 - **SSL 2.0** - Cryptographically broken
 - **SSL 3.0** - Vulnerable to POODLE attacks
 - **TLS 1.0** - defined in [RFC 2246]() - Deprecated due to *weak cryptographic primitives*
 - **TLS 1.1** - defined in [RFC 4346]() - Deprecated and no longer recommended
 > **Note** : All versions listed above are **deprecated** and **should not be used**
 
#### Supported and secure versions
 - **TLS 1.2** - defined in [RFC 5246]() - updated in [RFC 8446]()
	 - Uses SHA-256 (instead of MD5 and SHA-1 combination)
	 - Added AES-GCM and AES-CCM
	 - Still widely deployed and used
	 - Authentication is **embedded in cipher suite**, thus the certificate is **tightly coupled to it**
 - **TLS 1.3** - defined in [RFC 8446]()
	- Removes insecure algorithms and features
	- Reduces handshake latency
	- Authentication and key exchange are **decoupled** from cipher suites (negotiated via `signature_algorithm`), increasing flexibility, configuration and auditing

**Note**
 - To explore TLS interactively, check out the `TLS` section of the `Crypto on the web` page from `cryptohack.org`:
[![Static Badge](https://img.shields.io/badge/Cryptohack-Crypto_on_the_web-orange)](https://cryptohack.org/challenges/web/)   

---
# Handshake
TLS relies on a **handshake**, performed between the client and the server at connection initialization.  
Make sure to read the given documentation about TLS handshake risks.  
Below is a handshake overview.  

### TLS 1.2 handshake

1. **Client Hello**
	 - Supported TLS versions, supported cipher suites, supported compression methods, Client nonce, extensions.   

2. **Server Hello**
	 - Selected TLS version, selected cipher suite, server nonce.  

3. **Certificate**
	 - Server X.509 certificate chain, public key.  

4. **ServerKeyExchange** (if applicable)
	 - Key exhange parameters, digital signature.  

5. **ClientKeyExchange**
	 - Pre-master secret (RSA) or client key share (ECDHE)

6. **ChangeCipherSpec / Finished**
	 - Confirmation of negotiated parameters, handshake integrity verification.  

### TLS 1.3 handshake

1. **Client Hello**
	 - Supported TLS versions, supported cipher suites, supported signature algorithms, key shares (ECDHE), extensions.   

2. **Server Hello**
	 - Selected TLS version, selected cipher suite, selected key share.  

3. **Ecnrypted Extensions**
	 - Negotiated extensions.  

4. **Certificate**
	 - Server certificate chain, authentication context.

5. **CertificateVerify**
	 - Server proof of private key ownership

6. **Finished**
	 - Handshake transcript verification, keys activated.  

---
# Certificates

TLS relies on **X.509 certificates** to authenticate servers within a **public key infrastructure (PKI)**. Certificates are typically issued by a trusted **Certificate Authority (CA)**.

**Key considerations**
 - Verify that certificates are **valid**, **unexpired**, and issued by a **trusted CA**.  
 - Confirm **key strength** (e.g., RSA > 2048 bits).  
 - Check that **signature algorithms** are not **deprecated**.  
 - Ensure the **certificate chain** is **complete** and **correctly configured**.  
 - Confirm **hostname matching**.  

---
# Common attacks

**Renegociation**
	Exploiting unsafe TLS renegociation sequences
**Downgrade attacks**
	Forcing a connection to use older/weaker TLS or SSL versions
**Cross-protocols attacks**
	Leveraging compatibility with SSL/TLS in other services
**Time attacks**
**Cipher-specific attacks**
	**BEAST**
		Exploits TLS 1.0 CBC mode
	**CRIME**
		Targets TLS compression
	**POODLE**
		Exploit SSL 3.0 padding issued
	**RC4**
		Weak stream cipher in legacy TLS.
**Truncation and plaintext attack**
	Forcing premature session closure or exposing data.
**Heartbleed**
	Exploits vulnerable OpenSSL heartbeat implementations
**TLS interception / MiTM**
	Unauthorized inteception of traffic, usually via rogue certificates

---
# References & recommended readings

[![Static Badge](https://img.shields.io/badge/OWASP-TLS_Cheasheet-orange?logo=owasp)](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)  
[![Static Badge](https://img.shields.io/badge/OWASP-Testing_for_weak_SSL_TLS_ciphers-orange?logo=owasp)](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/01-Testing_for_Weak_SSL_TLS_Ciphers_Insufficient_Transport_Layer_Protection)  
[![Static Badge](https://img.shields.io/badge/OWASP-Testing_for_Weak_Transport_Layer_Security-orange?logo=owasp)](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/01-Testing_for_Weak_Transport_Layer_Security)  
[![Static Badge](https://img.shields.io/badge/MITTRE-AiTM:_Service_Based_Interface-blue)](https://fight.mitre.org/techniques/FGT1557.504/)   
[![Static Badge](https://img.shields.io/badge/messervicescyber-Security_recommendations_for_TLS-blue)](https://messervices.cyber.gouv.fr/documents-guides/security-recommendations-for-tls_v1.1.pdf)   
[![Static Badge](https://img.shields.io/badge/CWE_757-Selection_of_Less_Secure_Algorithm_During_Negociation-blue)](https://fight.mitre.org/techniques/FGT1557.504/)  