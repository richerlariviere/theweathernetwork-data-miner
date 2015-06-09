import urllib.request
import sqlite3

city_code = 'caqc0123' # Hardcoded

weather_request = urllib.request.urlopen('http://www.theweathernetwork.com/api/data/' + city_code)

conn = sqlite3.connect('weather.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS jsondata (id INTEGER PRIMARY KEY, path TEXT)')

json_string = weather_request.read().decode('unicode_escape')
cur.execute('INSERT INTO jsondata (path) VALUES (?)', (json_string,))

conn.commit()
cur.close()
conn.close()
