import random
def play():
      user=input("What's your choice('p' means paper,'r' means rock,'s' means scissor):")
      computer=random.choice(['p','r','s'])

      if user == computer:
          return 'It is a tie'
      #r>s,p>r,s>p
      if is_win(user,computer):
          return 'You Win!'
      else:
          return 'You Lost'
def is_win(player1,player2):
     # r>s,p>r,s>p
      if (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p'):
       return True
print(play())