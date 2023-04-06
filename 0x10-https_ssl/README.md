0x10. HTTPS SSL

HTTPS and SSL have two main roles in secure communication on the internet:

Encryption: The first role of HTTPS SSL is to encrypt the data being sent between a web server and a client, such as a web browser. Encryption ensures that the data cannot be intercepted and read by unauthorized parties who may be snooping on the network. SSL (Secure Sockets Layer) is a protocol that uses public-key encryption to encrypt data as it travels between the web server and the client. SSL ensures that the data remains private and secure during transmission.

Authentication: The second role of HTTPS SSL is to authenticate the identity of the web server to the client, and vice versa. This is done using SSL certificates, which are issued by trusted third-party Certificate Authorities (CAs). The SSL certificate contains information about the identity of the website and the public key that is used for encryption. When a client connects to a website over HTTPS, the SSL certificate is sent from the web server to the client's browser, which verifies that the certificate is valid and issued by a trusted CA. This provides assurance to the user that they are communicating with the intended website and not an imposter or attacker trying to steal their information.

Tasks 📃
0. World wide web

0-world_wide_web: Bash script that displays information about subdomains on my configured servers.
Usage: ./0-world_wide_web <domain> <subdomain>
Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
If no subdomain parameter is passed, displays information about the subdomains www, lb-01, web-01 and web-02, in that order.
1. HAproxy SSL termination

1-haproxy_ssl_termination: HAproxy configuration file that accepts encrypted SSL traffic for the subdomain www. on TCP port 443.
2. No loophole in your website traffic

100-redirect_http_to_https: HAproxy configuration file that automatically redirects HTTP traffic to HTTPS.
