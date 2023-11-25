# 1

name = input("Please, write your name: ")
print("hello " + name + "!")

second_name = input("Good, now write your second name: ")
print("hello " + name + " " + second_name + "!")

adress = input("We will finish soon! Just write adress where you live: ")
print("And last small request!")

number_and_code = input("Write number and code of your card: ")
print(
    "Thank so much!!! You are so sweet!!! And if you will notice money is disappears from your balance - don't worry! :D ")

# 2

print("WARNING!!! I AM NOOB!!! Write only \"no\" for more fun!")
x = input("You want to know if the number is martivi or shedgenili?")

y = input("Excellent! Pay just 99999999999999.9999999999999$ and get the answer to your question!")

z = input("So... Or get a free mode... leaving us starving... And living in a cardboard box on the side of the road...")

c = input("Please!!!! I have a credit and about 20 kids!!!")

if c == "no":
    print("Dude you are too cruel -_- ")
elif c == "okay":
    print("FINALLY!!!")
else:
    print("Please write \"no\" or \"okay\"")

v = int(input("Write there your number: "))
k = 0
for i in range(2, v // 2 + 1):
    if (v % i == 0):
        k = k + 1
if (k <= 0):
    print("Number is martivi")
else:
    print("Number is not martivi anu shedgenili")

print("Mye inglishe it is perfecto i sink U-U ")

# 3 დაწერეთ rock, paper, scissors

print("rock, paper, scissors")
# vsio? ra ioli iyo turme
# it is just a joke hehe


import random

possible_action = ["rock", "paper", "scissors"]

user_action = input("write there: ")

computer_action = random.choice(possible_action)

print(f"you choose: {user_action}")
print(f"computer choose: {computer_action}")
print("result: ")

if user_action == computer_action:
    print("Maybe computer know what you thinking about?..")
elif user_action == "rock":
    if computer_action == "paper":
        print("Fine, you lost to the computer ._.")
    else:
        print("Fine, you win to the computer ._.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Another victory!!!")
    else:
        print("Don't cry, baby!")
elif user_action == "scissors":
    if computer_action == "rock":
        print("Sorry, but life is so violent to you  LOL")
    else:
        print("Good, so when you go work and stop laze?")

# I didn't mean to offend anyone, these are jokes and don't take them seriously!
# imedi maqvs araa problema, rom viyenebdi W3shoolis tutorials da googls
# kalkulatoris azrze ar var magram shevecdebi da sxva failit gamogigzavnit
# good luck :3


# BONUS

first = int(input("Write first number: "))
second = int(input("Write second number: "))
action = input("Write what you want to do with this nimbers: ")
if action == "+":
    print(first + second)
elif action == "-":
    print(first - second)
elif action == "*":
    print(first * second)
elif action == "/":
    print(first / second)
elif action == "**":
    print(first ** second)
elif action == "%":
    print(first / second) * 100
else:
    print("Use only \"+\" , \"-\", \"*\" , \"/\" , \"**\" or \"%\" ")

# anu... yvelaferi sworia, magram dzalian ioli :((
# 10-15 wutshi rac momafiqrda is davwere, magram ar mawyobs es resultati
# ra tqma unda sheidzleba uamravi cvladis damateba, magram mainc es is ar aris hm... >:^
# axlaxans davgoogle da amomigdo chem nairi kodi
# mashin davaleba gaketebulia? miuxedavad amisa, me mainc ragac ar var   T.T
# tqven gainteresebt ratom? iyidet da waikitxet axali wigni chem biografiaze da gaiget pasuxi!!!
# P.S. sinamdvileshi tvivtonac ar vici ra ar momwons
# ¯\_(ツ)_/¯
