# Directions Reduction (5 kyu)
# https://www.codewars.com/kata/550f22f4d758534c1100025a/python

def dirReduc(arr):
  opposites = {
    'NORTH': 'SOUTH',
    'SOUTH':  'NORTH',
    'EAST': 'WEST',
    'WEST': 'EAST',
  }

  directions = []
  for direction in arr:
    directions.append(direction)
    if len(directions) > 1 and opposites[directions[-1]] == directions[-2]:
      directions.pop()
      directions.pop()

  return directions
  

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))