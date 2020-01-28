import requests
from bs4 import BeautifulSoup
import collections
def returnBase(string):
    base = {'K': pow(10,3), 'M': pow(10,6), 'B': pow(10,9)}
    if string[-1]in base:
        return float(string[:-1]) * base[string[-1]]
    else:
        return float(string)

def youtubeChannel(channel_url, sub_var, chan_var):
  page = requests.get(channel_url)
  #open("video.html", "w", encoding='utf8').write(page.text) 
  space = " "
  soup = BeautifulSoup(page.text, "html.parser")
  follow_sum = soup.findAll("span", {"class": sub_var})
  channel_name = soup.find("span", {"class": chan_var}).find("a").text
  for c in follow_sum:
      followers = int(returnBase(c.get_text().replace(",", "")))
      #print(channel_name + space + str(follow_count))
  fetched_data ={channel_name:followers}
  
  #print( food_list.sort(reverse=True))
  #print(min(released.values()))
      #i = collections.OrderedDict(sorted(released.items(), key=lambda t: t[0]))
      #print(i)

  #a1 = sorted(released.items(),key=operator.itemgetter(1),reverse=True)
  #print(a1)

  

def main():
  sub_var = "yt-subscription-button-subscriber-count-branded-horizontal" 
  "subscribed yt-uix-tooltip"
  chan_var = "qualified-channel-title-wrapper"
  with open("alternative_media.txt") as f:
      content = f.readlines()
  media_outlets = [x.rstrip() for x in content] 
  for a in media_outlets:
    youtubeChannel(a, sub_var, chan_var)
  

if __name__== "__main__":
  main()