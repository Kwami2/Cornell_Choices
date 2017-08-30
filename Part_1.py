from game_over import game_over
from space_maker import space_maker
def Part_1():
  letters_for_choices=["a","b","c"]
  Choices=["Fight","Family Dissappointment","Existential Crisis"]
  Comment=["Great!, I knew you were a fighter!","Tell your parents' basement hello and your tuition goodbye","We all have those. I'm a potato"]
  #An allusion to the other project I worked on.
  print "Part 1:Your First Major Decision...\n"
  space_maker()
  dorm=raw_input("where do you live?\n")
  
  print"It's been a week so far at Cornell, with you quickly realzing that Cornell Engineering classes don't play. Especially Chem 2090. After a day of class you walk back to %s, lay on your bed, and then you finally realize something:\n" %(dorm)
  print ("If you want to survive, you have three choices: \n")
  
#This while loop keeps asking the user to select from a list of choices. The loop won't break until the user does. 
  bailout=1
  while bailout==1:
    for i in range(len(Choices)):
      print letters_for_choices[i]+". " + Choices[i]+"\n"
    print "\n"
    user_answer=raw_input("What do you choose?\n")
    user_answer=user_answer.lower()
    user_answer=user_answer.strip()
    for i in range(len(letters_for_choices)):
      if user_answer==letters_for_choices[i]:
        bailout=0
#This is simply a way to print "You chose: [insert choice here] and the respective comment.
  for i in range(3):
    if user_answer==letters_for_choices[i]:
      print "You chose: " + Choices[i]+ "\n" + Comment[i]
      
#For this chapter, there is only one answer.
 #That is because I believe that you shouldn't be giving up 
  if user_answer == "b" or user_answer == "c":
    print "\n"
    game_over()
    
#I want to return this string, so I could possible use it later, and won't have to ask them again. 
  return dorm 