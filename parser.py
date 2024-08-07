import os
import re
import requests


class Parser:
    url = "https://portal.tgc1.ru/"

    
    def get_page_wiht_nodes(self, session: requests.Session):
        return session.post(self.url + "directorate/nodes", data={"onpage": 100}).text

    def get_nodes(self, html_page: str):
        nod = re.compile(r"(?:<tr data-id=\")(\d+)(?:\">)")
        nodes = nod.findall(html_page)
        print(nodes)
        return nodes


