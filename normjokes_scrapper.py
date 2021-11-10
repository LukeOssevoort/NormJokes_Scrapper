from requests_html import HTMLSession
from collections import namedtuple
import pickle

session = HTMLSession()
Joke = namedtuple("Joke", "text ep guest")

def get_joke(number):
    r = session.get('https://normjokes.com/' + str(number))
    r.html.render()
    joketext = r.html.find('#joke', first=True)
    ep = r.html.find('#ep', first=True)
    guest = r.html.find('#guest', first=True)
    out = Joke(joketext.text, ep.text, guest.text)
    return out

def get_jokelist():
    jokelist = []
    print('Loaded 000 of 407 jokes')
    for i in range(407):
        jokelist.append(get_joke(i))
        print('Loaded ' + f'{(i+1):03}' + ' of 407 jokes')
    else:
        print('')
        print('Jokes loaded')
    
    return jokelist

def get_jokepickle(jokeFileName):
    try:
        jokeFile = open(jokeFileName, 'rb')
        jokelist = pickle.load(jokeFile)
        print('Loaded jokes from file')
        jokeFile.close()
    except:
        jokeFile = open(jokeFileName, 'wb+')
        jokelist = get_jokelist()
        pickle.dump(jokelist, jokeFile)
        print('Saved joke list')
        jokeFile.close()
    return jokelist
