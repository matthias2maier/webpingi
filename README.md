# WebPingi
Splunk Technical Add-on based on Python opening a URL and measure the performance

## Why WebPingi?
Many providers from Cloud SAAS applications have disabled ICMP responses aka ping's. To identify availability and measure response times of any kind of webservice or website WebPingi was created. For example you can deploy WebPingi via a Splunk Heavy Forwarder to all your remote workers laptops to track and monitor their experience with your cloud services in use accross different regions. 

## What is it doing?
WebPingi allows you to query a webservice and get the DNS & PageLoad. 
Example Output:
> Fri Mar 27 17:01:37 2020 Timing for Okta: http://splunk.okta.com, DNS: 0.0034 sec, LOAD: 1.2280 sec.

## What does it use?
WebPingi uses for DNS urllib and urllib2. The "gethostbyname" python functionality ist used for DNS response time and for the page load "urlopen" is used.

## How to use it Standalone?

> python webpingi.py <Name> <HTTP URL>

Example: 
>python webpingi.py SplunkAnswers https://answers.splunk.com

Response:
> Fri Mar 27 17:09:01 2020 Timing for SplunkAnswers: https://answers.splunk.com, DNS: 3.0613 sec, LOAD: 8.2720 sec.

## How can i use it with Splunk?
1. Download the Git Repository and put it into /etc/apps/ of your Splunk Heavy Forwarder
2. Configure inputs.conf - for every SAAS Service you want to monitor you create a copy and adjust the parameters of Name & URL. Via interval you can control how often it is queried.
3. Save it and restart your Splunk Heavy Forwarder

## Why only Splunk Heavy Forwarder and not the Splunk Universal Forwarder?
The Splunk Universal Forwarder is lightwight and does not come with python. It's possible to [create wrapper script](https://sublimerobots.com/2017/01/simple-splunk-scripted-input-example/) so that within an Universal Forwarder the python script is executed with the machine's local python library which has to be installed. This was not yet tested. 
