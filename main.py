from replit import clear
from art import logo

bidding_finished = False                    
  
bids = {}

def find_highest_bid(bids):
  highest_bid = 0
  winner = ''
  for key in bids:
    if bids[key] > highest_bid:
       winner = key
       highest_bid = bids[key]
  print(f'The winner is {winner} with bid price of ${highest_bid}')

print(logo)
print('This is the secret auction game')

while not bidding_finished:
  name = input('What is your name: ')
  bid = int(input('What is your bid: $'))
  bids[name] = bid
  answer = input('Do you wanna keep on: Type \'yes\' or \'no\': ')
  if answer == 'no':
    bidding_finished = True
  elif answer == 'yes':
    clear()


find_highest_bid(bids)