
"""
Description : get news feed from choosen contries from Google news feed
By SinisterJK : https://github.com/tongjk

This code for education only, not for commercial purpose!!!

Enjoy ur develop :)
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

country_name = 'thailand'

country_code = {'australia': 'AU',
                'Canada': 'CA',
                'India': 'IN',
                'Singapore': 'SG',
                'South Africa': 'ZA',
                'United Kingdom': 'GB',
                'United States': 'US',
                'thailand': 'TH',
                'Indonesia': 'ID',
                'Ireland': 'IE',
                'Israel': 'IL',
                'Kenya': 'KE',
                'Malaysia': 'MY',
                'New Zealand': 'NZ',
                'Philippines': 'PH',
                'Pakistan': 'PK',
                'Korea': 'KR',
                'Japan': 'JP',
                'Hok Kong': 'HK'}

short = country_code[country_name]

if short == 'TH':
    language = 'th'

elif short == 'KR':
    language = 'ko'

elif short == 'HK':
    language = 'zh'

elif short == 'JP':
    language = 'ja'

else:
    language = 'en'

news_url = 'https://news.google.com/rss?hl=' + f'{language}-{short}&gl={short}&ceid={short}:{language}'

print('Hot news in ', country_name, f'({short})')
print('From : ', news_url.replace('rss', ''), '\n\n')

Client = urlopen(news_url)
xml_page = Client.read().decode('UTF-8')
Client.close()

soup_page = soup(xml_page, "lxml")
news_list = soup_page.findAll("item")

for news in news_list:
    print("-" * 100)
    print('Title : ', news.title.text)
    print('Link : ', str(news).split('<link/>')[1].split('<')[0])
    print('Date : ', news.pubdate.text)
    print('\n')
