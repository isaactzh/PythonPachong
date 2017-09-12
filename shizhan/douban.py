from bs4 import BeautifulSoup
import requests

DownLOAD_URL = 'http://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'
}

def download_page(url):
    return requests.get(url, headers = headers).content

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    movie_list_soup = soup.find('ol', attrs = {'class': 'grid_view'})
    movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs = {'class':'hd'})
        movie_name = detail.find('span', attrs = {'class': 'title'}).text

        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs = {'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, DownLOAD_URL + next_page['href']
    return movie_name_list, None

def main():
    url = DownLOAD_URL

    with open('/home/isaac/Desktop/movie.text', 'w') as f:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            print(movies)
            f.write('{movies}\n'.format(movies='\n'.join(movies)))

if __name__ == '__main__':
    main()