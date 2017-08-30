from space_maker import space_maker 
def exposition():
  #This print statement is meant to just give some instruction and background to the game.
  print "This Cornell-meme related program is brought to you by Atsu Kludze, member of Sleep is Not Due Tommorrow \n"
  print "Welcome to Cornell Choices, this game is a choose your own adventure, based on my college freshman college experience as an engineering student. \nEach chapter has a correct choice, where not picking it will result in game over.\n"
  print "Exposition:\nYou are a part of the Cornell's Class of 2021, the most select and diverse class Cornell has ever had (until next year).\nYou don't know who at the engineering admission office messed up, but you are graeftul they did."
  print "Despite that fact, you are trying to prove to yourself that you belong here. The choices you make here will determine the next 4 years.\nGood Luck.\n"
  #Lists that carry the letter and respective college name for what school you are apart of.
  letters_for_school=["a","b","c","d","e","f","g"]
  colleges = ["College of Agriculture and Life Sciences","College of Architecture, Art and Planning",
                  "College of Arts and Sciences","Cornell SC Johnson College of Business","College of Engineering",
                  "College of Human Ecology","School of Industrial and Labor Relations"]
  
  name=raw_input("What is your name? \n")
  space_maker()
  bailout=1
  #This while statement will keep asking you the same question about your school unless you input a valid letter.
  while bailout==1:
    for i in range(len(colleges)):
      print letters_for_school[i] +"."+colleges[i] + "\n"
    school= raw_input("What is your school? Please select from one of the choices.\n")
    school=school.lower()
    school=school.strip()
    for i in range(len(colleges)):
      if school==letters_for_school[i]:
        bailout=0
#The user should answer that he is from the college of engineering. If he/she does not, then it should print a trying to be funny alternate statement.
    if school==letters_for_school[4]:
      college_name=colleges[4]
      print ("Welcome to Cornell %s from %s!\nGet ready for 4 years of choices. Cornell Choices.") %(name,college_name)
    else:
      print "Oh God, you don't even know what college you are a part of...\nThis is going to be the start of a very long 4 years..."
  return name 