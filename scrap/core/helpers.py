

from bs4 import BeautifulSoup


def string_to_soup( html ):
    soup =  BeautifulSoup(html, 'html.parser')
    [s.extract() for s in soup(['iframe', 'script', 'style'])]
    return soup