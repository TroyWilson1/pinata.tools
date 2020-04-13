#!/usr/bin/env python3
# Takes a IPFS hash and tries to pin it to Pinata.Cloud
# if it does not work then it adds the hash to the Pinata.Cloud
# pinning queue for pinning later. 
#
import requests
import ast
import argparse
import subprocess


pinata_api_key = subprocess.check_output(["gpg2", "-q", "--for-your-eyes-only", "--no-tty", "--batch", "-d", "/Users/troywilson/testing/pinata/pinata.api.key.gpg"])
pinata_api_key = pinata_api_key.strip()
pinata_secret_api_key = subprocess.check_output(["gpg2", "-q", "--for-your-eyes-only", "--no-tty", "--batch", "-d", "/Users/troywilson/testing/pinata/pinata.api.secret.api.key.\
gpg"])
pinata_secret_api_key = pinata_secret_api_key.strip()


# Parse command arguments
parser = argparse.ArgumentParser(description='Copy Hash to Pinata.Cloud')
parser.add_argument('-i','--input', help='Hash to add to Pinata.Cloud', required=True)
parser.add_argument('-n','--name', help='Name of hash added to Pinata.Cloud', required=True)
args = parser.parse_args()

url = 'https://api.pinata.cloud/pinning/pinHashToIPFS'
hashToPin = (args.input)
hashName = (args.name)

headers = {'pinata_api_key': pinata_api_key,
           'pinata_secret_api_key': pinata_secret_api_key}

body = {
    'hashToPin': hashToPin,
    'pinataMetadata': {
        'name': hashName
    }
}

try: 
    url = 'https://api.pinata.cloud/pinning/addHashToPinQueue'
    r = requests.post(url, headers=headers, json=body)
    fullResponce = ast.literal_eval(r.text)
    print("Pinata Hash Pinned: " + fullResponce['IpfsHash'])
    print("File Name: " + hashName)
    print("Success!")
    
except:
    print("Didn't work! Error!")

