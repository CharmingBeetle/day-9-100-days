print("***GENERATION GENERATOR***")
print()
dob = int(input("What's your birth year?"))
if dob <= 1946 and dob >= 1925:
  print ("You're part of the Traditionalist Generation!")
elif dob <= 1964 and dob >= 1947:
  print ("You're part of the Baby Boomers generation!")
elif dob <= 1979 and dob >= 1965:
  print("Congrats! You are Generation X")
elif dob <= 1995 and dob >= 1980:
  print("Congrats! You're in the Millenial Generation!")
elif dob <= 2015 and dob >= 1996:
  print("Hurray! You're Gen Z!")
else: 
  print("Sorry you're too old or young for this app!")