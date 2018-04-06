#1
string = "Hello, how's life treating you buddy?"
print(string.upper())

#2
string = "you have failed this city."
print(string.capitalize())

#3
string = "alucard"
print(string[::-1])

#4
para = " If you can read this you really need to get a life Noob!"
new_para = ""
for chr in para:
    if chr.upper() == "A":
        new_para += str(4)
    elif chr.upper() == "E":
        new_para += str(3)
    elif chr.upper() == "G":
        new_para += str(6)
    elif chr.upper() == "I":
        new_para += str(1)
    elif chr.upper() == "O":
        new_para += str(0)
    elif chr.upper() == "S":
        new_para += str(5)
    elif chr.upper() == "T":
        new_para += str(7)
    else:
        new_para += chr
print(new_para)

#5
long_vowels = ("Duh-Kay Extreme is one of the best youtubers.")

long_vowels = long_vowels.replace("a", "aaaaa")
long_vowels = long_vowels.replace("e", "eeeee")
long_vowels = long_vowels.replace("i", "iiiii")
long_vowels = long_vowels.replace("o", "ooooo")
long_vowels = long_vowels.replace("u", "uuuuu")

print(long_vowels)  

#6
letters = "abcdefghijklmnopqrstuvwxyz"
text = "lbh zhfg hayrnea jung lbh unir yrnearq"
decipher = ""
for chr in text:
    if chr != " ":
        pos = letters.index(chr)
        if pos >= 13:
            decipher += letters[pos-13]
        else:
            decipher += letters[pos+13]
    else:
        decipher += chr
print(decipher)
