import random
options = ("rock", "paper","scissors")
cpu = random.choice (options)
print("rock paper scissors")
player_win = 0
cpu_win = 0
draw = 0

while True:
   cpu = random.choice (options)
   player = input("""rock, paper, scissors
                  : """)
   if player == "rock" and cpu == "scissors" or player == "paper" and cpu == "rock" or cpu == "scissors" and cpu == ("paper"):
      player_win = player_win + 1
      print(cpu)
      print("You won!")
      print("player:", player_win, "cpu:", cpu_win, "draw:", draw)
   elif player == cpu:
      draw = draw + 1
      print(cpu)
      print("draw!")
      print("player:", player_win, "cpu:", cpu_win, "draw:", draw)
   else:
      cpu_win = cpu_win + 1
      print(cpu)
      print("You lost!")
      print("player:", player_win, "cpu:", cpu_win, "draw:", draw)