from game_over import game_over
from space_maker import space_maker
def Part_2():
  letters_for_choices=["a","b","c","d"]
  Choices=["Screw it, I'll figure it out later","Re-read the textbook", "Cry","Ask for help", ]
  Comment=["This isn't high school. BS doesn't work here","Self-Teaching? At least you show that you have determination","Do you need some Kleenex and a ticket back home?","That's probably the smartest thing you did so far."]
  print"Part 2: I Don't Understand..."
  space_maker()

  print "After your decision to not give up, you encounter something every engineer has to deal with during the freshman year: Not knowing how to do something \n"
  print "In Chem, you understand the basics, but do not fully understand the application of a certain concept.\nYou know that you have to learn it soon, as the Professor said that it will defintely be on the prelim.\n"
  print ("You have three choices: \n")
#This while loop keeps asking the user to select from a list of choices. The loop won't break until the user does.
  bailout=1
  while bailout==1:
    for i in range(len(Choices)):
      print letters_for_choices[i]+". " + Choices[i]+"\n"
    user_answer=raw_input("What do you choose? \n")
    user_answer=user_answer.lower()
    user_answer=user_answer.strip()
    for i in range(len(letters_for_choices)):
      if user_answer==letters_for_choices[i]:
        bailout=0
#The cue_game_over variable is use to activate the game_over function. It only gets changed if the user selects the two answers that I want to nd in a game over.
  cue_game_over=0
#This is simply a way to print "You chose: [insert choice here] and the respective comment.
  for i in range(len(Choices)):
    if user_answer==letters_for_choices[i]:
      print "You chose: " + Choices[i]+ "\n" + Comment[i]
#Just another way to write that every other choice resilts in a gameover. I can now copy this for later code. #Work Smarter, not harder.
    for i in range(0,len(Choices),2):
       if user_answer==letters_for_choices[i]:
         cue_game_over=1
  if cue_game_over==1:
    game_over()
  