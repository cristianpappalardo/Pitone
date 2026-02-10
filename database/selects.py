import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('''
SELECT Artists.name, Albums.title, Tracks.title, Tracks.plays
FROM Artists
JOIN Albums ON Artists.id = Albums.artist_id
JOIN Tracks ON Albums.id = Tracks.album_id
''')
for row in cur:
    print(row)
	
	
cur.close()