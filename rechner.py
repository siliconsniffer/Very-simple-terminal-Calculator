# Hinweis
print("Bitte die Zahlen und Rechenzeichen mit Leerzeichen trennen. Z.B. 3 * 4 oder 4.2 / 1.5")

# Variablen
global num1, y, num2

def rechnung():
    num1, y, num2 = input("Rechnung: ").split(' ')
    num1= float(num1)
    num2 = float(num2)

    # Funktionen definieren die Rechenart
    def summe(num1, num2):
	    sum = float(num1 + num2)
	    print(sum)
	    return

    def produkt(num1, num2):
	    produkt = float(num1 * num2)
	    print(produkt)
	    return

    def quotient(num1, num2):
	    quotient = num1 / num2
	    print(quotient)
	    return

    def differenz(num1, num2):
	    differenz = float(num1 - num2)
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

    global antwort
    antwort = input("Nochmal?(Ja/Nein) ")

    return

rechnung()

# While-Schleife
while (antwort == "Ja"):
	rechnung()
else:
    print("Vielen Dank für deine Rechnung, tschüss!")
