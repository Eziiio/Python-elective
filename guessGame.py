from breezypythongui import EasyFrame

import random



class guessGame(EasyFrame):

    def __init__(self):

        EasyFrame.__init__(self,title="Number Guess Game",width=300,height=150)

        self.myNumber=random.randint(1,100)

        self.count=0

        self.l1=self.addLabel(text="Guess a number btw 1 and 100", row=0, column=0, columnspan=2, sticky="NSEW")

        self.addLabel(text="Your Guess", row=1,column=0)

        self.t1=self.addIntegerField(value=0,row=1,column=1, width=10)

        self.next=self.addButton(text="Next", row=2, column=0, command=self.NextB)

        self.new=self.addButton(text="New Game", row=2, column=1, command=self.NewGame)



    def NextB(self):

        self.count+=1

        n=self.t1.getNumber()

        if n==self.myNumber:

            self.l1["text"]="You've guessed it in "+str(self.count)+" attempts"

            self.next["state"]="disabled"

        elif n<self.myNumber:

            self.l1["text"]="Guess is too small"

        elif n>self.myNumber:

            self.l1["text"]="Guess is too Large"



    def NewGame(self):

        self.myNumber = random.randint(1, 100)

        self.count = 0

        self.l1["text"] = "Guess a number between 1 and 100"

        self.t1.setNumber(0)  

        self.next["state"] = "normal"

guessGame().mainloop()

    
