print("-----1------\n")

nimi = str(input("Nimi: "))
if nimi == "Juku":
    aastad = int(input("aastad: "))
    if aastad <= 0 or aastad >= 100:
        AastadAnswer = "viga andmetega"
    else:
        if aastad < 6:
            AastadAnswer = "tasuta"
        elif aastad < 6:
            AastadAnswer = "lastepilet"
        elif 15 <= aastad <= 65:
            AastadAnswer = "täispilet"
        elif 65 <= aastad <= 99:
            AastadAnswer = "sooduspilet"

print("\n-----2------\n")

Nimi0 = str(input("nimi1: "))
Nimi1 = str(input("nimi2: "))

print(f"{Nimi0} ja {Nimi1} tana pinginaabrid.")

print("\n-----3------\n")

ToaA = float(input("ristkülikukujulise toa[a]: "))
ToaB = float(input("ristkülikukujulise toa[b]: "))

print("põranda pindala", ToaA*ToaB) # meter

Question0 = str(input("remondi tegemise soov + or -?: "))
if Question0 == "+":
    Question1=float(input("kui palju maksab ruutmeeter: "))
    print( (ToaA*ToaB)*Question1,"€")
    
print("\n-----4------\n")

hind = int(input("hind: "))
if hind >= 700:
    hind = hind-(hind*0.30)
print("hind")

print("\n-----5------\n")

QuestionTemp0 = int(input("temperatuur?: "))
QuestionTemp1 = str(input("Talv,Sügis,Suvi,Kevad?: "))

if QuestionTemp0 < 18:
    print("<18")
elif 20 < QuestionTemp0 < 22 and QuestionTemp1.lower() == "talv":
    print("nice time")
else:
    print(">=18")

print("\n-----6------\n")

QuestionPikkus = float(input("Pikkus?[m]: "))
if QuestionPikkus <= 1:
    print("lühike")
elif 1 <= QuestionPikkus <= 2:
    print("keskmine")
elif QuestionPikkus > 2 :
    print("pikk ")

print("\n-----7------\n")

QuestionPikkus = float(input("Pikkus?: "))
QuestionSugu  = str(input("Sugu?[m/f]: "))

if (QuestionPikkus <= 0.8 and QuestionSugu.lower() == "f") or (QuestionPikkus <= 1 and QuestionSugu.lower() == "m"):
    print("lühike")
elif (QuestionPikkus <= 1.6 and QuestionSugu.lower() == "f") or (QuestionPikkus <= 2 and QuestionSugu.lower() == "m"):
    print("keskmine")
else:
    print("pikk ")

print("\n-----8------\n")

HindPoes = 0

QuestionPoes0 = str(input("kokku piima 3.67€? jah/ei?: "))
if QuestionPoes0 == "jah":
    HindPoes=HindPoes+3.67
QuestionPoes0 = str(input("kokku leiba 3.69€ jah/ei?: "))
if QuestionPoes0 == "jah":
    HindPoes=HindPoes+3.69

print("ostetud kraam maksma: {HindPoes}€")

print("\n-----9------\n")

QuestionRuut = int(input("ruudu küljed: "))
if QuestionRuut == 4:
    print("ROOT")
else:
    print("no root")

print("\n-----10------\n")

QuestionMateA = int(input("A: "))
QuestionMateT = str(input("mode: "))
QuestionMateB = int(input("B: "))

if QuestionMateT == "+":
    print(QuestionMateA+QuestionMateB)
elif QuestionMateT == "-":
    print(QuestionMateA-QuestionMateB)
elif QuestionMateT == "*":
    print(QuestionMateA*QuestionMateB)
elif QuestionMateT == "/":
    print(QuestionMateA/QuestionMateB)
    
print("\n-----11------\n")
import datetime

QSP0 = str(input("sünnipäeva päev: "))
QSP1 = str(input("sünnipäeva kuud: "))

x = datetime.datetime.now()

if (QSP0 == x.day) and (QSP1 == x.month):
    print("juubeliga.")
else:
    print("good day")

print("\n-----12------\n")

print("\n-----13------\n")

Qgenger = str(input("m-1/n-0: "))
if Qgenger == "n" or Qgenger == '0':
    Qage = int(input("vanus: "))

if ((Qgenger == "m" or Qgenger == "1") and ( 16 => Qage =< 18 ) ) or ( Qgenger == "n" or Qgenger == "0" ):
    print("allowed")
else:
    print("no")

print("\n-----14------\n")
