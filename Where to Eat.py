import random

restaurant = ['1154', 'Nolita', 'Origami', 'Somewhere New', 'Crab Shack', 'Rosita\'s Tacos' 'Chow', 'Dragonfly']
fast_food = ['Subway', 'Hell\'s Pizza', 'Dominos', 'Takeaway Nolita', 'Sushi']
cafe = ['Midnight Espresso', 'Belen']

where_eat = input('Dinner, fast food, or a cafe?')
if where_eat == 'dinner':
    print('You must eat at: ' + random.choice(restaurant))
elif where_eat == 'fast food':
    print('You must eat at: ' + random.choice(fast_food))
elif where_eat == 'cafe':
    print('You must eat at: ' + random.choice(cafe))
else:
    'That is not an option. Please choose one of the three options.'
