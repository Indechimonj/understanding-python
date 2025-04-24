print("Welcome to my computer quiz.")
playing = input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("Okay!Let's play: ")
score=0

answer=input("What does CPU stand for?").lower()
if answer =="central processing unit":
    print ("Correct")
    score += 1
else:
    print("Incorrect!")

answer_2=input("What does GPU stand for? ").lower()
if answer_2 =="graphics processing unit":
    print ("Correct")
    score += 1
else:
    print("Incorrect!")

answer_3=input("What does RAM stand for? ").lower()
if answer_3 =="random access memory":
    print ("Correct")
    score += 1
else:
    print("Incorrect!")

print("You got "+ str(score) + " questions correct!")
print("You got "+ str((score/3) * 100) + " %")