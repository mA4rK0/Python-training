# use keyword import random to choose a random choice from a list 
import random 

# You can call the same function multiple times with different arguments, avoiding repetitive code by using def keyword.
def get_choices():
  # player have to input the choice 
  player_choice = input ("enter a choice (rock, paper, scissors):") 
  # make the computer choose a random weapon from a list of options then, use the keyword random.choice(list) 
  options = ['rock' , 'paper' , 'scissors'] 
  computer_choice = random.choice(options)
  
  # dictionary are used to store data values in key value pairs
  choices = {'player': player_choice , 'computer': computer_choice}

  # return to choices after the player choosed 
  return choices

def check_win(player, computer):
  # use keyword (f'{}') to connect strings and variables on one line 
  print(f'you chose {player} , computer chose {computer}' )  
  if player == computer:
    return "it's a tie!" 
  elif player == 'rock':
    if computer == 'scissors': 
      return "rock smashes scissors! you win!" 
    else:
      return 'paper covers rock! you lose.' 
  elif player == 'paper': 
    if computer == 'rock': 
      return "paper covers rock! you win!" 
    else:
      return 'scissors cuts paper! you lose.'
  elif player == 'scissors': 
    if computer == 'paper': 
      return "scissors cuts paper! you win!" 
    else:
      return 'rock smashes scissors! you lose.' 

choices = get_choices()
  # the result is one of the returns
result = check_win (choices['player'], choices['computer']) 
print(result)                                        
