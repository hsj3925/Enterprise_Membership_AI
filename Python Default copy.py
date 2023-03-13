cube = float(input("cube = "))
epsilon = 0.001
guess = 0.0
increment = 0.001
num_guesses = 0
limitmax = 1.0
limitmin = cube
guess = (cube + limitmax) / 2
while abs(guess**3 - cube) >= epsilon:
	if guess**3 >= cube:
		limitmax = guess
		guess = (guess + limitmin) / 2
	else:
		limitmin = guess
		guess = (guess + limitmax) / 2

	num_guesses += 1
	
	print('num_guesses = ', num_guesses)
	if abs(guess**3 - cube) >= epsilon:
		print("Failed on cube root of", cube, guess)
	else:
		print(guess, 'is close to the cube root of', cube)