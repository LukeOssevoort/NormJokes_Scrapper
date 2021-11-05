# Norm Jokes Scrapper

This python library scrapes the site [normjokes.com](https://normjokes.com/) for blue card jokes from the talk shows of the great Norm Macdonald.

## Usage

This library contains one function, ```get_joke(int)```, that takes an integer between 0 and 406, and returns the corresponding joke from [normjokes.com](https://normjokes.com/). The joke is given as an ```namedtuple``` containing the ```text``` of the joke, the ```ep```isode it is from, and the ```guest``` that was on. Below is some example code.

```Python
from normjokes_scrapper import get_joke
from random import randint

joke = get_joke(randint(0,406))

print(joke.text)
print()
print(joke.ep)
print(joke.guest)
```