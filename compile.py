print("Welcome to our stress questionnaire. We will give you a list of topics. \nFor each one, rate your level of stress relating to that topic on a scale of 1 to 5.\n1 being the least stressed,\n3 if you are unconcerned, and \n5 being the most stressed.\n\n")
# print("Response scale:\na - Super happy\nb - Very happy\nc - Unbothered\nd - Mildly disappointed\ne - Very disappointed")

def assessment1(question, points):
    """print out question, take in current points and return total points after getting answer"""
    print(question)
    response=input()
    while response!="1" and response !="2" and response!="3" and response !="4" and response!="5":
        response=input("Please rate with a number from 1 to 5")
    response=int(response)
    print()
    if response == 1:
        points+=1
    elif response == 2:
        points+=2
    elif response == 3:
        points+=3
    elif response == 4:
        points+=4
    else:
        points+=5
    return points


def yesnoques(question):
    """check question for correct format, then return y or n"""
    print(question,"(y/n)")
    ans=input()
    while ans!="y" and ans!="n":
        print("Please reenter your answer (y/n).",question)
        ans=input()
    return ans

points = 0
#question 1-11
points=assessment1("Question 1 : On a scale of 1 to 5, how do you feel in regards to your present job, business, or school?",points)
points=assessment1("Question 2 : How would you rate the quality of your primary relationships?",points)
points=assessment1("Question 3 : How would you rate your capacity to have fun?",points)
points=assessment1("Question 4 : How would you rate your financial prospects?",points)
points=assessment1("Question 5: How satisfied are you concerning spirituality?",points)
points=assessment1("Question 6: How would you rate your level of self-esteem?",points)
points=assessment1("Question 7: How would you rate your sex life?",points)
points=assessment1("Question 8: How satisfied are you with your body, how it looks and performs?",points)
points=assessment1("Question 9: How would you rate your home life?",points)
points=assessment1("Question 10 : Life skills and knowledge of issues and facts unrelated to your job or profession.",points)
points=assessment1("Question 11 : Ability to recover from disappointment, hurts, setbacks, and tragedies.",points)


print("For the following questions, indicate how much you identify with each statement on a scale of 1 to 5.")

#question 12-15
points=assessment1("Question 12 : You have the confidence that you currently are, or will in the future be, reasonably close to your highest potential.",points)
points=assessment1("Question 13 : You have achieved a rounded or balanced quality in your life.",points)
points=assessment1("Question 14: You have the sense that life for you is on an upward curve, getting better and fuller all the time.",points)
points=assessment1("Question 15: You have a role in some kind of network of friends, relatives, and/or others about whom you care deeply and who reciprocate that commitment to you.",points)

# print(points)

if points<35:
    print("you have low level of stress")
elif points<55:
    print("you have moderate level of stress")
else:
    print("you have high level of stress")

if yesnoques("Do you want to take a depression self-assessment?")=='y':
    depression()
else:
    print("thank you for taking this quiz")


def depression():
    print("This is the depression self-assessment.")
    q21=yesnoques("Do you often feel down, depressed, or hopeless?")
    q22=yesnoques("Do you lack interest in activities, hobbies, and what is happening around you?")
    if q21=='y' or q22=='y':
        print("Further assessment is needed from you.")

def selfharm():
    print("This is the suicide - self harm self-assessment. Please answer y/n to following questions.")
    q31=yesnoques("Do you feel hopeless about the present or future?")
    if q31=="y":
        q32=yesnoques("Have you had thoughts about taking your life?")
        if q32=="y":
            print("When did you have these thoughts and do you have a plan to take your life?")
            q33=input("")
            """should insert chatbot function into here to reply"""
    q34=yesnoques("Have you ever attempted to harm yourself or attempted suicide?")
    if q31=="y" or q32=="y" or q34=="y":
        print("Please seek immediate attention from a trained clinician.")
#what happens if patient answer "no" to the questions??
