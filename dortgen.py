m = input("yan kenari giriniz: ")
h = input("dik kenari girin: ")

m *= 2

dortgen = " "

for i in range(m) :
        dortgen += "_"
print dortgen
dortgen = ""

for j in range(h) :
        dortgen += "|"
        for k in range(m) :
                if j == h-1 :
                        dortgen += "_"
                else :
                        dortgen += " "

        dortgen += "|"
        print dortgen
        dortgen = ""
