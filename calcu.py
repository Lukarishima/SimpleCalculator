#code By Bandhitawkunthi
import os
import sys
os.system("clear")


print("\033[93m")
while True:
		print("===================")
		print("===================")
		print("  ")
		print("ＳＩＭＰＬＥ ＣＡＬＣＵＬＡＴＯＲ")
		print("Code by Bandhitawkunthi")
		print("  ")
		print("===================")
		print("===================")
		print("Enter the operation you want, for example +,-,*,/,")
		
		operasi = input("{?} Enter Your Operation : ")
		if operasi not in("+","-","*","/"):
			print("Closed connetions.....")
			break
		
		
		a = int(input("First number : "))
		b = int(input("Second number : "))
		
		if operasi == "+":
		    print("Result of",a ,"+",b ,"=",a+b)
		elif operasi == "-":
		   	print("Result of",a ,"-",b ,"=",a-b)
		elif operasi == "*":
			   print("Result of",a ,"*",b ,"=",a*b)
		elif operasi == "/":
		   	print("Result of",a , "/",b ,"=",a/b)
		
