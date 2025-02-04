n = int(input())
game = input()
num_A = game.count("A")
num_D = game.count("D")
if num_A > num_D:
  print("Anton")
elif num_A < num_D:
  print("Danik")
else:
  print("Friendship")