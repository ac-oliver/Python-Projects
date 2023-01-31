#Movie Recommendations

from random import randint
import random

fantasy = ['LOTR', 'Pan\'s Labyrinth', 'Princess Mononoke', 'Spirited Away', 'Howl\'s Moving Castle', 'The Princess Bride']
drama = ['13 Assassins', 'Django Unchained']
comedy = ['The Other Guys']
musical = ['The Phantom of the Opera']

genre = input('Do you feel like fantasy, drama, comedy, or a musical?')
if genre == 'Fantasy':
    print(random.choice(fantasy))
elif genre == 'drama':
    print(random.choice(drama))
elif genre == 'Comedy':
    print(random.choice(comedy))
elif genre == 'musical':
    print(random.choice(musical))
else:
    print('You either need to check your spelling or just choose a movie.')
