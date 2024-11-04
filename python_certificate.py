user_input=input("have you completed the course ?")  #YES AND NO 
user_input=user_input.lower() # yes or no

if user_input=='yes':  #True
  user_input2 =input("have you completed all the classes of python ")## yes or no
  #user_input2=user_input2.lower()
  if user_input2 == "yes":
    user_input3=input("have you completed all the assignment ") ## yes or no
    user_input3=user_input3.lower()
    if user_input3=='yes':
      print("Congratulation ! you are eligiable for the certificate")
    else:
      print("Please complete all the assignment")
  else:
    print("Please complete all the classes of python")

else:
  print("Complete the course")

