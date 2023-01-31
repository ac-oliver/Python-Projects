#ideal protein intake calculator

print('For building muscle, a solid amount of protein to cosume is 1.6 grams per kg of body weight.')

weight = input('How much do you weigh?')
print('You weigh ' + weight + ' kgs.')

protein = str(int(weight)* 1.6)

print(f"Daily, you should consume {protein} grams of protein.")
