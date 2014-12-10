#!/usr/bin/env python
# Convert a HAR entry to a `curl` command -- super convenient for all kinds of web-hacking :)

import sys
import json
import urllib

f = open(sys.argv[1])
data = json.load(f)
opts = {}
opts['url'] = data['request']['url']
opts['cookies'] = urllib.urlencode([(cookie['name'], cookie['value']) for cookie in data['request']['cookies']])
opts['http0'] = '-0' if data['request']['httpVersion'] == 'HTTP/1.0' else ''
opts['method'] = data['request']['method']
opts['headers'] = ' '.join(['-H "' + x['name'] + ': ' + x['value'] + '"' for x in data['request']['headers']])
if 'postData' in data['request']:
    opts['postData'] = data['request']['postData']['text']
else:
    opts['postData'] = ''

print 'curl -X {method} {http0} -b "{cookies}" {headers} -d "{postData}" {url}'.format(**opts)




def process_har(data):

    opts = {}
    opts['method'] = data['request']['method']
    opts['url'] = data['request']['url']
    #opts['url'] = data.get('request',{}).get('url')

    ar = []
    for cookie in data['request']['cookies']:
        ar.append((cookie['name'], cookie['value']))
    opts['cookies'] = urllib.urlencode(ar) 

    if data['request']['httpVersion'] == 'HTTP/1.0':
        opts['http0'] = '-0'
    else:
        opts['http0'] = ''

    ar = []
    for x in data['request']['headers']:
        ar.append('-H "{0}: {1}"'.format(x['name'],x['value']))
    opts['headers'] = ' '.join(ar)
    
    if 'postData' in data['request']:
        opts['postData'] = data['request']['postData']['text']
    else:
        opts['postData'] = ''

    print 'curl -X {method} {http0} -b "{cookies}" {headers} -d "{postData}" {url}'.format(**opts)


process_har(data)
