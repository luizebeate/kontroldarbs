import json


def tkrekli():
    # Instrukcijas
    print("\nSveicināti LOLO-Tshirt kompānijā!")
    print("Pasūtījumu veikšanas nosacījumi: piegāde, neatkarīgi no pasūtījuma lieluma, maksā 7EUR, taču, ja pasūtījuma summa pārsniedz 100EUR, tad iegūstat 5 procentu atlaidi")
    print("Pirms veicat pasūtījuma meklēšanu pēc kādas pazīmes, lūdzu saglabājiet tos failā!")
    print("Pirms datu saglabāšanas failā, pievienojiet visus pasūtījumus!")
    print("Apdruka: ar tekstu - 5EUR, ar vienkrāsainu zīmi - 7EUR, ar fotogrāfiju - 20EUR")
    sakums()

def sakums():
    # Pasūtījuma sākšana
    pp = input("\nVai vēlaties veikt kādu darbību?(ievadiet + vai -):")
    if pp == "+":
        izvelne()
    elif pp == "-":
        beigt()
    else:
        print("Dati ievadīti nepareizi, lūdzu izvēlaties + vai -")
        sakums()


def izvelne():
    # Darbību izvēle
    print("\nKo vēlaties darīt?")
    print("Iespējas: 1-pievienot pasūtījumu, 2-meklēt pasūtījumu pēc kādas pazīmes, 3-apskatīt savus jaunos pasūtījumus, 4-saglabāt datus failā, 5-nolasīt vecos datus, 6-beigt darbu")
    izv = input("\nKo izvēlējies?: ")

    if izv == "1":
        pievienot()
    elif izv == "2":
        meklet()
    elif izv == "3":
        apskatit()
    elif izv == "4":
        g = input("Vai esat pievienojis visus pasūtījumus? (+ vai -):")
        if g == "+":
            vajadzigs = input("Vai šis ir jūsu pirmais pirkums? (+ vai -):")
            if vajadzigs == "+":
                pirmareize()
            elif vajadzigs == "-":
                datupieraksts()
        elif g == "-":
            print("Lūdzu pievienojiet visus pasūtījumus pirms to saglabāšanas!")
            pievienot()
    elif izv == "5":
        nolasit()
    elif izv == "6":
        beigt()

    
def pievienot():
    # Pasūtījumu pievienošana
    pasutijums = {}
    skaits = int(input("Lūdzu ievadiet apdrukājamo tkreklu skaitu:"))
    veids = input("Lūdzu ievadiet apdrukas veidu (teksts, zime vai foto): ")
    piegade = input("Vai vajadzīga piegāde? (ievadiet + vai -): ")

    i = 7
    if veids == "teksts" and piegade == "+":
        apdruka = input("Ievadiet, lūdzu, tekstu, ko vēlaties uzdrukāt: ")
        krasa = input("Ievadiet, lūdzu, krāsu kādā vēlaties uzdrukāto tekstu: ")
        cena = 5
        kopa = cena*skaits
        print(f"Pasūtījuma cena ir {kopa} ar {i} eiro piegādi")
        pasutijums["krasa"] = krasa
    elif veids == "teksts" and piegade == "-":
        apdruka = input("Ievadiet, lūdzu, tekstu, ko vēlaties uzdrukāt: ")
        krasa = input("Ievadiet, lūdzu, krāsu kādā vēlaties uzdrukāto tekstu: ")
        cena = 5
        kopa = cena*skaits
        print(f"Pasūtījuma cena ir {kopa}")
        pasutijums["krasa"] = krasa
    if veids == "zime" and piegade == "+":
        apdruka = input("Iekopējiet linku vai aprakstiet, lūdzu, zīmi, ko vēlaties uzdrukāt: ")
        krasa = input("Ievadiet, lūdzu, krāsu kādā vēlaties uzdrukāto zīmi: ")
        cena = 7
        kopa = cena*skaits
        print(f"Pasūtījuma cena ir {kopa} ar {i} eiro piegādi")
        pasutijums["krasa"] = krasa
    elif veids == "zime" and piegade == "-":
        apdruka = input("Iekopējiet linku vai aprakstiet, lūdzu, zīmi, ko vēlaties uzdrukāt: ")
        krasa = input("Ievadiet, lūdzu, krāsu kādā vēlaties uzdrukāto zīmi: ")
        cena = 7
        kopa = cena*skaits
        print(f"Pasūtījuma cena ir {kopa}")
        pasutijums["krasa"] = krasa
    if veids == "foto" and piegade == "+":
        apdruka = input("Lūdzu, iekopējiet linku uz foto, ko vēlaties uzdrukāt: ")
        cena = 20
        kopa = cena*skaits
        print(f"Pasūtījuma cena ir {kopa} ar {i} eiro piegādi")
    elif veids == "foto" and piegade == "-":
        apdruka = input("Lūdzu, iekopējiet linku uz foto, ko vēlaties uzdrukāt: ")
        cena = 20
        kopa = cena*skaits
        print(f"Pasūtījuma cena ir {kopa}")

        
    pasutijums["skaits"] = skaits
    pasutijums["piegade"] = piegade
    pasutijums["apdruka"] = apdruka
    pasutijums["cena"] = kopa + i

    firma.append(pasutijums)
    if kopa > 100:
        atlaide = 0.2
        summa = int(kopa-(kopa*atlaide))
        print("Tā kā jūsu kopējā pasūtījuma cena (neieskaitot piegādi) ir lielāka par 100 eiro, jūs esat saņēmis 5% atlaidi")
        print(f"Par pasūtījumu jāmaksā {summa} ar {i} eiro piegādi")
        pasutijums["cena"] = summa + i
    
    izvelne()

def meklet():
    # Pasūtījumu meklēšana pēc apdrukas vai piegādes
    svarigi = input("Ja esat pievienojis jaunus pasūtījumus, vai esat saglābājis tos failā? (+ vai -): ")
    if svarigi == "+":
        with open("tkrekli.json", "r", encoding="utf-8") as fails:
            i = fails.read()
        visidati = json.loads(i)
        pazime = input("Ievadiet, lūdzu, pazīmi, pēc kuras meklēt pasūtījumu (apdruka vai piegāde): ")
        atrada = False
        for viens in visidati:
            for z in viens:
                if pazime in z["apdruka"]:
                    print("Pasūtījums tika atrasts!")
                    atrada = True
                    for atslega in z:
                        print(f"{atslega}: {z[atslega]}")
                elif pazime in z["piegade"]:
                    print("Pasūtījums tika atrasts!")
                    atrada = True
                    for atslega in z:
                        print(f"{atslega}: {z[atslega]}")
            if not atrada:
                print("Pasūtījums nav atrasts!")
        izvelne()
    elif svarigi == "-":
        print("Lūdzu sākumā saglabājiet jūsu jaunos datus, citādi tie neuzrādīsies meklēšanā!")
        izvelne()
    
def apskatit():
    # Pasūtījumu apskatīšana
    for viens in firma:
        for atslega in viens:
            print(f"{atslega}: {viens[atslega]}")
        print()
    izvelne()

def datupieraksts():
    # Pasūtījumu ierakstīšana JSON failā (pēc pirmās reizes)
    with open("tkrekli.json") as feedsjson:
        feeds = json.load(feedsjson)
    feeds.append(firma)
    with open("tkrekli.json", "w") as f:
        f.write(json.dumps(feeds))

    print("Jūsu pasūtījums ir noformulēts un ierakstīts failā!")
    izvelne()

def pirmareize():
    # Pirmā pasūtījuma ierakstīšana JSON failā (tikai pirmā pasūtījuma)
    a = []
    a.append(firma)
    dati = json.dumps(a, ensure_ascii=False)
    with open("tkrekli.json", "w", encoding="utf-8") as file:
        file.write(dati)
    print("Jūsu pirmais pasūtījums ir noformulēts un ierakstīts failā!")
    izvelne()

def beigt():
    # Programmas apstāšanās
    print("Paldies par servisa izmantošanu, uzredzēšanos!")

def nolasit():
    # Veco datu nolasīšana
    with open("tkrekli.json", "r", encoding="utf-8") as fails:
        i = fails.read()
    visidati = json.loads(i)
    print("Jūsu iepriekš saglabātie dati ir nolasīti")
    vecie = input("Vai vēlaties apskatīt visus datus (+ vai -): ")
    if vecie == "+":
        for viens in visidati:
            for katrs in viens:
                for atslega in katrs:
                    print(f"{atslega}: {katrs[atslega]}")
                print()
        izvelne()
    elif vecie == "-":
        izvelne()
    

firma = []
tkrekli()


    
