from random import shuffle
from functions.ordinal import ordinal 

length = None

def ask():
    global length # "global" makes a function have the ability to modify variable in global scope
    try:
        answer = int(input("Please decide the number length[3-9] (default 4): "))
    except ValueError:
        print("Please do not enter non-number characters")
        return None # Break the function
    if answer not in range(3, 10):
        print("Please enter a number between 3 and 9, inclusive")
        return None
    else:    
        length = answer
        return None 

while length == None:
    ask()

# functions 
def generate(length : int) -> str:
    """
    Return a non-repeating number by the given length, 
    the number is consist of 0-9 and starts with a non-zero number.
    
    For example: 435, 1234, 15094 or 156107
    """
    numbers = []
    for i in range(10):
        numbers.append(i)
    shuffle(numbers)
    while numbers[0] == 0:
        shuffle(numbers)
    return "".join(map(str, numbers[:length])) # [1, 3, 8, ...] -> ["1", "3", "8" , ...] -> "138..."

answer = generate(length)
guess = 0
attempts = 0
while guess != answer:
    guess = input(f"Please enter a {length}-digit number: ")
    #　detections
    is_break = False
    try:
        int(guess)
    except ValueError:
        print("Please do not enter non-number characters")
        continue
    for i in guess:
        if guess.count(i) >= 2:
            print("Number can't be repeated")
            is_break = True
            break
    if is_break:
        continue
    if guess[0] == "0":
        print("Number can't starts with '0'")
        continue
    if len(guess) != length:
        print(f"Please enter a \"{length}-digit\" number, you entered a {len(guess)}-digit number")
        continue
    
    # calculations
    attempts += 1
    A = 0   
    B = 0
    for i in range(length):
        if guess[i] == answer[i]:
            A += 1
        elif guess[i] in answer:
            B += 1
    print(f">>>　{A}A{B}B") # (e.g., 1A4B)
print(f"You win after your {ordinal(attempts)} attempt!")
