wrd=input("Give me a word: ")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd.upper() == rvs.upper():
    print("This is a Palindrome")
else:
    print("This is NOT a Palindrome")