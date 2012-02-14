CHANNELS = list()

class Channel(object):
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

        CHANNELS.append(self)


Channel(1, 'Specific Radio', 'shout://stream.specific.dk/SR')
Channel(2, 'Specific Mainstram Radio', 'shout://stream.specific.dk/MS')

Channel(3, 'The Voice', 'shout://195.184.101.203/voice128')

Channel(4, 'Radio 100', 'shout://onair.100fmlive.dk/100fm_live.mp3')
Channel(5, 'Radio 100 Soft', 'shout://onair.100fmlive.dk/soft_live.mp3')
Channel(6, 'Radio 100 Klassisk', 'shout://onair.100fmlive.dk/klassisk_live.mp3')

Channel(7, 'Nova FM', 'shout://195.184.101.204/nova128')

Channel(8, 'Radio24syv', 'rtmp://fl1.sz.xlcdn.com/live/sz=Radio24syv=ENC1_Web256 live=1')

Channel(9, 'Pop FM','shout://195.184.101.202/pop128')

Channel(10, 'Radio VLR', 'shout://streaming.fynskemedier.dk/vlr')

