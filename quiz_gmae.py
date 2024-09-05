print("Welcome to my computer Quiz!!")

playing = input("Do you want to play?? ")

if playing.lower()!= "yes":
    quit()
    
print("Okey ! Let's play :)")
score = 0

answer = input("what does CPU stands for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!!')
    
answer = input("what does GPU stands for? ").lower()
if answer == "graphical processing unit":
    print('Correct!')
    score += 1

else:
    print('Incorrect!!')
    
answer = input("what does RAM stands for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!!')
    
answer = input("what does PSU stands for? ").lower()
if answer == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!!')
    
answer = input("All questions are related to what? ").lower()
if answer == "computer parts":
    print('Correct!')
    score += 1
else:
    print('Incorrect!!')

print("You got " + str(score)+ " Questions correct!!")
print("You got " + str((score / 4) * 100)+ "%.")

