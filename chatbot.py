from random import choice

computerResponses = [] # list of all computer's questions
humanResponses = []  # list of all the person's responses

def eliza():
    """
        simulate a Rogerian therapist
        this function asks the user questions
        based on the answer to the previous question
    """
    userComment = input("Computer >> How are you feeling today?\nThe User >> ")

    while userComment not in ["goodbye","bye","quit","exit"]:
        humanResponses.append(userComment)
        response = respond(userComment)
        if response in computerResponses:
            response = "Once again, "+response
        computerResponses.append(response)
        print("Computer >> "+response)
        userComment = input("The User >> ")
    print("bye")

def respond(comment):
    """ generate a computer response to the user's comment"""
    if contains(comment,sadWords):
        return choice(sadResponses)
    if contains(comment,madWords):
        return choice(madResponses)
    if len(comment.split()) <= 2:  # respond to short answers...
        return choice(shortResponses)
    return choice(generalResponses)

def contains(sentence,words):
    """ true if one of the words is in the sentence
        where sentence is a string and
        words is a list of strings
    """
    wordsInSentence = [word for word in words if word in sentence]
    return len(wordsInSentence) >= 1

def contains2(sentence,words):
    """
    a more efficient test to see if a word in the list words
    is also in the string sentence. Note, this will return
    True for contains2("lovely day",["el"])
    which might not be what you wanted. We could first split
    sentence into words, which might be better!
    """
    for w in words:
        if w in sentence:
            return True
    return False

# Here are the sad keywords and responses to sad comments
sadWords = "sad down blue depressed".split()
sadResponses=[
"Do you often feel sad?",
"What do you do when you are feeling blue?",
"Why do you think you are feeling down?",
"Do you find you have a lot of negative thoughts?"
]


# Here are the mad keywords and response to comments containing a mad keyword
madWords = "mad shutup angry upset hate anger wrath hatred delirium despicable,".split()
madResponses = [
  "calm down",
  "Why are you feeling this way?",
  "How long have you been feeling this way?",
  "Are you experiencing any conflicts in your life right now?",
  "i am listening, what makes you angry",
  "lifes good, dude",
  "what is frustrating you?"
]

# these are the possible responses to short comments
# like "yes" or "no" or "idk"
shortResponses = [
    "Could you please elaborate?",
    "Would you mind elaborating?",
    "What else?",
    "Anything more to say?",
    "Don't hold back on the words, brethren!",
    "Tell me more good person",
    "Fine. Tell me more about yourself.",
    "WHY ARE YOU BEING SO SHORT WITH ME!!!!"
]

# We give these responses if there is nothing else to say!
generalResponses = [
  "Hmmm. Tell me more.",
  "Do you have a lot of negative thoughts?",
  "Tell me about your relationship with your mother?",
  "How do you get along with your father?",
  "How do you feel about your performance in school?",
  "Do you often feel this way?",
  "How is your relationship with your mother?",
  "When was the last time you laughed out loud?",
  "Is there anyone you can confide in?",
  "Tell me about the last time you got mad.",
  "Tell me about the last time you were very sad.",
  "Do you ever feel ashamed about something you've done?",
]


if __name__=="__main__":
    eliza()  # call eliza when run as a script
             # but not when imported
