def introduction():
  
  print('hello! I\'m nayeli the chatbot...')
  name = input('What\'s your name? ')
  print('Let\'s see if I can spell that: ')
  nameList= []
  
  # print(name.split())
  for i in name:
    print(i)
    nameList.append(i)
  print(nameList)
  
  print('Nice to meet you ' + name)


def questions():
  print('Tell me about yourself')
  
  print('Where are you from? ')
  place = input('You are from... ')
  print('I\'d love to visit ' + place + ' one day!')
  
  print('What are you interested about? ')
  interest = input('You are interested about... ')
  print('That\'s awesome! ' + interest + ' is so cool!')
  
  print('What are your goals? ')
  goals = input('Your goals are to... ')
  print('I really admire your goal to ' + goals + '. I know you can do it!')

introduction()
questions()

while True:
  botInput1 = input('what would you like to know about me? -  home, interest, goal, or none? ').lower()
  
  if botInput1 == 'home':
    print('\nI live this computer right here')
  elif botInput1 == 'interest':
    print('\nI help people by keeping them company.')
  elif botInput1 == 'goal':
    print('\nI want to become a robot')
  elif botInput1 == 'none':
    print('\ntalk to you another time then!')
    break
  else: 
    print('\nenter one of the choices from above')
    