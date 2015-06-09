import urllib.request
import sqlite3
from bs4 import BeautifulSoup

conn = sqlite3.connect('weather.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS locations (id INTEGER PRIMARY KEY, code TEXT, name TEXT)')

for country in ['ca', 'us', 'intl']:
    locations_request = urllib.request.urlopen('http://www.theweathernetwork.com/weather/list/' + country + '/all')
    soup = BeautifulSoup(locations_request.read().decode('unicode_escape'))
    location_container = soup.find(id='all-index')
    locations = location_container.find_all('a')
    for location in locations:
        code = location['href']
        code = code.replace('/weather/','')
        cur.execute('INSERT INTO locations (code, name) VALUES ((?), (?))', (code, location.text))

conn.commit()
cur.close()
conn.close()
