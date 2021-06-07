# Card Games
# By Linh Vuong
# 52 cards
# A,2,3,..10, J,Q,K
# c:clubs, h:hearts, s:spades,d:diamonds
import random
player1=[]
player2=[]
## STEP 1: Generate the deck
def deck_generate():
    deck=[]
    for i in range(1,14):
        for item in ["c","h","s","d"]:
            deck.append("%02d"%i+" "+item)
    return deck
## STEP 2: Shuffle the deck
def deck_shuffle(deck):
    random.shuffle(deck)
    return deck
## STEP 3: Deliver the deck
def deck_deliver(deck,n):
    for i in range(1,n+1):
        player1.append(deck.pop())
        player2.append(deck.pop())
    return deck
my_deck=deck_generate()
print(my_deck)
my_deck=deck_shuffle(my_deck)
my_deck=deck_deliver(my_deck,5)
print("* player2:",player2)
print("*"*10+" after sorting ...")
player1.sort()
player2.sort()
print("* player2:",player2)
computer_cards_begin=[]
player_cards_begin= []
for item in player1:
    computer_cards_begin.append(item)
for item in player2:
    player_cards_begin.append(item)

## STEP 4
# Start playing
computer_win_round=0 #store win rounds
player_win_round=0
player_cards=[]
computer_cards=[]
#-----------------------------
# round 1: 
# computer's card
random.shuffle(player1)
computer_round1=player1.pop()
#print("First round: computer's card is: %2d"%computer_round1)

# player's card
print("\n\n"+"*"*10+" START THE GAME"+"*"*10)
print("You have cards:")
print(player2)

for j in range (0,5):
    temp="Please select one card from your hand by pick an index number ("
    for i in range (len(player2)):
        temp+=str(i+1)+","
    temp+=")"
    print(temp)

    # input
    player_pick=int(input())
    player_round1=player2.pop(player_pick-1)
    #print("First round: player's card is:")

    #show 2 cards
    print("Computer's card:" +computer_round1)
    computer_cards.append(computer_round1)
    
    print("Player's card: " +player_round1)
    player_cards.append(player_round1)

    #compare two cards
    letter_player1=player_round1[3:4]
    
    letter_computer1=computer_round1[3:4]
    
    res_computer1 = [int(i) for i in computer_round1.split() if i.isdigit()] 
    res_player1 = [int(i) for i in player_round1.split() if i.isdigit()] 

    ## STEP 5 - 6
    if res_player1>res_computer1:
        print("You win round %1d, congratulation!"%(j+1))
        player_win_round+=1

    elif res_player1<res_computer1:
        print("Computer win round %1d"%(j+1))
        computer_win_round+=1
    else: # s, c, d, h
        if letter_player1=='s':
            compare_player1=1
        if letter_player1=='c':
            compare_player1=2
        if letter_player1=='d':
            compare_player1=3
        if letter_player1=='h':
            compare_player1=1
        if letter_computer1=='s':
            compare_computer1=1
        if letter_computer1=='c':
            compare_computer1=2
        if letter_computer1=='d':
            compare_computer1=3
        if letter_computer1=='h':
            compare_computer1=4
        if compare_player1>compare_computer1:
            print("You win round %1d, congratulation!"%(j+1))
        else:
            print("Computer win round %1d"%(j+1))

    #-----------------------------

# Step 7
if computer_win_round>player_win_round:
    print("\n\nCOMPUTER WON this Game")
else:
    print("\n\nYOU WON this Game")

# Step 8
print("Computer holds cards:")
print(computer_cards_begin)
print("Player holds cards:")
print(player_cards_begin)

print("Five Rounds: %2d %2d %2d %2d %2d"%(1,2,3,4,5))
print("Computer   :"+computer_cards[0]+" "+computer_cards[1]+" "+computer_cards[2]+" "+computer_cards[3]+" "+computer_cards[4])
print("Player     :"+player_cards[0]+ " "+player_cards[1]+" "+player_cards[2]+" "+player_cards[3]+" "+player_cards[4])