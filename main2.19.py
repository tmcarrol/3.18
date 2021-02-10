
# Timothy Carroll
# ID: 1826369

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings_cups = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_cups))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups))
print('{:.2f} cup(s) water'.format(water_cups))
print('{:.2f} cup(s) agave nectar'.format(nectar_cups))

num_servings_required = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups * num_servings_required / servings_cups))
print('{:.2f} cup(s) water'.format(water_cups * num_servings_required / servings_cups))
print('{:.2f} cup(s) agave nectar'.format(nectar_cups * num_servings_required / servings_cups))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} gallon(s) lemon juice'.format(lemon_juice_cups * num_servings_required / servings_cups / 16))
print('{:.2f} gallon(s) water'.format(water_cups * num_servings_required / servings_cups / 16))
print('{:.2f} gallon(s) agave nectar'.format(nectar_cups * num_servings_required / servings_cups / 16))

