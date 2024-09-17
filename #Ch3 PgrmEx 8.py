#Ch3 PgrmEx 8
import math
HDPack = 10
HDBuns = 8

People = int(input("How many people are attending the cookout?: "))
#Number of hot dogs per person
HDPP = int(input("How many hot dogs does each person get?: "))

HotDogs = People * HDPP



NumHDPack = math.ceil(HotDogs / HDPack)
NumHDBuns = math.ceil(HotDogs / HDBuns)
RemHD = HDPack - (HotDogs % HDPack)
RemBuns = HDBuns - (HotDogs % HDBuns)


print("You will need", NumHDPack, "hot dog packs")
print("You will need", NumHDBuns, "hot dog bun packs")
print("You will have", RemHD, "hot dogs left")
print("You will have", RemBuns, "hot dog buns left")