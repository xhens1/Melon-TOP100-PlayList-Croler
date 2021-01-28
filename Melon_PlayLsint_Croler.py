import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class Music:
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        self.req = requests.get('https://www.melon.com/chart/week/index.htm', headers=self.header)
        self.html = self.req.text
        self.parse = BeautifulSoup(self.html, 'html.parser')

    def MelonTop100(self):
        RANK = 100
        titles = self.parse.find_all("div", {"class": "ellipsis rank01"})
        singers = self.parse.find_all("div", {"class": "ellipsis rank02"})

        title = []
        singer = []
        Result = []

        for tData in titles:
            title.append(tData.find('a').text)

        for sData in singers:
            singer.append(sData.find('span', {"class": "checkEllipsis"}).text)

        for i in range(RANK):
            print('%3d위: %s - %s' % (i + 1, title[i], singer[i]))

        return title

    

if __name__ == '__main__':
    Mp3_Download_Path = 'Download'
    MusicCrol = Music()
    MusicCrol_List = MusicCrol.MelonTop100()
