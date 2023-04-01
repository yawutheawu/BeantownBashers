from mutagen.mp3 import MP3

def getSong(x):
    try:
        audio = MP3(x)
    except:
        return "Not Found"
    musicLength = int(audio.info.length)
    if(musicLength % 3 == 0):
        pass;
    else:
        musicLength = int(3 * round(musicLength / 3)) + 3
    print(musicLength)
    return createMap(musicLength)

def createMap(len):
    map = []
    beats  = []
    keys = ["SPACE"]
    value = 3
    while(len >= value):
        beats.append(value)
        value += 3
    map.append(beats)
    map.append(keys)
    print(map)
    return map