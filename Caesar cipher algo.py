letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)
print (letters[15])

def encrypt_decrypt(method, key):
    userText = input("Enter the message to transform.\n")
    convertedText = ""
    
    for letter in userText:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                convertedText += letter
            else:
                if method == "e":
                    new_index = index + key
                    if new_index >= num_letters:
                        new_index -= num_letters
                    convertedText += letters[new_index].upper()
                else:
                    new_index = index - key
                    if new_index < 0:
                        new_index += num_letters
                    convertedText += letters[new_index].lower()
    return convertedText

while True:
    try:
        method = input("Do you want to (e)ncrypt or (d)ecrypt?\n").lower()

        key = int(input("Please enter the key(0 to 25) to use.\n"))
        
        if (method == "e" or method == "d"):
            print(encrypt_decrypt(method, key))
        else:
            continue
        
    except: 
        print("Error invalid input")   
        a = input("Try (1)again or (2)end\n")
        
    if a == "1":
        continue
    else:
        break
    
print("end of caesar cipher")