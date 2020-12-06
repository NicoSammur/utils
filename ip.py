import socket
import urllib.request

host = socket.gethostname()
iip = socket.gethostbyname(host)
eip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(f"hostname: {host}")
print(f"ip lan  : {iip}") 
print(f"ip wan  : {eip}") 
