"""
-------------------------------------------------------------------------------
Name:       Webpingi
Purpose:    performs a dns and urlopen with measuring timings
Author:     Matthias Maier
Created:    27/03/2020
Updated:    27/03/2020
Copyright:  Splunk
Usage: python webpingi.py NAME URL
Note:
 URL fromat has to be like: http://www.google.de 
-------------------------------------------------------------------------------
"""

# module imports

import sys
import re
import urllib2
import time
import socket
from urllib import urlopen

from time import strftime
from string import Template
urlparse = urllib2.urlparse.urlparse

name = sys.argv[1]
url = sys.argv[2]

def test_connection(name, url, timeout=10):
    """Simple connection test"""
    urlinfo = urlparse(url)
    start = time.time()
    try:
        ip = socket.gethostbyname(urlinfo.netloc)
    except Exception as e:
        print('Error resolving DNS for {}: {}, {}'.format(name, url, e))
        return
    dns_elapsed = time.time() - start
    start = time.time()
    try:
        _ = urlopen(url)
    except Exception as e:
        print("Error open {}: {}, {}, DNS finished in {} sec.".format(name, url, e, dns_elapsed))
        return
    load_elapsed = time.time() - start
# Output Format for Standalone usage
    print("{} Timing for {}: {}, DNS: {:.4f} sec, LOAD: {:.4f} sec.".format(time.ctime(),name, url, dns_elapsed, load_elapsed)) 

# Output Format to be in sync and work with the out of the box dashboards of the Splunk Network Toolkit Uptime Monitoring Dashboard
   # print("{} sent=1 received=1 packet_loss=0 min_ping={:.3f} avg_ping={:.3f} max_ping={:.3f} jitter=0.000 return_code=0 dest={} DNSLoad={:.3f}".format(time.ctime(),load_elapsed,load_elapsed,load_elapsed,url,dns_elapsed))


if __name__ == '__main__':
    test_connection (name,url)
