#Ask Username
name=input("Enter your Name:\n")
#welcome wishes!
print("Hello!",name,",","Welcome to the Quiz :) !\n")
print("#######Rules Of the Quiz#######\n")
print("->In This Quiz Completely Will Be  in Python \n")
print("->Only 5 questions Will Be their in this Quiz.All Questions are MCQ'S\n")
print("->Each question have 5marks weightage\n")
print("->Total marks is '25'\n")
print("->Above 15 are Pass Marks and  below 15 are Fail marks \n")      
print("->No negative marks\n")
#Creating  5 multiline strings(q1,q2,q3,q4,q5) in python by using triple quotes("""")
q1="""1)Who developed Python Programming Language?
a)Wick
b)John rick
c)Guido Van Rossum
d)Niene stok
"""
q2="""2)Is python case sensitive when dealing with identifiers?
a)No
b)yes
c)a is correct
d)none of the above
"""
q3="""3)Which of the following is the correct extension of the python file?
a).python
b).prr
c).py
d).y
"""
q4="""4)Which of these is not a core datatype ?
a)List
b)Dictionary
c)Tuples
d)Class
"""
q5="""5)Is python supports exception handling?
a)yes
b)no
c)none of the above
d)Invalid Question
"""
#creating dictionary named as questions
questions={q1:"c",q2:"b",q3:"c",q4:"d",q5:"a"}
#intializing score value as 0
score=0;
#By using for loop to print quiz questions
for i in  questions:
    print(i)
    #By using input function to take answer as input from the user
    ans=(input( "Enter the answer[a/b/c/d]:"))
    #By using if loop to compare user answer with actual answer
    if(ans==questions[i]):
        #if its correct print below statement
        print(ans," is Correct answer!")
        score+=5
        #prints current score
        print("current score :",score)
    else:
        print("wrong answer!Correct answer is",questions[i])
print("quiz completed")
#By using if loop to check whether the player is pass or fail
if(score<=15):
    print("-------------------------------------")
    print(name,"!your are failed in this quiz\n")
    print("Better luck next time")
else:
    print("-------------------------------------")
    print(name,"!Your are passed in this quiz")
    print("Your performance on this quiz is awesome")
#prints final score
print("Your Final Score is",score,"/25")