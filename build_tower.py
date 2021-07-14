# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
  return ['{}'.format('*' * ((n_floors * 2) - 1)) if i == 0 else '{}{}{}'.format(' ' * i, ('{}'.format('*' * ((n_floors * 2) - 1)))[i:(-i)], ' ' * i) for i in range(0, n_floors)][::-1]