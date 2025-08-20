#1
kuhan_pituus = float(input("Syötä kuhan pituus senttimetreinä: "))
sallittu_pituus = 37

if kuhan_pituus < sallittu_pituus:
    alijaama = sallittu_pituus - kuhan_pituus
    print("Kuha on " + str(alijaama) + "cm alamittainen, heitä se takaisin veteen")
else:
    print("Kuha on täysikasvuinen!")

#2
hyttivalinta = input("Syötä valitsemasi hyttiluokka (LUX, A, B tai C): ")

if hyttivalinta == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttivalinta == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttivalinta == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttivalinta == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

#3
sukupuoli = input("Syötä biologinen sukupuolesi (M tai N): ")
hemoglobiiniarvo = float(input("Syötä hemoglobiiniarvosi (muodossa g/l): "))

if sukupuoli == "M":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi ovat matalat")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvosi ovat korkeat")
    else:
        print("Hemoglobiiniarvosi ovat normaalit")


elif sukupuoli == "N":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi ovat matalat")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvosi ovat korkeat")
    else:
        print("Hemoglobiiniarvosi ovat normaalit")

else:
    print("Virheellinen vastaus")

#4
vuosi = int(input("Syötä vuosiluku: "))
jakojaannos = vuosi % 4

if jakojaannos == 0 and vuosi % 100 != 0:
    print("Vuosiluku on karkausvuosi")
elif jakojaannos == 0 and vuosi % 100 == 0 and vuosi % 400 == 0:
    print("Vuosiluku on karkausvuosi")
else:
    print("Vuosiluku ei ole karkausvuosi")