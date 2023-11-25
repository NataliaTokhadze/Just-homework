#1. 2(12 + 6)(34+67) + 12/(3+6)

#1.1 es aris ioli da logikuri gamosavali

x = 2 * (12 + 6) * (34 + 67) + 12 / (3 + 6)
print (x)

#1.2 magram sheidzleba uqro dzneli gzit wasvla

y = 2
z = 12 + 6
c = 34 + 6
v = 12
b = 3 + 6
print( y * z * c + v / b)



#2. ((4 + 23)^2 + 56 + 89)(52 + 12)^6

#2

def myfunc():
    x = ((4 + 23)**2 + 56 + 89)*(52 + 12)**6
    print(x)

myfunc()



#3. radiusi = 5 . unda vipovot sigrdze da qartobi

#3

# S = пr^2 (kvadratshi)
# C = пd   (C aris sigrdze)
# d = 2r   (d aris diametri)

def myfunc():
    r = 5
    x = r**2
    txt = "answer is: S = п{}"
    print(txt.format(x))

    d = 2*r
    txt1 = "answer is: C = п{}"
    print(txt1.format(d))

myfunc()



#4. 200000 wami. ramdeni wutia?

#4

wami = 200000
wuti = wami / 60
print (wuti)



#5.

#S = 150000 km
#   T = 10000 hr
#   V = S/T = ?

S = 150000
T = 10000
V = S/T
print(V)



# Bonus

def myfunc():
    x = 2006
    y = "Jule"
    z = 18
    print (z , y , x)

myfunc()
