from tkinter import *
import random
from numpy import char
from wordlist import words
#from PIL import ImageTk, Image

root = Tk()

#game version
version = '1.0'

#names the window
windowname = root.title(f'Hangman {version}')

#word that is being guessed
word = (random.choice(words))

#numerical length of variable word
wordlength = len(word)

#the word shown as guessed letters and dashes for unknown letters
shownword='-'*wordlength

#output message for errors, messages, etc.
message = ()

#last guessed letter
guessedletter=''

#window size
root.geometry('700x500')

#number of hints left
hintsleft = 2

#title
greeting = Label(text='Hangman', font = ('Helvetica', 24, 'bold'))
greeting.pack()

#Number of lives in a round
lives = (6)

#Letter input
label = Label(text='Guess a letter')
label.pack()

guessentry = Entry()
guessentry.pack()

#output label for errors, messages, etc.
outputlabel = Label(root, text = message)
outputlabel.place(relx= .5, rely= .25, anchor= CENTER)

#shownword
wordshow = Label(root, text = shownword)
wordshow.place(relx= .5, rely= .3, anchor= CENTER)

#create a new game
def newgame():
    global guessedletter, shownword, word, hintsleft
    word = (random.choice(words))
    wordlength = len(word)
    shownword = '-'*wordlength
    wordshow['text'] = shownword
    outputlabel['text'] = ''
    hintsleft = 2
    guessedletter=''
    guessentry.delete
    guessentry['state'] = NORMAL
    print(word)

#get entry and process it
def updategame():
    global shownword, lives, guessedletter, guess
    guess = guessentry.get()
    guessentry.delete(0, END)
    if lives < 1:
        guessentry.delete
        guessentry['state'] = DISABLED
        lives = (6)
        message = ('Better luck next time')
    elif len(guess) > 1:
        message = ('I\'m sorry, you can only guess one letter at a time')
    elif len(guess) < 1:
        message = ('You have to actually guess a letter')
    elif shownword == word:
        message = ('Great job!! One more round')
    else:
        if word.__contains__(guess):
            message = (f'That\'s correct, you still have {lives} lives.')
            guessedletter=(f'{guess}')
        elif guess not in word:
            lives -= 1
            message = (f'That is incorrect. You have {lives} lives left.')
            if lives == 0:
                message = (f'The word was {word}')
    #updates shownword
    letterpos = ([pos for pos, char in enumerate(word) if char==guessedletter])
    for ndx in letterpos:
        shownword = list(shownword)
        shownword[ndx] = guessedletter
        shownword = ''.join(shownword)
        wordshow['text'] = shownword
    outputlabel['text'] = message

#give a hint
def hint():
    global shownword, word, wordlength, hintsleft
    if hintsleft == 0:
        outputlabel['text'] = 'No more hints left'
        return
    hintpos = random.randint(0,wordlength - 1)
    hintletter = word[hintpos]
    if shownword == word:
        return
    while hintletter in shownword:
        hintpos = random.randint(0,wordlength - 1)
        hintletter = word[hintpos]
        print (hintletter)
    letterpos = ([pos for pos, char in enumerate(word) if char==hintletter])
    for ndx in letterpos:
        shownword = list(shownword)
        shownword[ndx] = hintletter
        shownword = ''.join(shownword)
        wordshow['text'] = shownword
    hintsleft = hintsleft - 1
    if shownword == word:
        guessentry.delete
        guessentry['state'] = DISABLED
        return

givehint = Button(root, text = 'Hint', command = hint)
givehint.place(relx = .6, rely = .4, anchor = CENTER)
    
confirmbutton = Button(root,text = 'Okay', command = updategame).place(relx= .5, rely= .2, anchor= CENTER)

playagain = Button(root, text = 'New game', command = newgame)
playagain.place(relx= .5, rely= .4, anchor= CENTER)

root.mainloop()