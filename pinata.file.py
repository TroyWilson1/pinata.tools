#!/usr/bin/env python3
#
#

import os
import ast
import argparse
import subprocess
import requests

# Fetch Key & PWD 
pinata_api_key = subprocess.check_output(["gpg2", "-q", "--for-your-eyes-only", "--no-tty", "--batch", "-d", "/Users/troywilson/testing/pinata/pinata.api.key.gpg"])
pinata_api_key = pinata_api_key.strip()
pinata_secret_api_key = subprocess.check_output(["gpg2", "-q", "--for-your-eyes-only", "--no-tty", "--batch", "-d", "/Users/troywilson/testing/pinata/pinata.api.secret.api.key.gpg"])
pinata_secret_api_key = pinata_secret_api_key.strip()


# Parse command arguments
parser = argparse.ArgumentParser(description='Copy file to Pinata.Cloud')
parser.add_argument('-i', '--input', help='File to add to Pinata.Cloud', required=True)
parser.add_argument('-n', '--name', help='Name of file added to Pinata.Cloud', required=True)
args = parser.parse_args()

url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
file_to_pin = (os.path.abspath(args.input))
file_name = (args.name)

headers = {'pinata_api_key': pinata_api_key,
           'pinata_secret_api_key': pinata_secret_api_key}

payload = {'file': (file_name, open(file_to_pin, 'rb'))}

try: 
    r = requests.post(url, headers=headers, files=payload)
    full_response = ast.literal_eval(r.text)
    print("File Pinata pinned file to: " + full_response['IpfsHash'])
    print("File Name: " + file_name)
    print("Success!")
    
except:
    print("Didn't work! Error!")
    
