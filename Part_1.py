from game_over import game_over
from space_maker import space_maker
def Part_1():
  letters_for_choices=["a","b","c"]
  Choices=["Fight","Family Dissappointment","Existential Crisis"]
  Comment=["Great!, I knew you were a fighter!","Tell your parents' basement hello and your tuition goodbye","We all have those. I'm a potato"]
  #An allusion to the other project I worked on.
  print "Part 1:Your First Major Decision...\n"
  space_maker()
  dorm=raw_input("where do you live?")
  
  print"It's been a week so far at Cornell, with you quickly realzing that Cornell Engineering classes don't play. Especially Chem 2090. After a day of class you walk back to %s, lay on your bed, and then you finally realize something:\n"
  print ("If you want to surive, you three choices: \n")

  bailout=1
  while bailout==1:
    for i in range(len(Choices)):
      print letters_for_choices[i]+". " + Choices[i]+"\n"
    user_answer=raw_input("What do you choose? \n")
    user_answer=user_answer.lower()
    for i in range(len(letters_for_choices)):
      if user_answer==letters_for_choices[i]:
        bailout=0
      
  for i in range(3):
    if user_answer==letters_for_choices[i]:
      print "You chose: " + Choices[i]+ "\n" + Comment[i]

  if user_answer == "b" or user_answer == "c":
    game_over()
  return dorm 