from requests_html import HTMLSession

def get_joke(number):
    session = HTMLSession()
    r = session.get('https://normjokes.com/' + str(number))
    r.html.render()
    joke = r.html.find('#joke', first=True)
    ep = r.html.find('#ep', first=True)
    guest = r.html.find('#guest', first=True)
    print("Joke:")
    print(joke.text.replace('\n','\n\n'))
    print("\nEpisode:")
    print(ep.text)
    print(guest.text)