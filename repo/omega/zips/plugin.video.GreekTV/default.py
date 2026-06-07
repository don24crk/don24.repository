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
    addDir3('LIVE TV', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/channels.txt', 3, 'https://images.sftcdn.net/images/t_app-icon-m/p/20b72a35-d299-417f-9b4b-e2f2fefb12f0/4074394849/greek-tv-live-logo', 'https://images4.alphacoders.com/755/thumb-1920-75518.jpg', '')
    addDir3('SEFLIX', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/seflix.txt', 4, 'https://sefflix.com/wp-content/uploads/2021/03/xLOGO_TRANSPARENT-1-300x113.png.pagespeed.ic.xOd0wGkcRY.png', 'https://images4.alphacoders.com/755/thumb-1920-75518.jpg', '')
    addDir3('GREEKMOVIES', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/GreekMovies.txt', 5, 'https://www.mesimvria.com/wp-content/uploads/logo-GreekMoviesx2-2.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkraYO5t__Ih8zHbGH3J--BKy6OW2HIC1Kfw&s', '')
    addDir3('SUPERMAMI', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Supermami.txt', 6, 'https://greek-movies.com/icon/ant1.jpg', 'https://greek-movies.com/icon/series/Supermammy2022.jpg', '')
    addDir3('JESUSMOVIES', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Ellinikes%20Tainies%20To%20Xristo.txt', 7, 'https://i.pinimg.com/474x/04/92/76/049276f7b9f248461f8e8dac5de55b3f.jpg', 'https://images4.alphacoders.com/755/thumb-1920-75518.jpg', '')
    addDir3('KIDSMOVIES', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Paidika.txt', 8, 'https://i.ytimg.com/vi/z6C0H4lXxtI/sddefault.jpg', 'https://images4.alphacoders.com/755/thumb-1920-75518.jpg', '')
    addDir3('ALIKIVOUGIOKLAKI', 'https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/AlikiVougioklakiTenies.txt', 9, 'https://m.media-amazon.com/images/I/51qym3NUWrL._AC_UF894,1000_QL80_.jpg', 'https://images4.alphacoders.com/755/thumb-1920-75518.jpg', '')


def channel():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/channels.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')
              
def SEFLIX():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/seflix.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')

        
        
def GREEKMOVIES():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/GreekMovies.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')

def SUPERMAMI():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Supermami.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')

def JESUSMOVIES():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Ellinikes%20Tainies%20To%20Xristo.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')


def KIDSMOVIES():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/Paidika.txt')
    match = re.compile(r'name= (.+?) url= "(.+?)" logo= "(.+?)"').findall(r.text)
    for name, link, logo in match:
        addLink(name, link, logo, '', '')

def ALIKIVOUGIOKLAKI():
    r = requests.get('https://raw.githubusercontent.com/don24crk/Don24crk-Repository/refs/heads/master/AlikiVougioklakiTenies.txt')
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
    SEFLIX()
elif mode == 5:
    GREEKMOVIES()
elif mode == 6:
    SUPERMAMI() 
elif mode == 7:
    JESUSMOVIES() 
elif mode == 8:
    KIDSMOVIES()
elif mode == 9:
    ALIKIVOUGIOKLAKI()    
    

xbmcplugin.endOfDirectory(int(sys.argv[1]))