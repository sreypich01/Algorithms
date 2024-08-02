# •	Enter a string text in the console.
# •	Print length of text times of the character "X”.
text = input()
result = ""
for i in range(len(text)):
    result += "x"
print(result)