# 6

human = {}

hobbies = ["teach"]

children = [
    {
        "firstname": "Luka",
        "comment": "unknown hacker"

    },

    {
        "firstname": "Aleqsandre",
        "comment": "30 wliani kaci"

    },

    {
        "firstname": "Aleqsandre",
        "comment": "daibada 1995 wels ._.' "

    },

    {
        "firstname": "Anastasia",
        "comment": "are you lost? XD"

    },

    {
        "firstname": "Gio",
        "comment": "loud genius"

    },

    {
        "firstname": "Ilia",
        "comment": "me megona aleqsandrea ._.' "

    },

    {
        "firstname": "Luka",
        "comment": "shotos avatarit"

    },

    {
        "firstname": "Natalia",
        "comment": "mezobeli bomji loti"

    },

    {
        "firstname": "Saba",
        "comment": "patara"

    },

    {
        "firstname": "Sophio",
        "comment": "even the pycharm will confuse"

    },

    {
        "firstname": "Tamari",
        "comment": "so busy lady"

    }
]

human.update({'name': "Mariam",
              "lastname": "Siradze",
              "hobbies": "teach",
              "children": children
              })

print(human)



# 8

set1 = {0, 1, 2, 3, 4}

set1.update([23, 35, 42])

set1.discard(0)
set1.discard(4)

for i in set1:
    print(i)



# 9.1

set2 = {"green", "blue"}
set3 = {"blue", "yellow"}

set4 = set2.union(set3)
print(set4)
print(len(set4))

set4 = set2.intersection(set3)
print(set4)
print(len(set4))

set4 = set2.difference(set3)
print(set4)
print(len(set4))
set4 = set3.difference(set2)
print(set4)
print(len(set4))

set4 = set2.symmetric_difference(set3)
print(set4)
print(len(set4))

# OH MY GOOOOOOOOOD!!! SETEBI TURME LISTISAVIT AR ICVLEBIAN DA ARAA AUCILEBELI YOVELTVIS AXALI SETIS DAMATEBA!!!
# щ⁠(⁠゜⁠ロ⁠゜⁠щ⁠)
# tore set100 meqneboda hehe



# 9.2

set4 = set2 | set3
print(set4)
print(len(set4))

set4 = set2 & set3
print(set4)
print(len(set4))

set4 = set2 - set3
print(set4)
print(len(set4))

set4 = set2 ^ set3
print(set4)
print(len(set4))



# 10

set5 = {35, 328795, 678934, 7, 37828, 326748698,
        0.99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
        4879828937802372375297857928273958728327920297258728628560828}

# au aqedan romeli yvelaze didi da patara ricxvi????
# ai imena ver vigeb raaa
# jobia kods davwer XD

set6 = max(set5)
print(set6)
set6 = min(set5)
print(set6)

# eeeeee!!! ratom daamrgvala?? mewyina T.T



# 11

tap = input("Write something : ")

set7 = set(tap)

print(set7)



#12

tap1 = input("You know what to do : ")
tap2 = input("Again : ")

taptap1 = list(tap1)
taptap2 = list(tap2)

setset1 = set(taptap1)
setset2 = set(taptap2)

tapset = setset1|setset2

print(tapset)