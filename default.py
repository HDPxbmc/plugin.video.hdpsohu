# -*- coding: utf-8 -*-
# default.py
# HDPfans sohu

import urllib,urllib2,re,xbmcplugin,xbmcgui,subprocess,sys,os,os.path,xbmcaddon


# Plugin constants 
__addonid__ = "plugin.video.hdpsohu"
__addon__ = xbmcaddon.Addon(id=__addonid__)
__cwd__ = __addon__.getAddonInfo('path')
__resource__  = xbmc.translatePath( os.path.join( __cwd__, 'lib' ) )
sys.path.append (__resource__)
import hdplib

def playVideo(url):
	mylist = hdplib.GetHttpData(url)
	foobars = re.compile('<m3u8>(.*?)</m3u8>', re.DOTALL).findall(mylist)
	playlist = xbmc.PlayList(1)
	playlist.clear()
	for i in range(0,len(foobars)):
		title =" µÚ"+str(i+1)+"/"+str(len(foobars))+"½Ú"
		listitem=xbmcgui.ListItem(title)
		listitem.setInfo(type="Video",infoLabels={"Title":title})
		playlist.add(foobars[i], listitem)
	xbmc.Player().play(playlist)

params = hdplib.get_params()
mode = None
url = None
page = None
type = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	page = int(params["page"])
except:
	pass
try:
	type = int(params["type"])
except:
	pass

if mode == None:
	hdplib.buildRoot()
elif mode == 1:
	hdplib.buildLists(url,page,type)
elif mode == 2:
	hdplib.buildSeries(url)
elif mode == 3:
	playVideo(url)
elif mode == 5:
	hdplib.performChange(type)
	
