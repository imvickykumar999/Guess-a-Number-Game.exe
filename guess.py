
import random, math

total = 0
sug = []

who_play = int(input('\nWho will play ? (Computer - 1, Human - 0) : '))
if not who_play:
  if_sug = int(input('Do you need suggestion ? (Yes - 1, No - 0) : '))
else:
  if_sug = 0
limit = int(input('Need limit ? (Yes - 1, No - 0) : '))

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

if limit:
  a = int(input('\nEnter lower limit (e.g., 1) : '))
  b = int(input('Enter upper limit : (e.g., 100) '))
else:
  a,b=1,100

choice = random.randint(a,b)

c = math.ceil(math.log(b-a+1))
print('\nChance given : ', c)
binary_search(range(a,b+1), choice)

for i in range(c):
  print()

  if if_sug:
    print('Suggestion (beta) : ', sug[i])

  if who_play:
    ask = sug[i]
  else:
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

if total:
  print(f'Missed by difference of {total} numbers.')
else:
  if not who_play:
    print('Congratulations Human ...')
  else:
    print('Congratulations Computer ...')

input('\n\t ... Press `Enter` to Exit.')