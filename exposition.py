def Exposition():
  #This print statement is meant to just give some instruction and background to the game.
  print "This Cornell-meme related program is brought to you by Atsu Kludze, member of Sleep is Not Due Tommorrow \n"
  print "Welcome to Cornell Choices, this game is a choose your own adventue, based on the freshman college experience. \n each chapter has a correcct choices, where not picking it will resut in game over. Have fun!"
  #Lists that carry the letter and respective college name for what school you are apart of.
  letters_for_school=["a","b","c","d","e","f","g"]
  colleges = ["College of Agriculture and Life Sciences","College of Architecture, Art and Planning"
                  "College of Arts and Sciences","Cornell SC Johnson College of Business","College of Engineering",
                  "College of Human Ecology","School of Industrial and Labor Relations"]
  
  name=raw_input("What is your name? \n")
  bailout=1
  #This while statement will keep asking you the same question about your school unless you input a valid letter.
  while bailout==1:
    for i in range(len(colleges)):
      print letters_for_school[i] +"."+colleges[i] + "\n"
    school= raw_input("What is your school? Please select from one of the choices.\n")
    school=school.lower()
    
    for i in range(len(colleges)):
      if school==letters_for_school[i]:
        college_name=colleges[letters_for_school.index(school)]
        print ("Welcome to Cornell %s! from %s") %(name,college_name)
        bailout=0
        return name
Exposition()