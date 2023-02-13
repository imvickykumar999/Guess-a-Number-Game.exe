
import random, math, os
os.system('cls')

total = 0
sug = []
def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:
    mid = (high + low) // 2
    sug.append(arr[mid])

    if arr[mid] < x:
      low = mid + 1

    elif arr[mid] > x:
      high = mid - 1

    else:
      return mid
      
  return -1

# a = int(input('Enter lower limit : '))
# b = int(input('Enter upper limit : '))

a,b=1,100
choice = random.randint(a,b)

c = math.ceil(math.log(b-a+1))
print('\nChance given : ', c)
binary_search(range(a,b+1), choice)

for i in range(c):
  print()
#   print('Suggestion (beta) : ', sug[i])

#   ask = sug[i]
  ask = int(input(f'{i+1}). Enter a number : '))

  if ask > choice:
    print('too high')

  elif ask < choice:
    print('too low')

  else:
    print('... correct ...')
    break

print('-'*25, end=' Summary\n')
print('\nTaken chances : ', i+1)
print('Correct Answer : ', choice)

print('\nLast guess : ', ask)
total += abs(ask-choice)
print(f'Missed by difference of {total} numbers.')

# =====================================================

'''
C:\\Users\\Vicky\\Desktop\\Repository\\Guess-a-Number-Game.exe>python guess.py

Chance given :  5

Suggestion (beta) :  50
too high

Suggestion (beta) :  25
too high

Suggestion (beta) :  12
too high

Suggestion (beta) :  6
too high

Suggestion (beta) :  3
too low
------------------------- Summary

Taken chances :  5
Correct Answer :  4

Last guess :  3
Missed by difference of 1 numbers.

'''