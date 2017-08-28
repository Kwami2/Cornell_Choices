def Part_1():
  letters_for_choices=["a","b","c"]
  Choices=["Fight","Family Dissappointment","Existential Crisis"]
  Comment=["Great!, I knew you were a fighter!","Tell your parents' basement hello and your tuition goodbye","We all have those. I'm a potato"]
  print ("At Cornell, we give you three choices: \n")
  
  while bailout==1:
    for i in range(len(Choices)):
      print letter[i]+". " + Choices[i]+"\n"
      
    ans=raw_input("What do you choose? \n")
    ans=ans.lower()
    for i in range(3):
      if ans==letter[i]:
        print "You chose: " + Choices[i]+ "\n" + Comment[i]
        bailout=0
    print "Please select from one of the choices."
Part_1()