import time, random

#randomize rooms
#separate upstairs and downstairs into lists if there are two treasures

rooms = ['basement', 'kitchen', 'garden', 'roof', 'balcony']
random_room = str(random.choice(rooms))
print(random_room)
done = False

def find_treasure(options):
  input2 = input('there are two paths ahead: ' + options).lower()
  if input2 == random_room:
    print('searching...')
    time.sleep(3)
    print('excellent! you found the treasure :D')
    done = True
    break
    
  else:
    print('searching...')
    time.sleep(3)
    print('no treasure here!')
    print('turning back now...')
    time.sleep(2)

  

while True: 
  print('You are in a mansion on the search for treasure. Where would you like to search?')
  input1 = input('Type in upstairs or downstairs: ').lower()
  
  if input1 == 'downstairs':
    find_treasure('to the basement, kitchen or the garden? ')
    
   

  elif input1 == 'upstairs':
    find_treasure('balcony or roof? ')


  else: 
    print('enter downstairs or upstairs')


    
    
