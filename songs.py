from requests_html import HTMLSession

def main():
    url = 'https://acharts.co/us_singles_top_100'
    session = HTMLSession()
    req = session.get(url)
    table = req.html.find('table#ChartTable', first=True)
    songs  = table.find('a span[itemprop=name]')
    artist = table.find('span[itemprop=byArtist]:first-child span[itemprop=name]')
    for rank, song in enumerate(songs):
        print(f'{rank + 1}: {song.text},{artist[rank].text}')

if __name__ == '__main__':
    main()
