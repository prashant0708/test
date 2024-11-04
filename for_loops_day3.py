# Enter the user input and check nenter number is prime or not

user_input = int(input ("Enter the number to check "))# -> 6

flag=0  
for i in range(2,(user_input//2)+1): #  (2,3)  -> i=2, i=3
   if user_input%i==0:   #i=2 , user_input= 6
     flag=1
     break
   
if flag==0:
  print(f"{user_input} is prime number")
else:
  print(f"{user_input} is not prime number")
  
  

  