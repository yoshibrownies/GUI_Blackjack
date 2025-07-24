from tkinter import *
from tkinter import messagebox
import pydealer as pd
'''
Version Two
- Using 1 Class
- Dealing
Player Actions
    - Hitting
    - Standing
    - Winning Conditions
'''

class Windows:
    def __init__(self):
        self.master=Tk()
        self.master.title('Blackjack')
        self.master.resizable(0,0)
        self.master.geometry("700x500") 

        # Main frame to hold everything
        self.main_frame = Frame(self.master, bg='white')
        self.main_frame.pack(fill=BOTH, expand=True)
        self.create_menu_window()
        self.master.mainloop()

    def create_menu_window(self):
        self.menu_frame=Frame(self.main_frame)
        self.menu_frame.pack(fill=BOTH, expand=True)
        # Adds a spacer frame to push buttons down
        self.spacer_frame = Frame(self.menu_frame, height=200)
        self.spacer_frame.pack()

        self.l_title=Label(self.spacer_frame, text='Black Jack', font='Arial 60 bold', fg='black')
        self.l_title.pack(pady=90, side=BOTTOM)

        # Creates a frame to hold the buttons
        self.button_frame = Frame(self.menu_frame)
        self.button_frame.pack(expand=True)  # Center the frame in the window

        
        # Buttons
        self.b_play = Button(self.button_frame, text='PLAY', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=lambda: self.open_window('Menu', 'Betting'))
        self.b_play.pack(side=LEFT, padx=30)

        self.b_help = Button(self.button_frame, text='HELP', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=lambda: self.open_window('Menu', 'Help'))
        self.b_help.pack(side=LEFT, padx=30)

    def create_help_window(self):
        self.help_frame=Frame(self.main_frame)
        self.help_frame.pack(fill=BOTH, expand=True)
        TITLE_STYLE = 'Arial 15 bold'

        # Header
        self.l_title = Label(self.help_frame, text='How To Play', font='Arial 35 bold', justify=CENTER)
        self.l_title.grid(row=0, columnspan=2)
        
        self.l_description = Label(self.help_frame, text='Objective: Beat the dealer by getting a hand value as close to 21 as possible without going over.\n')
        self.l_description.grid(row=1, columnspan=2, ipadx=10)

        # Card Values
        self.l_cardvalues = Label(self.help_frame, font=TITLE_STYLE, text='Card Values')
        self.l_cardvalues.grid(row=2, column=0, padx=10)

        self.l_cardvalues_description = Label(self.help_frame, text='Number Cards (2-10): Face Value\nFace Cards (King, Queen, Jack): Worth 10\nAces: Worth 1 or 11\n')
        self.l_cardvalues_description.grid(row=3, column=0, padx=10)

        # Game Setup
        self.l_gamesetup = Label(self.help_frame, font=TITLE_STYLE, text='Game Setup')
        self.l_gamesetup.grid(row=4, column=0, padx=10)

        self.l_gamesetup_description = Label(self.help_frame, text='1. You place a bet\n2. You and the dealer get two cards\n(your cards face up, dealer has one \nface up and one face down)\n')
        self.l_gamesetup_description.grid(row=5, column=0, padx=10)

        # Player Actions
        self.l_playeractions = Label(self.help_frame, font=TITLE_STYLE, text='Player Actions')
        self.l_playeractions.grid(row=6, column=0, padx=10)

        self.l_playeractions_description = Label(self.help_frame, text='Hit: Take another card\nStand: Keep your current hand\nDouble Down: Double your bet and take \none more card\nSplit: If you have two cards of the same value, \nsplit them into two hands for an additional bet\n')
        self.l_playeractions_description.grid(row=7, column=0, padx=10)

        # Dealer's Turn
        self.l_dealerturn = Label(self.help_frame, font=TITLE_STYLE, text="Dealer's Turn")
        self.l_dealerturn.grid(row=2, column=1, padx=10)

        self.l_dealerturn_description = Label(self.help_frame, text='The dealer reveals their hole card and \nmust hit until reaching 17 or higher.\n')
        self.l_dealerturn_description.grid(row=3, column=1, padx=10)

        # Winning
        self.l_winning = Label(self.help_frame, font=TITLE_STYLE, text='Winning')
        self.l_winning.grid(row=4, column=1, padx=10)

        self.l_winning_description = Label(self.help_frame, text="1. If your hand exceeds 21, you bust and lose\n2. If the dealer busts, remaining players win\n3. If your hand is closer to 21 than the dealer's,\n you win (payout is typically 1:1)\n4. A blackjack (Ace + 10-value card) usually pays 3:2\n5. A tie results in a push, and you get your bet back")
        self.l_winning_description.grid(row=5, column=1, padx=10)

        # Back Button
        self.b_back = Button(self.help_frame, text='BACK', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=lambda: self.open_window('Help', 'Menu'))
        self.b_back.grid(row=7, column=1, padx=30)
    
    def create_betting_window(self):
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

        self.b_bet = Button(self.betting_frame, text='BET', font='Arial 20 bold', fg='white', bg='#FFC300', width=9, command=lambda: self.open_window('Betting', 'Playing'))
        self.b_bet.pack(side=BOTTOM, pady=20)

    
    def create_playing_window(self):
        self.playing_frame=Frame(self.main_frame)
        self.playing_frame.pack(fill=BOTH, expand=True)
        
        # Crating and shuffling Deck
        self.deck=pd.Deck()
        self.deck.shuffle()

        # Creating hands
        self.dealer_hand = pd.Stack()
        self.player_hand = pd.Stack()

        self.deal_cards()
        self.player_total = self.calculate_hand_value(self.player_hand)
        self.dealer_total = self.calculate_hand_value(self.dealer_hand)

# Sectioning information with frames
        
    # Dealer Frame
        self.dealer_frame = Frame(self.playing_frame, bg='purple', height=50)
        self.dealer_frame.pack(fill=X, side=TOP)

    # Cards Frame
        self.cards_frame = Frame(self.playing_frame, bg='green')
        self.cards_frame.pack(fill=BOTH, expand=True)
        
        # Player Cards & Score
        self.l_player = Label(self.cards_frame, text=str(self.player_total))
        self.l_player.pack(side=BOTTOM)

        self.l_player_card = Label(self.cards_frame, text=f'{self.player_hand[0].value} of {self.player_hand[0].suit}')
        self.l_player_card.pack(side=BOTTOM)

        self.l_player_card = Label(self.cards_frame, text=f'{self.player_hand[1].value} of {self.player_hand[1].suit}')
        self.l_player_card.pack(side=BOTTOM)

        # Dealer Cards & Score
        self.l_dealer = Label(self.cards_frame, text=str(self.dealer_total))
        self.l_dealer.pack(side=TOP)

        self.l_dealer_card = Label(self.cards_frame, text=f'{self.dealer_hand[0].value} of {self.dealer_hand[0].suit}')
        self.l_dealer_card.pack(side=TOP)

    # Player Frame
        self.player_frame = Frame(self.playing_frame, bg='yellow', height=100)
        self.player_frame.pack(fill=X, side=BOTTOM)

        # Align buttons to the right within the player frame
        self.right_align = Frame(self.player_frame,)
        self.right_align.pack(side=RIGHT)

        self.b_hit = Button(self.right_align, text='HIT', font='Arial 20 bold', fg='white', bg='red', width=9, command=lambda: self.hit('Player'))
        self.b_hit.grid(column=1, row=0, padx=10)

        self.b_stand = Button(self.right_align, text='STAND', font='Arial 20 bold', fg='white', bg='green', width=9, command=self.stand)
        self.b_stand.grid(column=0, row=0, padx=10)

    def open_window(self, current_frame, window_name):
        # Destroys Open frame
        if current_frame == 'Menu':
            self.menu_frame.destroy()
        elif current_frame == 'Help':
            self.help_frame.destroy()
        elif current_frame == 'Betting':
            self.betting_frame.destroy()
        elif current_frame == 'Playing':
            self.playing_frame.destroy()

        # Opens new frame
        if window_name == 'Menu':
            self.create_menu_window()
        elif window_name == 'Help':
            self.create_help_window()
        elif window_name == 'Betting':
            self.create_betting_window()
        elif window_name == 'Playing':
            self.create_playing_window()

    def deal_cards(self):
        '''Deals Cards to hands'''
        self.player_hand += self.deck.deal(2)
        self.dealer_hand += self.deck.deal(1)
        
    def calculate_hand_value(self, hand):
        '''Calculates Hand Value'''
        value = 0
        aces = 0
        for card in hand:
            if card.value in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.value == 'Ace':
                aces +=1
                value += 11
            else:
                value += int(card.value)
        while value>21 and aces>0:
            # Changes ace value from 11 to 1 until no longer busting and no more aces
            value-=10 
            aces-=1
        return value
    
    def hit(self, person):
        '''Deals another card to hand'''
        if person == 'Player':
            if self.calculate_hand_value(self.player_hand)<=21: # Checking hand hasn't already busted
                self.player_hand += self.deck.deal(1)
                self.player_total = self.calculate_hand_value(self.player_hand)
                self.l_player_card = Label(self.cards_frame, text=f'{self.player_hand[-1].value} of {self.player_hand[-1].suit}')
                self.l_player_card.pack(side=BOTTOM)
                self.l_player.configure(text=str(self.player_total))
                if self.player_total > 21: # Checking if player busts
                    messagebox.showinfo("You Lost", "You Busted.")
                    # Creates play again button
                    self.b_replay = Button(self.cards_frame, text='PLAY AGAIN', font='Arial 20 bold', fg='white', bg='#FFC300', command=lambda: self.open_window('Playing', 'Betting'))
                    self.b_replay.place(relx= 0.5, rely=0.5, anchor=CENTER)
            else:
                messagebox.showerror("You Already Lost", "You cannot hit again.")

        if person == 'Dealer':
            self.dealer_hand += self.deck.deal(1)
            self.l_dealer_card = Label(self.cards_frame, text=f'{self.dealer_hand[-1].value} of {self.dealer_hand[-1].suit}')
            self.l_dealer_card.pack(side=TOP)
            self.l_dealer.configure(text=str(self.calculate_hand_value(self.dealer_hand)))

    def stand(self):
        '''Deals dealer until over 16 and determines who wins'''
        while self.calculate_hand_value(self.dealer_hand)<17:
            self.hit('Dealer')
        self.player_total = self.calculate_hand_value(self.player_hand)
        self.dealer_total = self.calculate_hand_value(self.dealer_hand) 
        if self.dealer_total > 21: # Checking if dealer busts
            messagebox.showinfo("You Win", "Dealer Busted.")
        
        # Winning Conditions
        elif self.player_total == self.dealer_total:
            messagebox.showinfo("Push", "You get your money back")
        elif self.player_total > self.dealer_total:
            messagebox.showinfo("You Win", "You Win.")
        elif self.player_total < self.dealer_total:
            messagebox.showinfo("You Lose", "Dealer Wins.")

        # Creates play again button 
        self.b_replay = Button(self.cards_frame, text='PLAY AGAIN', font='Arial 20 bold', fg='white', bg='#FFC300', command=lambda: self.open_window('Playing', 'Betting'))
        self.b_replay.place(relx= 0.5, rely=0.5, anchor=CENTER)

app=Windows()
        