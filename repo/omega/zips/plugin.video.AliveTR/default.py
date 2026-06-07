import sys
import xbmcaddon
import os
import requests
import xbmc
import xbmcgui
import urllib.parse  # Changed to urllib.parse for Python 3 compatibility
import re
import xbmcplugin


def CATEGORIES():
    addDir3('LIVE TV', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/livetvtr.txt', 3, 'https://images.sftcdn.net/images/t_app-icon-m/p/20b72a35-d299-417f-9b4b-e2f2fefb12f0/4074394849/greek-tv-live-logo', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCPBtz0mRTx8qvMGUfWLk4Rvm-R5J0f48G-A&s', '')
    addDir3('KEMAL SUNAL', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/KemalSunal.txt', 4, 'https://renk-magazin.de/wp-content/uploads/Kemal_Sunal-1.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCPBtz0mRTx8qvMGUfWLk4Rvm-R5J0f48G-A&s', '')
    addDir3('BOLLYWOOD', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Bollywood%20Film%20Izle%20T%C3%BCrk%20Dublaj.txt', 5, 'https://img.kitapyurdu.com/v1/getImage/fn:1134980/wh:true/wi:500', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCPBtz0mRTx8qvMGUfWLk4Rvm-R5J0f48G-A&s', '')
    addDir3('BOLLYWOODSERIALS', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Bollywood%20Serials.txt', 6, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIOZuXa0W94ROCKuD1yKURzYTrYiR2-7nZfw&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCPBtz0mRTx8qvMGUfWLk4Rvm-R5J0f48G-A&s', '')

def channel():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/livetvtr.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')
        

def KEMALSUNAL():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/KemalSunal.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')

        
        
def BOLLYWOOD():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Bollywood%20Film%20Izle%20T%C3%BCrk%20Dublaj.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')

def BOLLYWOODSERIALS():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Bollywood%20Serials.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')              

def addLink(name, url, image, urlType, fanart):
    liz = xbmcgui.ListItem(name)
    liz.setArt({'thumb': image})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty('IsPlayable', 'true')
    liz.setProperty('fanart_image', fanart)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz)

def get_params():
    param = {}
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        cleanedparams = paramstring.replace('?', '')
        if paramstring[-1] == '/':
            paramstring = paramstring[:-2]
        pairsofparams = cleanedparams.split('&')
        for pair in pairsofparams:
            splitparams = pair.split('=')
            if len(splitparams) == 2:
                param[splitparams[0]] = splitparams[1]
    return param

def addDir(name, url, mode, label, fanart, description):
    u = sys.argv[0] + "?url=" + urllib.parse.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.parse.quote_plus(name)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'thumb': label, 'icon': 'DefaultFolder.png'})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)

def addDir2(name, url, mode, label, fanart, description):
    u = sys.argv[0] + "?url=" + urllib.parse.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.parse.quote_plus(name)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'thumb': label, 'icon': 'DefaultFolder.png'})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)

def addDir3(name, url, mode, label, fanart, description):
    u = sys.argv[0] + "?url=" + urllib.parse.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.parse.quote_plus(name) + "&iconimage=" + urllib.parse.quote_plus(label) + "&fanart=" + urllib.parse.quote_plus(fanart) + "&description=" + urllib.parse.quote_plus(description)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'thumb': label, 'icon': 'DefaultFolder.png'})
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    liz.setProperty("Fanart_Image", fanart)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view') == 'true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType)

params = get_params()
url = params.get("url", None)
name = params.get("name", None)
label = params.get("label", None)
mode = int(params.get("mode", 0))  # Default to 0 if not present
fanart = params.get("fanart", None)
description = params.get("description", None)

print("Mode: " + str(mode))
print("URL: " + str(url))
print("Name: " + str(name))

if mode is None or url is None or len(url) < 1:
    
    print("")
    CATEGORIES()
elif mode == 1:
    OPEN_URL(url)  # Ensure OPEN_URL is defined elsewhere
elif mode == 3:
    channel()
elif mode == 4:
    KEMALSUNAL()
elif mode == 5:
    BOLLYWOOD()
elif mode == 6:
    BOLLYWOODSERIALS()       

xbmcplugin.endOfDirectory(int(sys.argv[1]))