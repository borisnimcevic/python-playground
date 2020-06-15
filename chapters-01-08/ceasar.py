#example code based on www.tutorialspoint.com
#some usefull terms to reasearch:
# - ASCII table
# - python ord()
# - python chr()

def CeaserCypher(text,shift,direction):
	result=""
	if (direction == 'L'):
		shift = shift * (-1)
	elif (direction == 'R'):
		shift = abs(shift)

	for i in range(len(text)):
		letter = text[i]

		if(letter.isupper()):
			result+=chr((ord(letter) + shift - 65) % 26 + 65)
		else:
			result+=chr((ord(letter) + shift - 97) % 26 + 97)
	return result

test_text = "the"
test_shift = 2

print("Plain text: " + test_text)
print("Encrypted tect: " + CeaserCypher(test_text,test_shift,'L'))
