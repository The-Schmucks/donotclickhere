# Texting back app

from time import ctime
import os 
import webbrowser
from youtube_search import YoutubeSearch

def TextInput(prompt):
    data = str(input(prompt).strip()).lower()

    return data

def answering(dictionary, data):
    conv = data
    if conv in dictionary:
        if str(conv) in dictionary:
            value = dictionary.get(conv)
            if conv == 'kina':
                search_term = input("Kadogo: Mbwira izina ry'indirimbo: ")
                results = YoutubeSearch(search_term, max_results=10).to_json()
                i = results.find('link')
                j = results.find(',', i, -1)

                needed = results[i: j]
                i1 = needed.find('/')
                needed2 = needed[i1: -1]
                a_website = "https://www.youtube.com" + needed2
                answer = webbrowser.open_new(a_website)
            answer = str(value)
        
    else:
        answer = 'Ntago mbyumvise !'
        
    return answer 

def read(filename):
    dictionary = {}
    infile = open(filename, 'r')
    content = infile.readlines()
    #infile.close()
    for i in content:
        ques = i.strip().split('-')[:1]
        ans = i.strip().split('-')[1:]
        # print('%r\t\t%r' %(ques, ans))
        for k, j in zip(ques, ans):
            dictionary[k.strip()] = j.strip()
    
    return dictionary


def main():
    prompt = 'Me: '
    #dictionary = {'amakuru': 'ni meza', 'mwaramutse': 'Waramutse !','ni saa ngahe': ctime(), 'bye': 'Bye, Mugire ibihe byiza !'}
    filename = 'draft.txt'
    dictionary = read(filename)
    additional = 'ni saa ngahe'
    dictionary[additional] = ctime()
    data = ''
    
    while str(data) != 'bye':
        print('\n', '-'*80)
        data = TextInput(prompt)
        answer = answering(dictionary, data)
        print('Charmant: ', answer)
main()




'''
indamukanyo - condtion ctime()
amategeko - 
inkomyi


while str(input('kanda 1 niba ushaka gukuramo: ')) != '1':
    print('\n', '-'*80)
    conv = str(input('Me: ').strip())

    for i, k in dictionary.items():
        if str(i.strip()) == str(conv.strip()):
            print('Charmant: ', k)
            break
            
        elif str(conv) != str(i):
            print('Ntago mbyumvise !\nBasubiza bate ?: ')
            a = str(input('Basubiza ngo: '))
            dictionary[conv] = a
            print('Charmant: Murakoze !')
            
        else:
            print('Nishimiye kuganira namwe')
        
        else:
            if str(i.strip()) != str(conv.strip()):
                print('Ntago mbyumvise !\nBasubiza bate ?: ')
                a = str(input('Basubiza ngo: ').strip())
                dictionary[conv] = a.strip()
                break


#--------------------------------
import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
#-------------------------------






import pyaudio
import wave 
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print('Play a wave file.\n\nUsage: %s filename.wave' %sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')
p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(wf.getsampwidth()), channels = wf.getnchannels(), rate = wf.getframerate(), output = True)

data = wf.readframes(CHUNK)

while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()












import pygame
import tkinter as tkr

player = tkr.Tk()

player.title('Music player')
player.geometry()

file = 'song.mp3'

def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()

button1 = tkr.Button(player, width=5, height=3, text='Play', command=Play)
button1.pack(fill='x')
button2 = tkr.Button(player, width=5, height=3, text='Stop', command=ExitPlayer)
button2.pack(fill='x')

label1 = tkr.LabelFrame(player, text='Song Name')
label1.pack(fill='both', expand='yes')
contents1 = tkr.label(label1, text=file)
contents1.pack()

player.mainloop()

import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.amazon.ca/s?k=piano&ref=nb_sb_noss_1')
src = result.content
soup = BeautifulSoup(src, 'lxml')

for span in soup.find_all('div', class_='a-section a-spacing'):
    data = span.find('span', class_='a-price-whole')
    print(data)
  
import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.sportingnews.com/ca/soccer?utm_source=Goal&utm_medium=Redirect&utm_campaign=Canada')
src = result.content
soup = BeautifulSoup(src, 'lxml')

print(soup.prettify())
'''












