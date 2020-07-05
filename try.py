import json

class gusoma:
    def __init__(self, filename):
        self.filename = filename



    def Open(self):
        infile = open(self.filename, "r")
        content = infile.read()
        infile.close()

        return content

    def Words(self):
        content = self.Open()
        List = []
        List.append(content)
        words = List[0].split()

        return words 


class indangahantu:
    def __init__(self, filename2):
        self.filename2 = filename2

    def Open2(self):
        infile2 = open(self.filename2, "r")
        content2 = json.loads(infile2.read())
        infile2.close()

        return content2
    
    def Recognition(self):
        ListCount = {}
        count = 0
        c=0
        content2 = self.Open2()
        indangahantu_data = AI.Words()
        for indangahantu_data_in in indangahantu_data:
            ListCount[indangahantu_data_in] = 0
            if indangahantu_data_in in content2.get("indangahantu"):
                count = ListCount[indangahantu_data_in]
                if count > 0:
                    return count
                count += 1
                c += 1
                ListCount[indangahantu_data_in] = count
                ListCount["c"] = c
                count = 0
        return ListCount




AI2 = indangahantu("example.json")

filename = "paragraph.txt"
AI = gusoma(filename)

#print(AI.Words())
#print('\n', '80')
print(AI2.Recognition())
