# Temperaturumrechner

faktor = 1.8
offset = 32

print("--------- Temperaturumrechner ---------")

while True:
    print("\nWie möchtest du umrechnen?")
    print("1 = Celsius in Fahrenheit")
    print("2 = Fahrenheit in Celsius")
    auswahl = input("Bitte 1, 2 oder B zum Beenden eingeben: ").lower()

    if auswahl == "1":
        celsius = float(input("Wie viel °C soll umgerechnet werden?: "))
        fahrenheit = celsius * faktor + offset
        print(f"{celsius} °C entsprechen {fahrenheit} °F")
    elif auswahl == "2":
        fahrenheit = float(input("Wie viel °F soll umgerechnet werden?: "))
        celsius = (fahrenheit - offset) / faktor
        print(f"{fahrenheit} °F entsprechen {celsius} °C")
    elif auswahl == "b":
        break
    else:
        print("Ungültige Auswahl. Bitte 1, 2 oder B eingeben.")

print("\n------ Programm beendet ------")
