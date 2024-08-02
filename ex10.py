# •	Enter a string word in the console.
# •	Enter the number n in the console.
# •	If word equal to “good” and the number between 7 and 15, it will be print “It’s good”.
# •	If word equal to “bad” and the number lower than 7 or greater than 15, it will be print “It’s bad”.
word = input("Enter a string word: ")
number = int(input("Enter a number: "))
if word == "good" and 7 <= number <= 15:
    print("It's good")
elif word == "bad" and (number < 7 or number > 15):
    print("It's bad")