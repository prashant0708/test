atm_pin=5693
Account_Balance= 10000

user_input=int(input("Please enter the ATM pin= "))

if user_input==atm_pin:
  user_input1=input("""Press 1 for Balance Withdraw , 
                      Press 2 for Balance check,
                    Press 3 for Deposit,
                    press 4 for main manu""")
  if user_input1=="1":
    withdraw_amount=int(input("Enter the Amount "))
    if isinstance(withdraw_amount,int):
      print(f"{withdraw_amount} Collect the cash ")
    else:
      print("Invalid entered amount")
  if user_input1=="2":
    print(f"you account balance is {Account_Balance}")
  if user_input1=="3":
    user_input1= input("Please enter the amount you want to deposit")
    print("Amout is deposited")
  if user_input1=="4":
    user_input1=input("""Press 1 for Balance Withdraw , 
                    Press 2 for Balance check,
                    Press 3 for Deposit,
                    press 4 for main manu""")
else:
  print("Invalid Pin")