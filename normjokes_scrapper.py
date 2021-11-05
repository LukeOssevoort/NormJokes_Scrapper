from requests_html import HTMLSession
from collections import namedtuple

def get_joke(number):
    session = HTMLSession()
    r = session.get('https://normjokes.com/' + str(number))
    r.html.render()
    joketext = r.html.find('#joke', first=True)
    ep = r.html.find('#ep', first=True)
    guest = r.html.find('#guest', first=True)
    Joke = namedtuple("Joke", "text ep guest")
    out = Joke(joketext.text, ep.text, guest.text)
    return out