from scapy.all import Ether, IP, TCP, Raw, wrpcap

http_request_raw = b"""GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/1.0
Accept: text/html
Connection: keep-alive


"""

request_pkt = Ether(src="00:11:22:33:44:55", dst="66:77:88:99:AA:BB") / \
              IP(src="10.0.0.1", dst="10.0.0.2") / \
              TCP(sport=12345, dport=80, flags="PA") / \
              Raw(load=http_request_raw)

http_response_raw = b"""HTTP/1.1 200 OK
Date: Sat, 01 Jan 1970 00:00:00 GMT

Content-Type: text/html
Content-Length: 48
Connection: keep-alive

<html>
<head><title>Example</title></head>
<body>Test Page</body>
</html>
"""

response_pkt = Ether(src="66:77:88:99:AA:BB", dst="00:11:22:33:44:55") / \
               IP(src="10.0.0.2", dst="10.0.0.1") / \
               TCP(sport=80, dport=12345, flags="PA") / \
               Raw(load=http_response_raw)

wrpcap("http_request_response.pcap", [request_pkt, response_pkt])
