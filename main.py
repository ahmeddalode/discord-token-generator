from requests.sessions import session
import cli_ui
from requests.api import head

import requests
import json
import random
import base64
import time
import urllib3
import captchatools
import string
import colorama
import ctypes
import psutil
import inspect
import sys
import os
import subprocess

from captchatools import captcha_harvesters, exceptions
from requests_futures.sessions import FuturesSession
from threading import Thread
from time import sleep
from termcolor import cprint
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from pyfiglet import figlet_format
from twocaptcha import TwoCaptcha
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)









register_link = "https://discordapp.com/api/auth/register"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
PASSWORD = "3219442@4324hjfdx6"


with open('Config/config.json') as r:
	config = json.load(r)

captcha_api_key = config.get('CaptchaKey')
captchatype1 = config.get('CaptchaType')


API_KEY = f"{captcha_api_key}" # capmonster key
SITE_KEY = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"


def typewritter2(text):
    for x in text:
        print(f'{Fore.RED}' + x, end="")
        sys.stdout.flush()
        time.sleep(0.05)



def gen_email():
    new_mail = ""
    i = 0
    length = random.randint(10, 20)
    while(i < length):
        new_mail += random.choice(alphabet)
        i += 1

    return new_mail + "@gmail.com"


proxies1 = open('config/proxies.txt','r').read().splitlines()
proxies1 = [{'https':f'http://{proxy}'} for proxy in proxies1]

def Get_cap_Balance():
    session = FuturesSession()
    try:
        json = {
            "clientKey": API_KEY
        }
        r = session.post('https://api.capmonster.cloud/getBalance', json=json, ).result()
        if r.json()['errorId'] == 1:
            return 'error, information about it is in the errorCode property'
        if r.json()['errorId'] == 0:
            return r.json()['balance']
    except:
        pass


def Get_anti_Balance():
    session = FuturesSession()
    try:
        json = {
            "clientKey": API_KEY
        }
        r = session.post('https://api.anti-captcha.com/getBalance', json=json).result()
        if r.json()['errorId'] == 1:
            return 'error, information about it is in the errorCode property'
        if r.json()['errorId'] == 0:
            return r.json()['balance']
    except:
        pass


def Get_2cap_Balance():
    try:
        solverbal = TwoCaptcha(f'{API_KEY}')
        balance = solverbal.balance()
        return balance
    except:
        pass


def get_super_properties(os, browser, useragent, browser_version, os_version, client_build):
    return {
        "os": os,
        "browser": browser,
        "device": "",
        "browser_user_agent": useragent,
        "browser_version": browser_version,
        "os_version": os_version,
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": client_build,
        "client_event_source": None
    }


def get_user_agent():
    return ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")


def get_headers():
    return {
        'Host': 'discordapp.com',
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/json',
        'Referer': 'https://discordapp.com/register',
        'Origin': 'https://discordapp.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'user-agent': "",
        'X-Fingerprint': "",
        'X-Super-Properties': ''
    }


def get_user_agent():
    return ("Windows", "Firefox", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0", "54.0", "7")
   
   
proxies = open('config/proxies.txt','r').read().splitlines()
proxies = [{'https':f'http://{proxy}'} for proxy in proxies]

def register():
    # get balance
    if captchatype1 == 'capmonster':
        Title = f'SoloX Gen | Current Balance: {Get_cap_Balance()}'
    
    if captchatype1 == 'anticaptcha':
        Title = f'SoloX Gen | Current Balance: {Get_anti_Balance()}'

    if captchatype1 == '2captcha':
        Title = f'SoloX Gen | Current Balance: {Get_2cap_Balance()}'
    ctypes.windll.kernel32.SetConsoleTitleW(Title)
    headers = get_headers()
    proxy = random.choice(proxies)
    os, browser, headers['user-agent'], browserver, osvers = get_user_agent()
    r = requests.Session()
    fingerprint_json = requests.get("https://discordapp.com/api/v6/experiments",
                                    timeout=10, proxies = proxy, headers=get_headers() , verify=False).json()
    fingerprint = fingerprint_json["fingerprint"]
    xsuperprop = base64.b64encode(json.dumps(get_super_properties(
        os, browser, headers['user-agent'], browserver, osvers, 36127), separators=",:").encode()).decode()
    headers['X-Super-Properties'] = xsuperprop
    # print
    print('[+] Creating Account!')
    email = gen_email()
    letters1 = string.ascii_letters
    
    #if REALN == 'y':
      #  namesfile=open("config/usernames.txt","r").readlines()
       # username = random.choice(namesfile)
    #else:
       # username = 'join | gg/solox'

    realistic = '1'
    if realistic == '1':
        r=requests.get('https://story-shack-cdn-v2.glitch.me/generators/username-generator?')
        text = json.loads(r.text)
        pairs = text.items()
        for name, value in pairs:
           newname1 = (value)
           username = newname1["name"]
           print(username)
        
        input('pog: ')
    else:
        username = 'gg/twitch-followers' 

    if captchatype1 == 'capmonster':
        solver = captcha_harvesters(solving_site=1, api_key=f"{API_KEY}", sitekey=f"{SITE_KEY}", captcha_type="hcap", captcha_url="https://discord.com/register")
        recaptcha_answer = solver.get_token()
    
    if captchatype1 == 'anticaptcha':
        solver = captcha_harvesters(solving_site=2, api_key=f"{API_KEY}", sitekey=f"{SITE_KEY}", captcha_type="hcap", captcha_url="https://discord.com/register")
        recaptcha_answer = solver.get_token()

    if captchatype1 == '2captcha':
        solver = captcha_harvesters(solving_site=3, api_key=f"{API_KEY}", sitekey=f"{SITE_KEY}", captcha_type="hcap", captcha_url="https://discord.com/register")
        recaptcha_answer = solver.get_token()

    payload = {
        'fingerprint': fingerprint,
        'email': email,
        'username': username,
        'password': PASSWORD,
        'invite': f"{INVITE}",
        'captcha_key': recaptcha_answer,
        'consent': True,
        "date_of_birth": "2001-01-01",
        'gift_code_sku_id': None
    }
    response = r.post('https://discordapp.com/api/v6/auth/register',
                json=payload, proxies = proxy, headers=headers, timeout=15000, verify=False)
    if response.status_code == 429:
        print('[-] proxy has been ratelimited!')
        return False
    else:
        try:
            token = response.json()
            data = token['token']
            print(f'{Fore.RED}[+] Joined The Server: {username}')
            with open(f"output/tokens.txt", "a+") as f:
                f.write(str(data + '\n'))
                f.close()
        except:
            print('[-] Could not get token!')
    

def Task():
    register()


def title():
    os.system('cls')
    print("""
\x1b[31m███████  ██████  ██       ██████  ██████  ███████ ██    ██ 
██      ██    ██ ██      ██    ██ ██   ██ ██      ██    ██ 
███████ ██    ██ ██      ██    ██ ██   ██ █████   ██    ██ 
     ██ ██    ██ ██      ██    ██ ██   ██ ██       ██  ██  
███████  ██████  ███████  ██████  ██████  ███████   ████  \x1b[D  Discord Member Generator
    """)



if __name__ == "__main__":
    typewritter2('server invite code: ')
    INVITE = input('')
    typewritter2('real names? [y/n]: ')
    REALN = input()
    while True:
        Thread(target=Task).start()
        time.sleep(0.3)
    

