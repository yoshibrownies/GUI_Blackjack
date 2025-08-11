from tkinter import *
from tkinter import messagebox
import pydealer as pd
import json as j
from PIL import Image, ImageTk
'''
Version Three
- Error Proof
- Images
'''

class Windows:
    def __init__(self):
        self.master=Tk()
        self.master.title('Blackjack')
        self.master.resizable(0,0)
        self.master.geometry("700x500") 

        with open('Gamehistory.json', 'r') as f: # Getting information from gamehistory file
            self.data = j.load(f)

        # Main frame to hold everything
        self.main_frame = Frame(self.master)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.BUTTON_FONT = 'Arial 20 bold'
        self.YELLOW = '#FFC300'

        self.create_menu_window()
        self.master.mainloop()

    def create_menu_window(self):
        '''Creates menu frame'''
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
        self.b_play = Button(self.button_frame, text='PLAY', font=self.BUTTON_FONT, fg='white', bg=self.YELLOW, width=9, command=lambda: self.open_window('Menu', 'Profile'))
        self.b_play.pack(side=LEFT, padx=30)

        self.b_help = Button(self.button_frame, text='HELP', font=self.BUTTON_FONT, fg='white', bg=self.YELLOW, width=9, command=lambda: self.open_window('Menu', 'Help'))
        self.b_help.pack(side=LEFT, padx=30)

    def create_help_window(self):
        '''Creates help frame'''
        self.help_frame = Frame(self.main_frame)
        self.help_frame.pack(fill=BOTH, expand=True)
        TITLE_STYLE = 'Arial 15 bold'

        # Centering all information
        self.center_frame = Frame(self.help_frame)
        self.center_frame.pack(side=TOP)

        # Header
        self.l_title = Label(self.center_frame, text='How To Play', font='Arial 35 bold', justify=CENTER)
        self.l_title.grid(row=0, columnspan=2)
        
        self.l_description = Label(self.center_frame, text='Objective: Beat the dealer by getting a hand value as close to 21 as possible without going over.\n')
        self.l_description.grid(row=1, columnspan=2)

        # Card Values
        self.l_cardvalues = Label(self.center_frame, font=TITLE_STYLE, text='Card Values')
        self.l_cardvalues.grid(row=2, column=0, padx=10)

        self.l_cardvalues_description = Label(self.center_frame, text='Number Cards (2-10): Face Value\nFace Cards (King, Queen, Jack): Worth 10\nAces: Worth 1 or 11\n')
        self.l_cardvalues_description.grid(row=3, column=0, padx=10)

        # Game Setup
        self.l_gamesetup = Label(self.center_frame, font=TITLE_STYLE, text='Game Setup')
        self.l_gamesetup.grid(row=4, column=0, padx=10)

        self.l_gamesetup_description = Label(self.center_frame, text='1. You place a bet\n2. You and the dealer get two cards\n(your cards face up, dealer has one \nface up and one face down)\n')
        self.l_gamesetup_description.grid(row=5, column=0, padx=10)

        # Player Actions
        self.l_playeractions = Label(self.center_frame, font=TITLE_STYLE, text='Player Actions')
        self.l_playeractions.grid(row=6, column=0, padx=10)

        self.l_playeractions_description = Label(self.center_frame, text='Hit: Take another card\nStand: Keep your current hand\nDouble Down: Double your bet and take \none more card\nSplit: If you have two cards of the same value, \nsplit them into two hands for an additional bet\n')
        self.l_playeractions_description.grid(row=7, column=0, padx=10)

        # Dealer's Turn
        self.l_dealerturn = Label(self.center_frame, font=TITLE_STYLE, text="Dealer's Turn")
        self.l_dealerturn.grid(row=2, column=1, padx=10)

        self.l_dealerturn_description = Label(self.center_frame, text='The dealer reveals their hole card and \nmust hit until reaching 17 or higher.\n')
        self.l_dealerturn_description.grid(row=3, column=1, padx=10)

        # Winning
        self.l_winning = Label(self.center_frame, font=TITLE_STYLE, text='Winning')
        self.l_winning.grid(row=4, column=1, padx=10)

        self.l_winning_description = Label(self.center_frame, text="1. If your hand exceeds 21, you bust and lose\n2. If the dealer busts, remaining players win\n3. If your hand is closer to 21 than the dealer's,\n you win (payout is typically 1:1)\n4. A blackjack (Ace + 10-value card) usually pays 3:2\n5. A tie results in a push, and you get your bet back")
        self.l_winning_description.grid(row=5, column=1, padx=10)

        # Back Button
        self.b_back = Button(self.center_frame, text='BACK', font=self.BUTTON_FONT, fg='white', bg='red', width=9, command=lambda: self.open_window('Help', 'Menu'))
        self.b_back.grid(row=7, column=1, padx=30)
    
    def create_betting_window(self):
        '''Creates Betting frame'''
        self.betting_frame=Frame(self.main_frame)
        self.betting_frame.pack(fill=BOTH, expand=True)

        self.l_balance = Label(self.betting_frame, text=f"Balance: ${self.data[self.profile.get()]['Balance']}", font=self.BUTTON_FONT)
        self.l_balance.pack(side=TOP, fill=X, pady=10)

        # Creates a frame to centre betting amount
        self.center_frame = Frame(self.betting_frame)
        self.center_frame.pack(expand=True)  # Center the frame in the window

        # Betting Amount 
        self.l_bet_title = Label(self.center_frame, text='Betting Amount: $', font='Arial 20 bold')
        self.l_bet_title.pack(side=LEFT)

        self.e_bet_amount = Entry(self.center_frame, font='Arial 25 bold')
        self.e_bet_amount.pack(side=LEFT)

        # Buttons
        self.button_frame = Frame(self.betting_frame)
        self.button_frame.pack(side=BOTTOM, pady=20)

        self.b_back = Button(self.button_frame, text='BACK', font=self.BUTTON_FONT, fg='white', bg='red', width=9, command=lambda: self.open_window('Betting','Menu'))
        self.b_back.pack(side=LEFT, padx=30)

        self.b_bet = Button(self.button_frame, text='BET', font=self.BUTTON_FONT, fg='white', bg='green', width=9, command=self.bet)
        self.b_bet.pack(side=LEFT, padx=30)
    
    def create_playing_window(self):
        '''Creates playing frame'''
        self.playing_frame=Frame(self.main_frame)
        self.playing_frame.pack(fill=BOTH, expand=True)
        
        # Creating and shuffling Deck
        self.deck=pd.Deck()
        self.deck.shuffle()

        # Creating hands
        self.dealer_hand = pd.Stack()
        self.player_hand = pd.Stack()

        # Deals initial cards
        self.player_hand += self.deck.deal(2)
        self.dealer_hand += self.deck.deal(1)
        self.player_total = self.calculate_hand_value(self.player_hand)
        self.dealer_total = self.calculate_hand_value(self.dealer_hand)

# Sectioning information with frames
        
    # Dealer Frame
        self.dealer_frame = Frame(self.playing_frame, bg='green', height=50)
        self.dealer_frame.pack(fill=X, side=TOP)

        self.l_dealer_title = Label(self.dealer_frame, bg='green', text='Dealer', font='Arial 20 bold')
        self.l_dealer_title.pack()

    # Cards Frame
        self.cards_frame = Frame(self.playing_frame, bg='green')
        self.cards_frame.pack(fill=BOTH, expand=True)
        
        # Player Cards & Score
        self.l_player_total = Label(self.cards_frame, text=str(self.player_total), bg='green', font='Arial 15 bold', pady=10)
        self.l_player_total.pack(side=BOTTOM)
        
        self.player_cards_frame = Frame(self.cards_frame, bg='white')
        self.player_cards_frame.pack(side=BOTTOM)

        self.player_card_images = []
        # Displaying player cards as images
        for card in self.player_hand:
            self.player_card_images.append(self.get_card_image(card))

        self.l_player_card = Label(self.player_cards_frame, image=self.player_card_images[0], bg='green')
        self.l_player_card.pack(side=LEFT)

        self.l_player_card = Label(self.player_cards_frame, image=self.player_card_images[1], bg='green')
        self.l_player_card.pack(side=LEFT)

        # Dealer Cards & Score
        self.l_dealer_total = Label(self.cards_frame, text=str(self.dealer_total), bg='green', font='Arial 15 bold', pady=10)
        self.l_dealer_total.pack(side=TOP)

        self.dealer_cards_frame = Frame(self.cards_frame, bg='white')
        self.dealer_cards_frame.pack(side=TOP)

        self.dealer_card_images = []
        # Displaying dealer cards as images
        for card in self.dealer_hand:
            self.dealer_card_images.append(self.get_card_image(card))

        self.l_dealer_card = Label(self.dealer_cards_frame, image=self.dealer_card_images[0], bg='green')
        self.l_dealer_card.pack(side=LEFT)

    # Player Actions Frame
        self.actions_frame = Frame(self.playing_frame, bg='green', height=100)
        self.actions_frame.pack(fill=X, side=BOTTOM)

        # Align buttons to the right within the player frame
        self.right_align = Frame(self.actions_frame, bg='green')
        self.right_align.pack(side=RIGHT)

        self.b_hit = Button(self.right_align, text='HIT', font=self.BUTTON_FONT, fg='white', bg='red', width=9, command=lambda: self.hit('Player'))
        self.b_hit.grid(column=1, row=0, padx=10, pady=5)

        self.b_stand = Button(self.right_align, text='STAND', font=self.BUTTON_FONT, fg='white', bg='green', width=9, command=self.stand)
        self.b_stand.grid(column=0, row=0, padx=10, pady=5)

    def create_profile_window(self):
            '''Creates profile frame'''
            self.profile_frame = Frame(self.main_frame)
            self.profile_frame.pack(fill=BOTH, expand=True)

            self.l_title = Label(self.profile_frame, text='Profiles', font='Arial 40 bold', pady=30)
            self.l_title.pack(side=TOP)

            self.profile = StringVar()

            self.l_current = Label(self.profile_frame, text='Selected Profile:', font='Arial 10')
            self.l_current.pack(side=TOP)

            self.l_current_profile = Label(self.profile_frame, textvariable=self.profile, font='Arial 10 bold', fg='green')
            self.l_current_profile.pack(side=TOP)

            # Centering 
            self.center_frame = Frame(self.profile_frame)
            self.center_frame.pack(fill=X, side=TOP, pady=40)

            # Loops through all profiles
            for key, value in self.data.items():
                self.individual_profile = Frame(self.center_frame, padx=65,)
                self.individual_profile.pack(side=LEFT)

                self.individual_profile.rowconfigure([0,1,2,3], minsize=10)

                self.l_title = Label(self.individual_profile, text=key, font='Arial 20 bold')
                self.l_title.grid(columnspan=2, row=0)

                self.l_balance = Label(self.individual_profile, text='Balance:')
                self.l_balance.grid(column=0, row=2)

                self.l_balance_amount = Label(self.individual_profile, text=f'${value["Balance"]}')
                self.l_balance_amount.grid(column=1, row=2)

                self.l_wins = Label(self.individual_profile, text='Wins:')
                self.l_wins.grid(column=0, row=3)

                self.l_wins_amount = Label(self.individual_profile, text=value["Wins"], fg='green')
                self.l_wins_amount.grid(column=1, row=3)

                self.l_losses = Label(self.individual_profile, text='Losses:')
                self.l_losses.grid(column=0, row=4)

                self.l_losses_amount = Label(self.individual_profile, text=value["Losses"], fg='red')
                self.l_losses_amount.grid(column=1, row=4)

                self.l_winrate = Label(self.individual_profile, text='Winrate:')
                self.l_winrate.grid(column=0, row=5)
                
                # Calculating winrate
                if value["Games"]>0:
                    winrate_percent = value["Wins"]/value["Games"]*100
                else:
                    winrate_percent = 0

                self.l_winrate_number = Label(self.individual_profile, text=f'{round(winrate_percent, 1)}%', fg='blue')
                self.l_winrate_number.grid(column=1, row=5)

                self.l_winstreak = Label(self.individual_profile, text='Winstreak:')
                self.l_winstreak.grid(column=0, row=6)

                self.l_winstreak_number = Label(self.individual_profile, text=value['Winstreak'], fg='blue', font='Arial 10 bold')
                self.l_winstreak_number.grid(column=1, row=6)

                self.radio = Radiobutton(self.individual_profile, variable=self.profile, value=key)
                self.radio.grid(columnspan=2, row=7)
            
            self.profiles = list(self.data.keys())
            self.profile.set(self.profiles[0]) # Sets first profile as default

            self.button_frame = Frame(self.profile_frame)
            self.button_frame.pack(side=TOP)

            self.b_back = Button(self.button_frame, text='BACK', font=self.BUTTON_FONT, fg='white', bg='red', width=9, command=lambda: self.open_window('Profile', 'Menu'))
            self.b_back.pack(side=LEFT, padx=30)

            self.b_play = Button(self.button_frame, text='PLAY', font=self.BUTTON_FONT, fg='white', bg='green', width=9, command=lambda: self.open_window('Profile','Betting'))
            self.b_play.pack(side=LEFT, padx=30)
    def open_window(self, current_frame, window_name):
        '''Opens new frames and destroys previously open one'''

        current_frame.title()
        window_name.title()

        # Destroys Open frame
        if current_frame == 'Menu':
            self.menu_frame.destroy()
        elif current_frame == 'Help':
            self.help_frame.destroy()
        elif current_frame == 'Profile':
            self.profile_frame.destroy()
        elif current_frame == 'Betting':
            try: # Avoiding value error from empty bet amount entry box
                self.bet_amount = int(self.e_bet_amount.get())
            except:
                pass
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
        elif window_name == 'Profile':
            self.create_profile_window()
    
    def bet (self):
        '''Checks Betting amount is valid and opens window if so'''
        try:
            if int(self.e_bet_amount.get())>self.data[self.profile.get()]['Balance']:
                messagebox.showerror('Error', 'Bet is higher than your balance. Enter lower bet.')
            elif int(self.e_bet_amount.get())<=0:
                messagebox.showerror('Error', 'Bet must be greater than 0.')
            else:
                self.open_window('Betting', 'Playing')
        except ValueError:
            messagebox.showerror('Error', 'Enter only whole numbers.')

    def calculate_hand_value(self, hand):
        '''Calculates Hand Value'''
        value = 0
        aces = 0
        for card in hand: # Loops through each card in given hand
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
            self.player_hand += self.deck.deal(1)
            self.player_total = self.calculate_hand_value(self.player_hand)

                # Displaying player cards as images
            self.player_card_images.append(self.get_card_image(self.player_hand[-1]))
            self.l_player_card = Label(self.player_cards_frame, image=self.player_card_images[-1], bg='green')
            self.l_player_card.pack(side=LEFT)

            self.l_player_total.configure(text=str(self.player_total))
            if self.player_total > 21: # Checking if player busts
                messagebox.showinfo("You Busted", f"-${self.bet_amount}")
                self.win_or_loss('Loss')
                # Creates play again button
                self.play_again()

        elif person == 'Dealer':
            # Dealing & showing dealer hand
            self.dealer_hand += self.deck.deal(1)

            # Displaying dealer cards as images
            self.dealer_card_images.append(self.get_card_image(self.dealer_hand[-1]))
            self.l_dealer_card = Label(self.dealer_cards_frame, image=self.dealer_card_images[-1], bg='green')
            self.l_dealer_card.pack(side=LEFT)

            self.l_dealer_total.configure(text=str(self.calculate_hand_value(self.dealer_hand)))

    def win_or_loss(self, outcome):
        '''Adds or removes bet amount to profile balance'''
        outcome.title()
        if outcome == 'Loss':
            self.data[self.profile.get()]['Balance'] -= self.bet_amount
            self.data[self.profile.get()]['Losses'] += 1
            self.data[self.profile.get()]['Winstreak'] = 0
            
        elif outcome == 'Win':
            self.data[self.profile.get()]['Balance'] += self.bet_amount
            self.data[self.profile.get()]['Wins'] += 1
            self.data[self.profile.get()]['Winstreak'] += 1
        self.data[self.profile.get()]['Games']+=1
        self.save()

    def stand(self):
        '''Deals dealer and determines who wins'''
        while self.calculate_hand_value(self.dealer_hand)<17: # Hits dealer until above 16
            self.hit('Dealer')
        self.player_total = self.calculate_hand_value(self.player_hand)
        self.dealer_total = self.calculate_hand_value(self.dealer_hand) 

        # Winning Conditions
        if self.dealer_total > 21:
            messagebox.showinfo("Dealer Busted", f"+${self.bet_amount}")
            self.win_or_loss('Win')
        elif self.player_total < self.dealer_total:
            messagebox.showinfo(f"You Lose", f"-${self.bet_amount}")
            self.win_or_loss('Loss')
        elif self.player_total > self.dealer_total:
            messagebox.showinfo(f"You Win", f"+${self.bet_amount}")
            self.win_or_loss('Win')
        elif self.player_total == self.dealer_total:
            messagebox.showinfo("Push", f"+$0")
            self.win_or_loss('Push')
        # Creates play again button 
        self.play_again()
    
    def save(self):
        '''Saves data'''
        # Saves to gamehistory file
        with open('Gamehistory.json', 'w') as f:
            j.dump(self.data, f, indent=4)

    def play_again(self):
        '''Creates Play Again or Create New Account Button'''
        if self.data[self.profile.get()]['Balance']>0:
            # Creates play again button 
                self.b_replay = Button(self.cards_frame, text='PLAY AGAIN', font=self.BUTTON_FONT, fg='white', bg=self.YELLOW, command=lambda: self.open_window('Playing', 'Betting'))
                self.b_replay.place(relx= 0.5, rely=0.5, anchor=CENTER)
        else:
            # Resets profile
            messagebox.showinfo('No Money','Account Balance = 0')
            self.b_replay = Button(self.cards_frame, text='CREATE NEW ACCOUNT', font=self.BUTTON_FONT, fg='white', bg=self.YELLOW, command=lambda: self.open_window('Playing', 'Betting'))
            self.b_replay.place(relx= 0.5, rely=0.5, anchor=CENTER)
            self.data[self.profile.get()]['Balance'] = 1000
            self.data[self.profile.get()]['Wins'] = 0
            self.data[self.profile.get()]['Losses'] = 0
            self.data[self.profile.get()]['Games'] = 0
            self.data[self.profile.get()]['Winstreak'] = 0
            self.save()

        self.right_align.destroy()
        self.b_menu = Button(self.actions_frame, text='MENU', font=self.BUTTON_FONT, fg='white', bg='red', width=9, command=lambda: self.open_window('Playing', 'Menu'))
        self.b_menu.pack(pady=10)

    def get_card_image(self, card):
        '''Gets image for card'''
        try:
            if card.value == "10":
                original_image = Image.open(f"PNG/10{card.suit[0]}.png")
            else:
                original_image = Image.open(f"PNG/{card.value[0]}{card.suit[0]}.png")
            
            original_image = original_image.resize((70, 105), Image.LANCZOS)
            return ImageTk.PhotoImage(original_image)
        except FileNotFoundError:
            print('File not Found')

app=Windows()