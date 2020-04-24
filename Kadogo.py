import re
import requests
from youtube_search import YoutubeSearch

class Kadogo:
    
    __dict_file = "draft.txt" #commands file
    dictionary = {}  #dictonary to hold the commands
    json_return = {}  #json_data to be returned by the api
    question = "" #holds the input from the user
    answer = "" #holds the output from kadogo
    audio = ""  #holds the audio file to be played
    is_command = False #indicates whether the answer is a command or not

    def __init__(self): #just a normal constructor mn. grow up
        self.json_return.clear()
        self.question = ""
        self.answer = ""
        self.audio = ""
        self.is_command = False
        self.dictionary = {}
        self.dictionary = self.load_dictionary()
        self.location = "paris,france" #i defined it coz i was having a bad time with android permissions
        

    def api(self, que):
        self.question = str(que).strip() #strips the input and sets it to the variable 'question'
        ans = self.answering()  #gets the answer from kadogo
        self.audio = re.sub(" ", "_", self.question) #replace the 
        self.json_return['audio'] = self.audio
        self.json_return['answer'] = ans
        self.json_return['is_command'] = self.is_command
        return self.json_return

    def get_temperature(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + self.location + "&appid=186d4b000520ab60db3db1c896f48882"
        data = requests.get(url)
        json_data = data.json()
        temp_k = float(json_data["main"]["temp"])
        temp_c = int(temp_k - 273.15)
        return str(temp_c)
    
    def answering(self):
        command = str(self.question.strip().split(" ")[0])
        
        if command == 'iteganyagihe':
            res = self.get_temperature()
            self.question = command
        
        elif  self.question in self.dictionary.keys():
            res = self.dictionary.get(self.question)
            
        elif command in self.dictionary.keys():
            res = self.dictionary.get(command)
            if  command == 'kina':
                search_term = str(self.question.split("kina ")[1])
                results = YoutubeSearch(search_term, max_results=1).to_json()
                i = results.find('link')
                j = results.find(',', i, -1)

                needed = results[i: j]
                i1 = needed.find('/')
                needed2 = needed[i1: -1]
                res = "https://www.youtube.com" + needed2
                self.is_command = True

        else:
            res = 'Ntago mbyumvise!'
        
        return res

    def load_dictionary(self):
        
        res = {}
        infile = open(self.__dict_file, 'r')
        content = infile.readlines()
        for i in content:
            arr = i.strip().split('-')
            ques = arr[:1]
            ans = arr[1:]
            
            for k, j in zip(ques, ans):
                res[k.strip()] = j.strip()
        
        return res


n = Kadogo()

#output: {'audio': 'amakuru', 'answer': 'Ni meza.', 'is_command': False}
# outputs the answer, the name of the audio to be played, and wether it is a command or not
print(n.api("iteganyagihe")) 
