def Cornell_Choices():
  print "This Cornell-meme related program is brought to you by Atsu Kludze, member of Sleep is Not Due Tommorrow"
  #Add college names later. 
  letters_for_school=["a","b","c"
  letters_for_choices=["a","b","c"]
  Choices=["Fight","Family Dissappointment","Existential Crisis"]
  Comment=["Great!, I knew you were a fighter!","Tell your parents' basement hello and your tuition goodbye","We all have those. I'm a potato"]
  name=raw_input("What is your name? \n")
  school= raw_input("What is your school")
  print ("Welcome to Cornell %s! \n") %name
  print ("At Cornell, we give you three choices: \n")
  for i in range(len(Choices)):
    print letter[i]+". " + Choices[i]+"\n"
  ans=raw_input("What do you choose? \n")
  ans=ans.lower()
  for i in range(3):
    if ans==letter[i]:
      print "You chose: " + Choices[i]+ "\n" + Comment[i]
Cornell_Choices()