import random

small = 1
big = 10
secret_number = random.randint(1, 10)

def guess_my_number(small, big):
    guess = (small + big) // 2
    return guess

def smaller(guess):
    return guess - 1

def bigger(guess):
    return guess + 1
    

#main loop

while True:
    guess = guess_my_number(small, big)
    print(guess)
    
    if guess > secret_number: 
        big = smaller(guess)
    
    if guess < secret_number:
        small = bigger(guess)
    if guess == secret_number:
        print(f"The secreet number is: {guess}")
        break
    print(guess)

print(f"Just for the test i print what lies under 'secret_number' variable: {secret_number}")
print(f"If this agrees with the number above you are golden!")
