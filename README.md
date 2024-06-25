# spose.py
Spose is a python tool for scanning open ports behind a Squid proxy. It uses the requests library to perform HTTP requests on specified ports and checks for common HTTP response codes. Simply provide the target IP and proxy address via command line arguments to start scanning.

# USAGE 

python3 spose.py --proxy http://target-ip:3128 --target 127.0.0.1
