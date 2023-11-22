import subprocess
from secret_auct_art import logo

print(logo)

print("Welcome to the Secret Auction\n")

def highest_bid(para_bids):
  high_bid = 0
  winner = " "
  for bidder in para_bids:
    bid_amount = para_bids[bidder]
    if bid_amount > high_bid:
      high_bidder = bidder
      high_bid = bid_amount

  print(f"The highest bidder is {high_bidder} and highest bid is {high_bid} ")

bids = {}
should_continue = True
while should_continue:
  #problem: if names are repeated it will update to the latest value
  name = input("What is your name?")
  bid = int(input("What is your bid?"))
  bids[name] = bid
  restart= input("if you wish to continue, type 'yes' else type 'no'")
  if restart == "no":
    should_continue = False
    subprocess.call(['clear'])
    highest_bid(bids)
  elif restart == "yes":
    should_continue == True
    subprocess.call(['clear'])


    




