# HTTP - HyperText Transfer Protocol
---
**Related pages**  
[![Static Badge](https://img.shields.io/badge/OSI-Layer_7-orange)](../../OSI%20Model.md)
[![Static Badge](https://img.shields.io/badge/HTTP-Reponse_header_fields-brown)](./HTTP%20response%20header%20fields.md)
[![Static Badge](https://img.shields.io/badge/HTTP-Request_header_fields-brown)](./HTTP%20request%20header%20fields.md)  
**Related RFCs**  
[![Static Badge](https://img.shields.io/badge/RFC-9110-blue)](https://datatracker.ietf.org/doc/rfc9110/)
[![Static Badge](https://img.shields.io/badge/RFC-9111-blue)](https://datatracker.ietf.org/doc/rfc9111/)
[![Static Badge](https://img.shields.io/badge/RFC-9112_HTTP/1.1-blue)](https://datatracker.ietf.org/doc/rfc9112/)
[![Static Badge](https://img.shields.io/badge/RFC-9113_HTTP/2-blue)](https://datatracker.ietf.org/doc/rfc9113/)
[![Static Badge](https://img.shields.io/badge/RFC-9114_HTTP/3-blue)](https://datatracker.ietf.org/doc/rfc9114/)
[![Static Badge](https://img.shields.io/badge/RFC-9204-blue)](https://datatracker.ietf.org/doc/rfc9204/)
[![Static Badge](https://img.shields.io/badge/RFC-9218-blue)](https://datatracker.ietf.org/doc/rfc9218/)

---
# Summary
1. [Definition](#definition)
2. [Requests](#requests)
3. [Status codes](#status-codes)
4. [Responses](#responses)

---
# Definition
> **HyperText Transfer Protocol (HTTP)**  
> **Application layer protocol** that specifies how to transmit data over the Internet.
> HTTP is a **request-response model** using a client-server architecture

**Key characteristics**
 - Stateless protocol
 - Supports multiple versions: HTTP/1.1, HTTP/2, HTTP/3 (see below)

**HTTP versions**
	**HTTP/1.1** : pipelining (asynchronous requests)
	**HTTP/2** : multiplexing and header compression (HPACK)
	**HTTP/3** : QUIC support (UDP-based)

**Note**
 - All example provided in this page can be found it the associated `pcap` file:
[![Static Badge](https://img.shields.io/badge/Download-pcap_file-blue?logo=wireshark&logoColor=blue)](https://raw.githubusercontent.com/cos-imo/Notes/refs/heads/main/src/Network/Protocols/HTTP/http_request_response.pcap)   
 - This capture was generate using [this Python script](https://github.com/cos-imo/Notes/blob/main/src/Network/Protocols/HTTP/generate_http_request_response.py) leveraging the [scapy library](https://scapy.net/).  

---

# Requests

## Request definition
A request is sent by a client to a server.  
The start line includes a method name, a request URI and the protocol version with a single space between each field. The following request start line specifies method `GET`, URI `/page` and protocol version `HTTP/1.1`:

```HTTP
GET /page HTTP/1.1
```

Requests can pass additional information using  [Request header fields](./HTTP%20request%20header%20fields.md). 

## Example request

Below is an example request to `example.com`.   

```HTTP
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/1.0
Accept: text/html
Connection: keep-alive


```

*Note*: There are **two blank lines** at the end of the request, marking the end of the request.  
The subsequent response can be found in the [response](#example-response) section.

## Requests methods

| Method      | RFC                                                   | Safe | Cacheable |
| ----------- | ----------------------------------------------------- | ---- | --------- |
| **GET**     | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | Yes  | Yes       |
| **POST**    | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | No   | Yes       |
| **PUT**     | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | No   | No        |
| **HEAD**    | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | Yes  | Yes       |
| **DELETE**  | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | No   | No        |
| **CONNECT** | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | No   | No        |
| **OPTIONS** | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | Yes  | No        |
| **TRACE**   | [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/) | Yes  | No        |
| **PATCH**   | [RFC 5789](https://datatracker.ietf.org/doc/rfc5789/) | No   | No        |
*Notes*:
 - A request is said **safe** if it does not modify server state.  
 - A request is **cacheable** if its response may be stored by the server for future reuse.  

---
# Status codes

| Class   | Description                                     |
| ------- | ----------------------------------------------- |
| **1XX** | Informational - Request received and continuing |
| **2XX** | Successful - Request accepted and processed     |
| **3XX** | Redirection - Further action required           |
| **4XX** | Client Error - Request contains error           |
| **5XX** | Server Error - Server failed to process request |

---
# Responses

## Definition

A **response** is sent by the server to the client.  

The start line contains:
 - **Protocol version**
 - **Status code**
 - **Reason phrase** (optional) 
 
 **Example start line**:

```HTTP
HTTP/1.1 200 OK
```

Responses may include additional [response header fields](./HTTP%20response%20header%20fields.md)

## Example Response

Below is the response from the request from [previous section](#example-request)

```HTTP
HTTP/1.1 200 OK
Date: Sat, 01 Jan 1970 00:00:00 GMT

Content-Type: text/html
Content-Length: 48
Connection: keep-alive

<html>
<head><title>Example</title></head>
<body>Test Page</body>
</html>
```

---
# Security considerations
HTTP is generally secured through **TLS**, resulting in **HTTPS**. Other security considerations are to be bear in mind:
 - **Never trust user input**
 - **Methods Enforcement** - Restrict or disable **unsafe methods** (cf. [request methods](#request-methods))
 - **Security Headers** - Implement headers such as `Strict-Transport Security` (enforces HTTPS-only), `X-Frame-Options`, `Content-Security-Policy` (enforces CSP) and `X-Content-Type-Options` (also see the [dedicated headers page])
 - **Response Header Validation** - Ensure headers do not leak sensitive informations (e.g., server software and version)
 - **IP and Header Spoofing Mitigation** - Validate incoming headers (cf. furnished [OWASP article](https://owasp.org/www-community/pages/attacks/ip_spoofing_via_http_headers))

[![Static Badge](https://img.shields.io/badge/OWASP-HTTP_Testing-orange?logo=owasp)](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/06-Test_HTTP_Methods)  
[![Static Badge](https://img.shields.io/badge/OWASP-HTTP_Security_Response_Headers_CheatSheet-orange?logo=owasp)](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)  
[![Static Badge](https://img.shields.io/badge/OWASP-Secure_Headers_Project-orange?logo=owasp)](https://owasp.org/www-project-secure-headers/)  
[![Static Badge](https://img.shields.io/badge/OWASP-Security_Headers-orange?logo=owasp)](https://owasp.org/www-community/Security_Headers)  
[![Static Badge](https://img.shields.io/badge/OWASP-IP_Spoofing_via_Security_Headers-orange?logo=owasp)](https://owasp.org/www-community/pages/attacks/ip_spoofing_via_http_headers)  
[![Static Badge](https://img.shields.io/badge/MITTRE-Application_Layer_Protocol:_Web_Protocols-blue)](https://attack.mitre.org/techniques/T1557/002/)  
