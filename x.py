from deepLearning import Ai

inputs = ''
while inputs!='0':

    inputs = input('Ai: Amakuru ? Mbafashe iki?\n:')
    # Input Lists storage
    inputsList = []
    inputsList.append(inputs)

    # Passing variables to the Ai class
    AI = Ai(inputs, inputsList)
    reply = AI.reply()

    # Output
    print(reply)

#print(Ai().database())