import random

suits =("Hearts","Diamonds","Spades","Clubs")
ranks =("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.player_cards=[]

    def remove_card(self):
        return self.player_cards.pop(0)

    def add_card(self,new_card):
        if type(new_card)==type([]):
            self.player_cards.extend(new_card)
        else:
            self.player_cards.append(new_card)

    def __str__(self):
        return f"{self.name} has {len(self.player_cards)} cards"

player_one=Player("One")
player_two=Player("Two")
new_deck=Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_card(new_deck.deal())
    player_two.add_card(new_deck.deal())

game_on=True
round_no=0
MAX_ROUNDS = 10000

while game_on:
    round_no+=1
    print(f"Round {round_no}")
    if round_no > MAX_ROUNDS:
        print("Maximum rounds reached — likely a draw or loop.")
        break

    if len(player_one.player_cards)==0:
        print("Player One has no cards! Player Two wins")
        game_on=False
        break

    if len(player_two.player_cards)==0:
        print("Player Two has no cards! Player One wins")
        game_on=False
        break

    player_one_cards=[]
    player_one_cards.append(player_one.remove_card())
    player_two_cards=[]
    player_two_cards.append(player_two.remove_card())

    at_war=True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war=False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war=False

        else:
            print("WAR!")
            if len(player_one.player_cards)<5:
                print("Player One unable to declare war")
                print("Player Two Wins!!")
                game_on=False
                break

            if len(player_two.player_cards)<5:
                print("Player Two unable to declare war")
                print("Player One Wins!!")
                game_on=False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())