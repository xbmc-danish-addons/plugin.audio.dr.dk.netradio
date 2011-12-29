import os
import sys
import simplejson
import urllib2
import buggalo

import xbmcaddon
import xbmcgui
import xbmcplugin

CHANNELS_URL = 'http://www.dr.dk/LiveNetRadio/datafeed/channels.js.drxml'

def showChannels():
    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    u.close()

    channels = simplejson.loads(data[39:-3])
    path = ADDON.getAddonInfo('path')
    for channel in channels:
        if channel.has_key('source_url'):
            item = xbmcgui.ListItem(channel['title'], iconImage = os.path.join(path, 'resources', 'logos', channel['source_url'] + '.png'))
        else:
            item = xbmcgui.ListItem(channel['title'], iconImage = channel['logo'])

        item.setProperty('IsPlayable', 'true')
        item.setInfo(type = 'audio', infoLabels = {
                'title' : channel['title']
        })

        if type(channel['mediaFile']) is list:
            url = channel['mediaFile'][0]
        else:
            url = channel['mediaFile']
        xbmcplugin.addDirectoryItem(HANDLE, url + ' live=1', item)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    HANDLE = int(sys.argv[1])
    try:
        showChannels()
    except Exception:
        buggalo.onExceptionRaised()

