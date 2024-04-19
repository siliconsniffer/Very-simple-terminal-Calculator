# Hinweis
print("Bitte die Zahlen und Rechenzeiten mit Leerzeichen trenne. Z.B. 3 * 4")

# Code
global num1, y, num2
num1, y, num2 = input("Rechnung: ").split(' ')
num1= int(num1)
num2 = int(num2)

# Funktionen definieren die Rechenart
def summe(num1, num2):
	sum = num1 + num2
	print(sum)
	return

def produkt(num1, num2):
	produkt = int(num1 * num2)
	print(produkt)
	return
	
def quotient(num1, num2):
	quotient = num1 // num2
	print(quotient)
	return
	
def differenz(num1, num2):
	differenz = num1 - num2
	print(differenz)
	return
	
# Rechenarten
match y:
    case "+":
        summe(num1, num2)
    case "-":
        differenz(num1, num2)
    case "/":
        quotient(num1, num2)
    case "*":
        produkt(num1, num2)


# While-Schleife
antwort = input("Nochmal? (Ja/Nein)")
while (antwort == "Ja"):
	num1, y, num2 = input().split(' ')
	num1 = int(num1)
	num2 = int(num2)
	rechenart(y)
	antwort = input("Nochmal? ")


#def rechenart(y):
#	if  y == "+":
#		summe(num1, num2)
#	elif y == "*":
#		produkt(num1, num2)
#	elif y == "/":
#		quotient(num1, num2)
#	elif y == "-":
#		differenz(num1, num2)
#	return
