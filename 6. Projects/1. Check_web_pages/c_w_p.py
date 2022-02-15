import webbrowser

import requests

site = ('https://mmr-ashiq.github.io/')
pages = ['#home', '#about', 'skills', '#projects', '#contact']

for page in pages:
    url = site + page
    response = requests.get(url)
    if response.status_code == 200:
        print(f'{url} - OK')
    else:
        print(f'{url} - {response.status_code}')
        webbrowser.open(url)
