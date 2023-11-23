from math import sqrt

print("Tere! Olen sinu uus sõber - Python!")
nimi= input("nimi: ")
print(f"{nimi}")

print(f"{nimi}, oi kui ilus nimi!")
answer = str(input(f"{nimi}! Kas leian Sinu keha indeksi? jah või ei?: "))
try:
    if answer.lower() == "jah":
        pikkus=int(input("pikkus(meter): "))
        mass=int(input("mass(kg): "))
        indeks= mass/sqrt(0.01*pikkus)**2
        if indeks >= 40:
            index="Tervisele ohtlik rasvumine"
        elif 35 <= indeks <= 40:
            index="Tugev rasvumine"
        elif 30 <= indeks <= 35:
            index="Rasvumine"
        elif 25 <= indeks <= 30:
            index="Ülekaal"
        elif 19 <= indeks <= 25:
          index="Normaalkaal"
        elif 16 <= indeks <= 19:
            index="Alakaal"
        elif 0 <= indeks <= 16:
            index="Tervisele ohtlik rasvumine"
        else:
            index="Kahju! See on väga kasulik info!"

        print(f"{nimi}! Sinu keha indeks on:{round(indeks,1)} BMI - {index}")
        
    else:
        print("Kahju! See on väga kasulik info!\n")
except:
    pass

print(f"Kohtumiseni,{nimi}!Igavesti Sinu, Python!")
