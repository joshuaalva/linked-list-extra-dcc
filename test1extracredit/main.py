from stack import Stack

print("Welcome to the Word Reversal Program")
userInput = input("Please type a word follow by Enter or type 999 to quit: \n")
myStack = Stack()

for letter in userInput:
    myStack.push(letter)

print(f"{userInput} : {myStack}")

while(userInput != 999):
    if(userInput == "999"):
        print("You have quit the program")
        break
    
    else: 
        userInput = input("To keep reversing words, please type a word followed by Enter or type 999 to quit: \n")
        myStack = Stack()
        for letter in userInput:
            myStack.push(letter)

        print(f"{userInput} : {myStack}")