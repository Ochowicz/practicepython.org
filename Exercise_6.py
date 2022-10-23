def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[-1-i]
	return x


word = input('Give me a word: ')
x = reverse(word)


if x.upper() == word.upper():
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')
