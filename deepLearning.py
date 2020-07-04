# Text-reply Kinyarwanda_Ai, based on Translation 
# of Kinyarwanda language into Mathemetical expression
# And those Mathematical signals are then used to get the Logic behind

import numpy as np

class Ai:
    def __init__(self, inputs, inputList):
        self.inputs = inputs
        self.inputsList = inputsList
    
    def memory(self):
        # We give a value every letter and number
        # Numbers remain with their value and From the start to the very end
        # Letters get an incrementing value(1),by dividing 10 (10 is arbitrary taken but there's a reason to divide) to their corresponding
        # Number in the alphabetic order, we get a variable for use ... memory will be completed later on
        memory = {'1':float(1), '2':float(2), '3':float(3), '4':float(4), '5':float(5), '6':float(6), '7':float(7), '8':float(8), '9':float(9), '0' :float(0),
                  'a':float(0.1), 'b':float(0.2), 'c':float(0.3), 'd':float(0.4), 'e':float(0.5),
                  'f':float(0.6), 'g':float(0.7), 'h':float(0.8), 'i':float(0.9), 'j':float(2.7), 'k':float(1.1), 
                  'l':float(1.2), 'm':float(1.3),'n':float(1.4), 'o':float(1.5), 'p':float(1.6),'q':float(1.7), 'r':float(1.8), 's':float(1.9),'t':float(2.8),
                  'v':float(2.2), 'u':float(2.1), 'w':float(2.3), 'x':float(2.4), 'y':float(2.5),'z':float(2.6)}
        
        return memory
    
    def database(self):
        # @Clovis @Roger ... This function will return a dictionary
        # With key and value more precisely key that has logical float value from Learning sessions
        # And value which is the range of replies, This system takes advantage of it to perfect replies as value is Editable in the database_dictionary
        return null
    
    def separator(self):
        # This function get inputs as one string and separates them by terms
        inputs = self.inputs
        inputsList = self.inputsList
        # List of input terms
        inputs_term = inputsList[0].split(',')
        
        return inputs_term
    
    def inputsValue(self):
        # This function appends a value in inputs_value_list 
        # based on the memory data and gets the sum of in_terms to generate 
        # a Mathemetical sense of the input sentence
        inputs_term = AI.separator()
        inputs_value_list = []
        memory = AI.memory()
        
        for terms in inputs_term:
            for in_terms in terms:
                for key, value in memory.items():
                    if in_terms == key:
                        # On the inputs_value a weight is powered
                        # This is to give a room the slope for the Ai best fit line
                        # It will also help to find the logic in form of a range
                        # There will be answers ranging in the same value, this Ai will learn
                        # and pick the perfect solution form the memory
                        inputs_value_list.append(float(value) ** len(inputs_term))
        
        # With the in_terms value powered the inputs_value is remarkable for other use
        inputs_value = sum(inputs_value_list)
        
        return inputs_value
    
    def learn(self):
        # This list hold the meaning(in terms of numbers) of webscrapped/input Data
        # based on classification of words in Kinyarwanda
        # This will help to analyse learning process 
        # Learn() save it's data in Database_dictionary with a specific key and value
        logic_key = []
        return logic_key
    
    def logic(self):
        logic_list = []
        # Logic array for faster processing -- later use
        logic_list_array = np.array(logic_list)
        
        inputs_value = AI.inputValue()
        sigmoid = (1 / (1 - np.e ** (float(-inputs_value))))
        # From the Database 
        logic = AI.database()
        
        for key, value in logic.items():
            # sigmoid and key are decimal numbers that define logic from inputs
            if sigmoid == key: 
                logic_list.append(str(value))
        
        return logic_list
    
    def reply(self):
        # This function does nothing much than returning 
        # An already analysed reply 
        logic_list = AI.logic()
        for reply in logic_list:
            return reply
        
# User-end
inputs = input('Ai: Amakuru ? Mbafashe iki?\n:')
# Input Lists storage 
inputsList = []
inputsList.append(inputs)

# Passing variables to the Ai class
AI = Ai(inputs, inputsList)
reply = AI.reply()

# Output
print(reply)
