from tkinter import *
'''
Version One
Basic set up's of screens
- Menu Screen
- Help & Information Screen
- Game Screen (Both Frames)
'''

class MainWindow:
    def __init__(self):
        self.master=Tk()
        self.master.title('Menu')
        self.master.resizable(0,0)
        self.master.geometry("700x500") 

        # Adds a spacer frame to push buttons down
        self.spacer_frame = Frame(self.master, height=200)
        self.spacer_frame.pack()

        self.l_title=Label(self.spacer_frame, text='Black Jack', font='Arial 60 bold', fg='black')
        self.l_title.pack(pady=90, side=BOTTOM)

        # Creates a frame to hold the buttons
        self.button_frame = Frame(self.master)
        self.button_frame.pack(expand=True)  # Center the frame in the window

        
        # Buttons
        self.b_play = Button(self.button_frame, text='PLAY', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=self.open_gamewindow)
        self.b_play.pack(side=LEFT, padx=30)

        self.b_help = Button(self.button_frame, text='HELP', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=self.open_helpwindow)
        self.b_help.pack(side=LEFT, padx=30)

        self.master.mainloop()

    def open_helpwindow(self):
        self.master.destroy()
        HelpWindow()

    def open_gamewindow(self):
        self.master.destroy()
        GameWindow()  

class HelpWindow:
    def __init__(self):
        self.master=Tk()
        self.master.title('Help & Information')
        self.master.resizable(0,0)
        TITLE_STYLE = 'Arial 15 bold'

        # Header
        self.l_title = Label(self.master, text='How To Play', font='Arial 35 bold', justify=CENTER)
        self.l_title.grid(row=0, columnspan=2)
        
        self.l_description = Label(self.master, text='Objective: Beat the dealer by getting a hand value as close to 21 as possible without going over.\n')
        self.l_description.grid(row=1, columnspan=2, ipadx=10)

        # Card Values
        self.l_cardvalues = Label(self.master, font=TITLE_STYLE, text='Card Values')
        self.l_cardvalues.grid(row=2, column=0, padx=10)

        self.l_cardvalues_description = Label(self.master, text='Number Cards (2-10): Face Value\nFace Cards (King, Queen, Jack): Worth 10\nAces: Worth 1 or 11\n')
        self.l_cardvalues_description.grid(row=3, column=0, padx=10)

        # Game Setup
        self.l_gamesetup = Label(self.master, font=TITLE_STYLE, text='Game Setup')
        self.l_gamesetup.grid(row=4, column=0, padx=10)

        self.l_gamesetup_description = Label(self.master, text='1. You place a bet\n2. You and the dealer get two cards\n(your cards face up, dealer has one \nface up and one face down)\n')
        self.l_gamesetup_description.grid(row=5, column=0, padx=10)

        # Player Actions
        self.l_playeractions = Label(self.master, font=TITLE_STYLE, text='Player Actions')
        self.l_playeractions.grid(row=6, column=0, padx=10)

        self.l_playeractions_description = Label(self.master, text='Hit: Take another card\nStand: Keep your current hand\nDouble Down: Double your bet and take \none more card\nSplit: If you have two cards of the same value, \nsplit them into two hands for an additional bet\n')
        self.l_playeractions_description.grid(row=7, column=0, padx=10)

        # Dealer's Turn
        self.l_dealerturn = Label(self.master, font=TITLE_STYLE, text="Dealer's Turn")
        self.l_dealerturn.grid(row=2, column=1, padx=10)

        self.l_dealerturn_description = Label(self.master, text='The dealer reveals their hole card and \nmust hit until reaching 17 or higher.\n')
        self.l_dealerturn_description.grid(row=3, column=1, padx=10)

        # Winning
        self.l_winning = Label(self.master, font=TITLE_STYLE, text='Winning')
        self.l_winning.grid(row=4, column=1, padx=10)

        self.l_winning_description = Label(self.master, text="1. If your hand exceeds 21, you bust and lose\n2. If the dealer busts, remaining players win\n3. If your hand is closer to 21 than the dealer's,\n you win (payout is typically 1:1)\n4. A blackjack (Ace + 10-value card) usually pays 3:2\n5. A tie results in a push, and you get your bet back")
        self.l_winning_description.grid(row=5, column=1, padx=10)

        # Back Button
        self.b_back = Button(self.master, text='BACK', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=self.open_mainwindow)
        self.b_back.grid(row=7, column=1, padx=30)

        self.master.mainloop()

    def open_mainwindow(self):
        self.master.destroy()
        MainWindow() 
    
class GameWindow:
    def __init__(self):
        self.master=Tk()
        self.master.title('Blackjack')
        self.master.resizable(0,0)
        self.master.geometry("700x500") 

        # Main frame to hold everything
        self.main_frame = Frame(self.master, bg='white')
        self.main_frame.pack(fill=BOTH, expand=True)

        self.create_betting_frame()

        self.master.mainloop()

    def open_playing_frame(self):
        # Destroys frame and create new one
        self.betting_frame.destroy()
        self.create_playing_frame()

    def create_betting_frame(self):
        self.betting_frame=Frame(self.main_frame)
        self.betting_frame.pack(fill=BOTH, expand=True)

        # Creates a frame to centre betting amount
        self.center_frame = Frame(self.betting_frame)
        self.center_frame.pack(expand=True)  # Center the frame in the window

        # Betting Amount 
        self.l_bet_title = Label(self.center_frame, text='Betting Amount: $', font='Arial 20 bold')
        self.l_bet_title.pack(side=LEFT)

        self.e_bet_amount = Entry(self.center_frame, font='Arial 25 bold')
        self.e_bet_amount.pack(side=LEFT)

        self.b_bet = Button(self.betting_frame, text='BET', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=self.open_playing_frame)
        self.b_bet.pack(side=BOTTOM, pady=20)

    
    def create_playing_frame(self):
        self.playing_frame=Frame(self.main_frame)
        self.playing_frame.pack(fill=BOTH, expand=True)

        # Sectioning information with frames
        self.dealer_frame = Frame(self.playing_frame, bg='purple', height=50)
        self.dealer_frame.pack(fill=X, side=TOP)

        self.cards_frame = Frame(self.playing_frame, bg='green')
        self.cards_frame.pack(fill=BOTH, expand=True)

        self.player_frame = Frame(self.playing_frame, bg='yellow', height=100)
        self.player_frame.pack(fill=X, side=BOTTOM)

        # Align buttons to the right within the player frame
        self.right_align = Frame(self.player_frame,)
        self.right_align.pack(side=RIGHT)

        self.b_hit = Button(self.right_align, text='HIT', font='Arial 20 bold', fg='white', bg='red', width=9)
        self.b_hit.grid(column=1, row=0, padx=10)

        self.b_stand = Button(self.right_align, text='STAND', font='Arial 20 bold', fg='white', bg='green', width=9)
        self.b_stand.grid(column=0, row=0, padx=10)


app=MainWindow()
        