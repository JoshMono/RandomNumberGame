from ast import Global
from asyncio.windows_events import NULL
from msilib.schema import File
import platform
import select
from tkinter import *
import random as random
from tkinter.ttk import Treeview
from turtle import back

score = 0
turn = 10

def PlayGame(PlayBTN, HighScoreBTN, Title, ClearData):
    PlayBTN.destroy()
    HighScoreBTN.destroy()
    Title.destroy()
    ClearData.destroy()
    
    global turn
    turn = 10
    
    global score
    score = 0
    
    Title = Label(root, text = "Guess A number (1-5)" ,fg = "black")
    Title.grid(column=2, row=1)
    
    ScoreLablel = Label(root, text = "Score" ,fg = "black")
    ScoreLablel.grid(column=4, row=0)
    
    Score = Label(root, text = "0" ,fg = "black")
    Score.grid(column=4, row=1)
    
    TurnLablel = Label(root, text = "Turn" ,fg = "black")
    TurnLablel.grid(column=3, row=0)
    
    Turn = Label(root, text = "10" ,fg = "black")
    Turn.grid(column=3, row=1)
    
    HigherLower = Label(root, text = "" ,fg = "black")
    HigherLower.grid(column=3, row=2)
    
    TextBox = Entry(root ,fg = "black")
    TextBox.grid(column=2, row=2)
    
    PlayBTN = Button(root, text = "Submit" ,fg = "black", command=lambda: SubmitNumber())
    PlayBTN.grid(column=2, row=3)    

    def SubmitNumber():
        global score
        global turn
        
        
        if TextBox.get() == '':
            pass
        
        else:
            try:
                if int(TextBox.get()) == 1 or int(TextBox.get()) == 2 or int(TextBox.get()) == 3 or int(TextBox.get()) == 4 or int(TextBox.get()) == 5:
                
                    if turn > 1:                
                        turn -= 1
                        Turn.config(text=str(turn))
                
                        randomNumber = random.randint(1,5)         

                        if randomNumber == int(TextBox.get()):
                            HigherLower.config(text='Correct')
                            score += 3
                            Score.config(text=str(score))

                        else:
                            if int(TextBox.get()) > randomNumber:
                                HigherLower.config(text='Too High')
                            else:
                                HigherLower.config(text='Too Low')
                        
                            score -= 1
                            Score.config(text=str(score))
                    
                    else:
                        turn -= 1
                        Turn.config(text=str(turn))
                
                        randomNumber = random.randint(1,5)        

                        if randomNumber == int(TextBox.get()):
                            score += 1
                            Score.config(text=str(score))

                        else:
                            score -= 1
                            Score.config(text=str(score))
                    
                        EndGame(score)
              
                else:
                    HigherLower.config(text='Put A Number From 1-5')
            
            except:
                HigherLower.config(text='Put A Number From 1-5')
    
    def EndGame(score):
        HigherLower.destroy()
        Title.destroy()
        ScoreLablel.destroy()
        Score.destroy()
        TurnLablel.destroy()
        Turn.destroy()
        TextBox.destroy()
        PlayBTN.destroy()
        UserInfo(score)
        
  
def HighScore(PlayBTN, HighScoreBTN, Title, ClearData):
    PlayBTN.destroy()
    HighScoreBTN.destroy()
    Title.destroy()
    ClearData.destroy()
    
    Title = Label(root, text = "High Score" ,fg = "black")
    Title.pack(side='top')

    treeView = Treeview(root, selectmode="browse")
    treeView.pack(side ='bottom')
    
    treeView["columns"] = ("1", "2")
    treeView['show'] = 'headings'
    
    treeView.column("1", width = 90, anchor ='c')
    treeView.column("2", width = 90, anchor ='c')
    
    treeView.heading("1", text ="Name")
    treeView.heading("2", text ="Score")
    
    backBTN = Button(root, text='Back', command=lambda: backToStart())
    backBTN.pack(side="bottom")

    def backToStart():
        treeView.destroy()
        backBTN.destroy()
        Title.destroy()
        StartUp()
    
    # file = open('dataBase.txt', 'a')

    # file.writelines(f"asdasd 100 \n")

    # file.close()



    name = ''
    score = ''
    testBool = True

    file = open('dataBase.txt', 'r')

    for i in file.readline():
        if testBool:
            if i == ':':
                testBool = False
            else:
                name = name + i
        else:
            if i == ';':
                testBool = True
                treeView.insert("", 'end', values =(f"{name}", f"{score}"))
                name = ''
                score = ''
            else:
                score = score + i
        
            
def UserInfo(score):
    Title = Label(root, text = "User Info")
    Title.grid(column=1, row=0)
    
    LabelUser = Label(root, text = "Enter Username")
    LabelUser.grid(column=0, row=1)
    
    Score = Label(root, text = f"Your socre was: {score}")
    Score.grid(column=1, row=1)

    Username = Entry(root, text = "Enter Username")
    Username.grid(column=0, row=2)
    
    SubmitBTN = Button(root, text = "Enter Username", command=lambda: SumbitInfo(score))
    SubmitBTN.grid(column=0, row=3)
    
    def SumbitInfo(score):
        if Username.get() != '':
            username = Username.get()
            file = open('dataBase.txt', 'a')
            file.write(f"{username}:{score};")
            file.close()
            Title.destroy()
            LabelUser.destroy()
            Username.destroy()
            SubmitBTN.destroy()
            Score.destroy()
            StartUp()

            


    

    

def StartUp():
    Title = Label(root, text = "Random Guessing Game" ,fg = "black")
    HighScoreBTN = Button(root, text = "HighScore" ,fg = "black", command=lambda: HighScore(PlayBTN, HighScoreBTN, Title, ClearDataBTN))
    PlayBTN = Button(root, text = "Play" ,fg = "black", command=lambda: PlayGame(PlayBTN, HighScoreBTN, Title, ClearDataBTN))
    ClearDataBTN = Button(root, text = "Clear Data" ,fg = "black", command=lambda: ClearData())

    PlayBTN.grid(column=1, row=1)
    HighScoreBTN.grid(column=3, row=1)
    Title.grid(column=2, row=0)
    ClearDataBTN.grid(column=3, row=5)


    def ClearData():
        file = open('dataBase.txt', 'w')
        file.write("")
        file.close()

root = Tk()
root.geometry('300x300')

StartUp()

root.mainloop()





# file = open('dataBase.txt', 'r')




# for i in file.readlines():
#     stringName = i
#     print(i)
    



