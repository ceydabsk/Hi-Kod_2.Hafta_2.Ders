liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

print(liste[3]) #"3" değeri
print(liste[5]) #"Hi-Kod" değeri
print(liste[7]) #4.7 değeri
print(liste[2:6]) #9,"3",8.4,"Hi-Kod"
print(liste[4:8]) #8.4,"Hi-Kod","False",4.7

yeni_liste=[liste[0],liste[3],liste[5],liste[6]]
print(yeni_liste) #Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

meyveler=["elma","armut","muz","çilek"] #Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.
for index,meyve in enumerate(meyveler):
    print(index,meyve)