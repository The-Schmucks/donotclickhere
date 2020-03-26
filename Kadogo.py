import re
from youtube_search import YoutubeSearch

class Kadogo:
    
    __dict_file = "draft.txt"
    dictionary = {}
    json_return = {}
    question = ""
    answer = ""
    audio = ""
    is_command = False

    def __init__(self):
        self.json_return.clear()
        self.question = ""
        self.answer = ""
        self.audio = ""
        self.is_command = False
        self.dictionary = {}
        self.dictionary = self.load_dictionary()
        

    def api(self, que):
        
        self.question = str(que).strip()
        ans = self.answering()
        self.audio = re.sub(" ", "_", self.question)
        self.json_return['audio'] = self.audio
        self.json_return['answer'] = ans
        self.json_return['is_command'] = self.is_command
        return self.json_return

    
    def answering(self):
        command = str(self.question.strip().split(" ")[0])
        if  self.question in self.dictionary.keys():
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
            
            self.question = command

        else:
            self.audio = "Ntago mbyumvise"
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

pop = "kina pop smoke"
print(pop.split("kina ")[1])