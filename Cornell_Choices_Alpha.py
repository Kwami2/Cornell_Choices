def Cornell_Choices_Alpha():
  #In terms of data flow, this program is a mess to read and understand. I was just testing how I would go along asking users to input choices.
  print "This Cornell-meme related program is brought to you by Atsu Kludze, member of Sleep is Not Due Tommorrow"
  letters_for_school=["a","b","c","d","e","f","g"]
  colleges = ["College of Agriculture and Life Sciences","College of Architecture, Art and Planning"
                  "College of Arts and Sciences","Cornell SC Johnson College of Business","College of Engineering",
                  "College of Human Ecology","School of Industrial and Labor Relations (ILR)"]
  for i in range(len(colleges)):
    print letters_for_school[i] +"."+colleges[i] + "\n"
  school= raw_input("What is your school?")
  school=school.lower()
  letters_for_choices=["a","b","c"]
  Choices=["Fight","Family Dissappointment","Existential Crisis"]
  Comment=["Great!, I knew you were a fighter!","Tell your parents' basement hello and your tuition goodbye","We all have those. I'm a potato"]
  name=raw_input("What is your name? \n")
  for i in range(len(colleges)):
    if school==letters_for_school[i]:
      College_name=colleges[letters_for_school.index(school)]
      print ("Welcome to Cornell %s! from %s") %(name,College_name)
      
  print ("At Cornell, we give you three choices: \n")
  for i in range(len(Choices)):
    print letter[i]+". " + Choices[i]+"\n"
  ans=raw_input("What do you choose? \n")
  ans=ans.lower()
  for i in range(3):
    if ans==letter[i]:
      print "You chose: " + Choices[i]+ "\n" + Comment[i]
Cornell_Choices_Alpha()