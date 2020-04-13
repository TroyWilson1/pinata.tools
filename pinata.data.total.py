#!/usr/bin/env python3
#
#
#

import requests
import subprocess
import math
import json

pinata_api_key = subprocess.check_output(["gpg2", "-q", "--for-your-eyes-only", "--no-tty", "--batch", "-d", "/Users/troywilson/testing/pinata/pinata.api.key.gpg"])
pinata_api_key = pinata_api_key.strip()
pinata_secret_api_key = subprocess.check_output(["gpg2", "-q", "--for-your-eyes-only", "--no-tty", "--batch", "-d", "/Users/troywilson/testing/pinata/pinata.api.secret.api.key.\
gpg"])
pinata_secret_api_key = pinata_secret_api_key.strip()

headers = {'pinata_api_key': pinata_api_key,
           'pinata_secret_api_key': pinata_secret_api_key}

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1000)))
   p = math.pow(1000, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

url = 'https://api.pinata.cloud/data/userPinnedDataTotal'
response = requests.get(url, headers=headers)
data_dict = json.loads(response.text)
pst = int(data_dict['pin_size_total'])
total_size_convert = convert_size(pst)
pin_count = str(data_dict['pin_count'])
pswrt = int(data_dict['pin_size_with_replications_total'])
pin_size_with_replications_total_convert = convert_size(pswrt)

print("Pinata Total Pins: " + pin_count)
print("Pinata Space Used: " + total_size_convert)
print("Pinata Pin Size with Replications: " + pin_size_with_replications_total_convert) 



