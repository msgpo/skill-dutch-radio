﻿#import requests
import csv

from collections import OrderedDict

class Channel():
    def __init__(self, name=None, id=None, stream_url=None):
        self.name = name
        self.id = id
        self.stream_url = stream_url


class DutchRadio():
    def __init__(self):
        indx = 0
        r = open('/opt/mycroft/skills/DutchRadio/radio.csv', 'r')
        reader = csv.reader(r, delimiter=',')
        channellist = list(reader)
        #Found ' + str(len(channellist)) + 'channels.
        #self.speak_dialog(' Starting ' + channellist[0][0])
        #Media = Instance.media_new(channellist[0][1].strip())
        self.channels = {}
        if r:
            for c in channellist:
                name =  channellist[indx][0].strip()
                id = indx
                stream_url = channellist[indx][1].strip()
                self.channels[name] = Channel(name, id, stream_url)
                indx += 1 

    def __contains__(self, channel):
        return channel in self.channels

    def get_next(current):
        keys = channels.keys()
        pos = 0
        for k in keys:
            if k == current:
                break
            pos += 1
        if pos < len(keys):
            return self.channels(keys[pos])