#Darryl Lau: 348615006
def caesarCipher(word,num):
    #Assume the word is all lowercase
    newWord = ''
    for i in word:
        x = ord(i) + num
        if (x > 96 and x < 122):
            wordConverted = chr(x)
            newWord += wordConverted
        elif (x > 122):
            ascii1 = (x-122)+96
            wordConverted = chr(ascii1)
            newWord += wordConverted
        else:
            ascii2 = (123-(97-x))
            wordConverted = chr(ascii2)
            newWord += wordConverted
    return newWord

test = input("Enter a word: ")
test1 = int(input("Enter the cipher number: "))
print(caesarCipher(test,test1))