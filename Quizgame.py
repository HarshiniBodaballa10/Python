questions=("What is the largest animal?:",
           "Where is the taj mahal located?:",
           "What is our national Bird?:")
options=(("A. Whale", "B. Elephant", "C. Giraffe", "D. Ostrich "),
         ("A. Hyderabad", "B. Vizag", "C. Mumbai", "D. Agra "),
         ("A. Parrot ", "B. Pegeon ", "C. Peacock ", "D. Sparrow "))
answers=["A","D","C"]
guesses=[]
score=0
question_num=0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"The correct answer is {answers[question_num]}")
    question_num+=1
print("Result")
print("answers: ",end="")
for answer in answers:
    print(answer,end="")
print()
print("guesses: ",end="")
for guess in guesses:
    print(guess,end="")
print()
score=int((score/len(questions))*100)
print(f"The Score is : {score}%")
