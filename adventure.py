import time, random

#randomize rooms
rooms = ['basement', 'kitchen', 'garden', 'roof', 'balcony']
random_room = str(random.choice(rooms))
print(random_room)

while True: 
  print('You are in a mansion on the search for treasure. Where would you like to search?')
  input1 = input('Type in upstairs or downstairs: ').lower()
  
  if input1 == 'downstairs':
    input2 = input('there are two paths ahead: to the basement, to the kitchen or to the garden? ').lower()
    if input2 == 'basement':
      print('searching...')
      time.sleep(3)
      input3 = input('wrong way!')
    elif input2 == 'kitchen':
      print('searching...')
      time.sleep(3)
      print('excellent! you found the treasure :D')
      break
    elif input2 == 'garden':
      print('searching...')
      time.sleep(3)
      print('no treasure here!')
    else:
      print('enter one of the choices above')
  elif input1 == 'upstairs':
    input4 = input('Two more paths lay ahead: balcony or roof? ').lower()
    if input4 == 'roof':
      print('searching...')
      time.sleep(3)
      print('you found the treasure :D')
      break
    elif input4 == 'balcony':
      print('searching...')
      time.sleep(3)
      print('you missed the treasure..')
    else: 
      print('enter one of the choices above')
  else:
    print('enter downstairs or upstairs')
      