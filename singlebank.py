#Data --> 
Account_Number = 98765
Pin = 1234
Initial_Amount = 10000
#Operations --> Deposite, Withdraw, Pin_change, Balance Check

Enter_Account_Number = int(input('Enter your Account_Number'))
Enter_Pin = int(input('Enter your Pin'))

print("""Press D for Deposite
Press W for Withdraw
Press P for Pin_change
Press B for Balance_Check""")
Operation = input('Please select the Operation')

#For Deposite Operation
if (Operation=='D'):
  if (Account_Number == Enter_Account_Number and Pin == Enter_Pin):
    
     Deposite_Amount = int(input('Enter Deposite Amount'))
     Initial_Amount = Initial_Amount + Deposite_Amount
     print('Deposite Successful')
     Balance_check = Initial_Amount
     print('Your available Balance is',Balance_check)
    
  else:
    print('Invalid Credentials')

#For Withdraw Operation
elif (Operation=='W'):
  if (Account_Number == Enter_Account_Number and Pin == Enter_Pin):

     Withdrawal_Amount = int(input('Enter Withdrawal Amount'))
     if (Withdrawal_Amount <= Initial_Amount):
         print('Withdrawal Successful')
         Initial_Amount = Initial_Amount - Withdrawal_Amount
         Balance_check = Initial_Amount
         print('Your available Balance is',Balance_check)
     elif (Withdrawal_Amount > Initial_Amount):
         print('Insufficient Balance')
   
  else:
    print('Invalid Credentials')

#For Pin change Operation
elif(Operation=='P'):
  if (Account_Number == Enter_Account_Number and Pin == Enter_Pin):

      Enter_New_Pin = int (input('Enter New Four digit Pin'))
    
      if (Enter_New_Pin == Pin):
        print('Please Enter New Pin')
      elif (Enter_New_Pin != Pin):
       print('Your Pin is changed')     
        
  else:
     print('Invalid Credentials')

#For Balance check
elif(Operation=='B'):
  if (Account_Number == Enter_Account_Number and Pin == Enter_Pin):

      Balance_check = Initial_Amount
      print('Available Bank Balance is:', Balance_check)    
        
  else:
      print('Invalid Credentials')
 

