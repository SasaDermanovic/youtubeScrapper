import requests
from bs4 import BeautifulSoup
import collections, operator
def returnBase(string):
    base = {'K': pow(10,3), 'M': pow(10,6), 'B': pow(10,9)}
    if string[-1]in base:
        return float(string[:-1]) * base[string[-1]]
    else:
        return float(string)

def youtubeChannel(channel_url, sub_var, chan_var):
  page = requests.get(channel_url)
  #open("video.html", "w", encoding='utf8').write(page.text) 
  soup = BeautifulSoup(page.text, "html.parser")
  follow_sum = soup.findAll("span", {"class": sub_var})
  channel_name = soup.find("span", {"class": chan_var}).find("a").text
  for c in follow_sum:
      followers = int(returnBase(c.get_text().replace(",", "")))
  return channel_name, followers

def main():
  sub_var = "yt-subscription-button-subscriber-count-branded-horizontal" 
  "subscribed yt-uix-tooltip"
  chan_var = "qualified-channel-title-wrapper"
  with open("alternative_media.txt") as f:
      content = f.readlines()
  media_outlets = [x.rstrip() for x in content] 
  channels = []
  for a in media_outlets:
    channel_name, followers = youtubeChannel(a, sub_var, chan_var)
    channels.append((channel_name, followers))
  
  filename = "top_channels.txt"
  myfile = open(filename, 'w')

  for key,value in sorted(channels,key=operator.itemgetter(1),reverse = True):
    myfile.write('{}: {} pretplatnika\n'.format(key, value)) 
  
  myfile.close()
if __name__== "__main__":
  main()