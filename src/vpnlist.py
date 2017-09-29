#!/usr/bin/env python

import os
import base64
import requests

path = os.path.join(os.path.expanduser('~'), '.openvpn')


def main():
    links = [x.split(',') for i,x in enumerate(requests.get(http://www.vpngate.net/api/iphone').text.split('\r\n')) if i>= 2]
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    for src in links:
        try:
            if (src[5] != 'Russia Federation' and src[6] != 'RU') and (src[5] != 'Ukraine' and src[6] != 'UA'):
                f = open(os.path.join(path, '{}-{}.ovpn'.format(src[0],src[6])), 'wb+')
                f.write(base64.b64decode(src[14]))
                f.close()
            except IndexError:
                pass
               
if __name__ == "__main__":
    main()
print('Done!')
