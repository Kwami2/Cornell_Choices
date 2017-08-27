#Made by Saleh Hassen
def soapBox(printThis):
    print printThis

college = lambda x: soapBox("You went to college, write the rest later")
    
military = lambda y: soapBox("You went to serve your country, write the rest later")

world = lambda z: soapBox("You decided to see the world, write the rest later")

class User(object):
    #Write this to keep track of user info 
    pass

class Question(object):

    ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'] #mostly
    
    def __init__(self, question, ansChoices, results):
        assert type(question) == str
        assert type(ansChoices) == list
        assert type(ansChoices[0]) == str
        #assert type(results) ==
        
        self.question = question
        self.ansChoices = ansChoices
        self.results = results
        self.letterChoices = []
    
    def initializeChoices(self):
        for index in range(len(self.ansChoices)):
            self.letterChoices.append(self.ALPHABET[index])
     
    def q_and_a(self):
        """Shows question and gets answer"""
        self.initializeChoices()
        answerInvalid = True
        print self.question
        for index in range(len(self.ansChoices)):
            print self.letterChoices[index] + ") " + self.ansChoices[index] 
        while(answerInvalid):
            userAnswer = raw_input(self.question)
            userAnswer = userAnswer.lower()
            if (userAnswer in self.letterChoices): #what conditions that make userAnswer valid
                answerInvalid = False
        chosenResult = self.results[self.letterChoices.index(userAnswer)]
        print type(chosenResult)
        chosenResult(2)

#Demo of the class
initialQuestion = Question("Hello dear adventurer, what is your chosen adventure?",
         ['go to college', 'go to the military','travel the world'],
         [college,military,world])
initialQuestion.q_and_a()


