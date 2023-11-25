#marto 2 davaleba unda davwero hehe >:)
#danarcheni klasshi gavakete

#1

cat = [3,3,3,4,4]
cat = sorted(cat)
paw = 1

blackcat = []
whitecat = []

for meow in range(0,len(cat)) :
    if cat[meow - 1] == cat[meow] :
        print(f"{cat[meow - 1]} - {paw} times")
        blackcat.append(1)
    else:
        print(f"{cat[meow]} - {paw} times")
        whitecat.append(1)


#print(f"{cat[meow - 1]} - {len(blackcat)} times")
#print(f"{cat[meow]} - {len(whitecat)} times")


#jerjerobit araa damtavrebuli da ar mushaobs
#vcdilobdi mepova axali gza
#da ar gadamewera saklasodan
#magram ar gamomivida T.T



#2

#chavtvalot, rom listia XD
list1 = { 1, 23, 545, 6, 6, 1, 7 , 8,4,6 ,86,5 ,76, 8 }
list2 = { 4, 87, 4,6 ,436, 3,46, 5 }
saerto = list1&list2
saerto = list(saerto)
print(saerto)



#3

llist = [3,4,3,5,6,54,5443,3,45,34,345,3,453,54,44444,44,444,4,4,4,4,44,4,4,4,4,44,4,4,4,4,4,4,4,4,4,4,4,4,44,4,4,4,4,4,4,4,4,4,4,444,44,4]
llist1 = sorted(llist)
no = []


for i in range(0, len(llist1)) :
    if llist1[i - 1] != llist1[i]:
        no.append(llist1[i])

print(no)



#4

dict1 = {
    "l" : 3 ,
    "o" : 2
}
print(sum(dict1.values()))



#5

vowel = ['a', 'e', 'i', 'o', 'u']

word = "meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow"

listword = list(word)
vowels = []
for p in vowel:
    if p in listword :
        vowels.append(p)
print(vowels)
print(len(vowels))



#6

wordd = "python"

listwordd = list(wordd)

print(listwordd)
print(len(listwordd))



#7

numberList = [15, 85, 35, 89, 125]
numberlist1 = sorted(numberList)
print(numberlist1[-1])



#8

listlist = []

i = 0

while i <=10 :
    if i % 2 == 0 :
        listlist.append(i)
    i+=1
listlist1 = sum(listlist)
print(listlist1)



#9
listt = []
i = 1

while i <= 10 :
    y = i**2
    listt.append(y)
    i += 1

print(listt)