#Code
num1, y, num2 = input().split(' ')
num1= int(num1)
num2 = int(num2)

#Funktionen
def summe(num1, num2):
	sum = num1 + num2
	print(sum)
	return

def produkt(num1, num2):
	produkt = int(num1 * num2)
	print(produkt)
	return
	
def quotient(num1, num2):
	quotient = num1 / num2
	print(quotient)
	return
	
def differenz(num1, num2):
	differenz = num1 - num2
	print(differenz)
	return
	
def rechenart(y):
	 if  y == "+":
	 	summe(num1, num2)
        elif y == "*":
        produkt(num1, num2)
        elif y == "/":
        quotient(num1, num2)
        elif y == "-":
        differenz(num1, num2)

#Code
	if  y == "+":
		summe(num1, num2)
	elif y == "*":
		produkt(num1, num2)
	elif y == "/":
		quotient(num1, num2)
	elif y == "-":
		differenz(num1, num2)

#Another one?
antwort = input("Nochmal? ")
while (antwort == "Ja"):
	num1, y, num2 = input().split(' ')
	rechenart(y)
	antwort = input("Nochmal? ")