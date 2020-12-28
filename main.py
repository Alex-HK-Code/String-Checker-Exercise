def beginWithVowel(s):
    if(len(s)) == 0:
        return False 
    if(s[0] == 'a' or s[0] == 'e' or s[0] == 'i' or s[0] == 'o' or s[0] == 'u'):
        return True 
    return False #return false if the above condition is not fulfilled


while(True):
    user_string = input("Enter 'exit' to exit the program | Enter a string that you want to check:\n")

    if(user_string == "exit"):  #break the while loop
        break

    if(beginWithVowel(user_string)):   #if beginWithVowel returns true, enter the block 
        print("It begins with a vowel")

    