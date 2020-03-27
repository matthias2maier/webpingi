# WebPingi
Splunk Technical Add-on based on Python opening a URL and measure the performance

## Why WebPingi?
Many providers from Cloud SAAS applications have disabled ICMP responses aka ping's. To identify availability and measure response times of any kind of webservice or website WebPingi was created. For example you can deploy WebPingi via a Splunk Heavy Forwarder to all your remote workers laptops to track and monitor  user experience with your cloud services in use accross different regions. 

## What is it doing?
WebPingi allows you to query a webservice and get the DNS & PageLoad. 
Example Output:
> Fri Mar 27 18:00:28 2020 Timing for Service=Okta URL=http://******.okta.com, DNS=0.0019 LOAD=1.1158

## What does it use?
WebPingi uses for DNS urllib and urllib2. The "gethostbyname" python functionality ist used for DNS response time and for the page load "urlopen" is used.

## How to use it Standalone?

> python webpingi.py <Name> <HTTP URL>

Example: 
>python webpingi.py SplunkAnswers https://answers.splunk.com

Response:
> Fri Mar 27 17:09:01 2020 Timing for Service=SplunkAnswers URL=https://answers.splunk.com, DNS=3.0613 LOAD=8.2720

## How can i use it with Splunk?
1. Download the Git Repository and put it into /etc/apps/ of your Splunk Heavy Forwarder
2. Configure inputs.conf - for every SAAS Service you want to monitor you create a copy and adjust the parameters of Name & URL. Via interval you can control how often it is queried.
3. Save it and restart your Splunk Heavy Forwarder

![Table Showing Response Times from an endpoint](https://github.com/matthias2maier/webpingi/blob/master/Screenshots/Screenshot_WebPingi_table.png?raw=true)

![Timechard showing average, minimum and maximum response times binned to 3m per reporting endpoint](https://github.com/matthias2maier/webpingi/blob/master/Screenshots/Screenshot_WebPingi_timechart_avg_max_min.png?raw=true)

## Why only Splunk Heavy Forwarder and not the Splunk Universal Forwarder?
The Splunk Universal Forwarder is lightwight and does not come with python. It's possible to [create wrapper script](https://sublimerobots.com/2017/01/simple-splunk-scripted-input-example/) so that within an Universal Forwarder the python script is executed with the machine's local python library which has to be installed. This was not yet tested. 

## How can I map it into the Network Toolkit Splunk App?
To align with the PING Logs the webpingi.py file allows you to change the output format. Go into the file before you copy it to the heavy forwarder and swap out the output where it is flagged in the comments. Output will then look like that:
> Fri Mar 27 17:07:29 2020 sent=1 received=1 packet_loss=0 min_ping=4.683 avg_ping=4.683 max_ping=4.683 jitter=0.000 return_code=0 dest=https://answers.splunk.com DNSLoad=0.027

Dashboard adjustments should be easy with adding the sourcetype early on and splitting by host to display from which host the performance is measured from.

![Status Overview with WebPingi](https://github.com/matthias2maier/webpingi/blob/master/Screenshots/Screenshot%20WebPingi%20Network%20Toolkit-1.png?raw=true)

Next up: 
* Wrapper Script to run on Splunk Universal Forwarders
* Implement a lookup table to for easier maintaining the set of URLs to query
