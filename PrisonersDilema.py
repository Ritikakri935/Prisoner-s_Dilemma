import random
def round_one():
    answer=(input("You and a buddy got caught commiting a crime. Do you keep quiet, or rat on your best friend? \n Enter Collude to confess or Betray to deny "))
    a = ["Collude", "Betray"]
    G = random.choice(a)
    print("You chose " + answer + ", and your partner chose " + G + ". ")
    if G == "Collude" and answer=="Collude":
        print("Both jailed for 3 years")
    if G == 'Collude' and answer=='Betray':
        print("You got free and your friend got jailed for 7 years")
    if G == 'Betray' and answer=='Betray':
        print("Both jailed for 1 year")
    if G == 'Betray' and answer=='Collude':
        print("You got jailed for 7 years and friend got free")
round_one()