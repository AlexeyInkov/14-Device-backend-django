import requests
import random
from bs4 import BeautifulSoup as bs


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # получаем ответ HTTP и создаем объект soup
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("tbody"):
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies


def check_proxies(proxies):
    real_proxies = []
    for proxy in proxies:
        s = get_session([proxy])
        try:
            s.get("http://icanhazip.com", timeout=1.5)
        except Exception as e:
            continue
        else:
            real_proxies.append(proxy)
    return real_proxies


def get_session(proxies):
    # создать HTTP‑сеанс
    session = requests.Session()
    # выбираем один случайный прокси
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


proxies = get_free_proxies()
print('Получено', len(proxies), "proxy")
real_proxies = check_proxies(proxies[:50])
print('Прошли проверку', len(real_proxies), "proxy")

for i in range(5):
    s = get_session(real_proxies)
    try:
        print("Страница запроса с IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
    except Exception as e:
        continue

