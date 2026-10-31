print("--------- Teperatur Umrechner ---------")

konst = {
    "1.8": 1.8,
    "32": 32
}

while True:
    print("\n--- wie möchtest du Umrechen? ----")
    print("\n  1 = °C in °F / 2. = °F in °C")
    x = input("\nBitte eingeben 1 oder 2 / Beenden = B : ")

    if x in ["1"]:
        z = float(input("Wie viel °C soll umgerechnet werden?: "))
        print(f'--- {z * konst["1.8"] + konst["32"]} °F --- sind aus {z}°C' )

    elif x in ["2"]:
        e = float(input("Wie viel °F soll umgerechnet werden?:  "))
        print(f'--- {(e - konst["32"]) / konst["1.8"]} °C --- sind aus {e}°F')

    elif x in ["b", "B"]:
        break

    else:
        print("\n ! --- ! Fehler ! --- !")

print("\n------ Beendet ------")
