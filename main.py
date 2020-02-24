#Status : Completed !
#Palindrome Checker 
#Author : Siddhant Khare
#Input : Positive Integer !

from termcolor import cprint
import replit

replit.clear()
num = str(input('Enter any Positive Integer : '))

if int(num[::-1]) == int(num) :
  print("\nIt's a Palindrome Number !")
else :
  print("\nIt's not a Palindrome Number !")
  
cprint("\n\nMade by Siddhant Khare", 'cyan',attrs=['blink','bold'])  
