sentence = ""
newSentence = ""

def getSentence():
    global sentence
    sentence = input("Please enter a sentence.\n\n")

def reverseIt():
    global sentence, newSentence
    for i in range(len(sentence)-1,-1,-1):
        newSentence += sentence[i]
    print(newSentence)

# getSentence()
# reverseIt()

def reversing():
    global sentence
    print(sentence[::-1])

# getSentence()
# reversing()

def theSentence():
    sentence = input("Please enter a sentence:\n\n")
    print(sentence[::-1])

theSentence()