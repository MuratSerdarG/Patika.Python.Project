#Çalışmayı devam ettirmek için ham veriler.


import pandas as pd
from math import sqrt
#values referances:https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html
covid19={"vaka":[1480,1344,1193,1132,1253,1743,1661,1480,1542,1858,1670,1778,1534,1407,1154,1254,1608,1443,1485,1017,1264,905,922,1304,1260,1310,940,966,864,908,975],"test":[108802,97783,92562,90301,101263,135316,102242,98758,109958,134646,129362,135738,134027,127538,120183,128957,138894,135563,137730,129945,138386,118852,123536,136332,137573,139482,134252,138752,129961,133352,128854],"iyilesen":[2113,1402,1354,1185,1782,2239,1843,1526,1463,1511,1711,1816,1673,1645,1190,1358,1219,1274,1389,1148,1219,1019,1105,1184,1225,1289,1237,1104,1107,1005,946],"vefat":[12,8,10,7,11,7,11,9,8,7,9,8,7,5,10,4,7,3,4,4,3,5,3,6,4,5,4,3,2,4,4]}
covidt=pd.DataFrame(covid19)
vaka_ay_ort=int(covidt.vaka.mean())
test_ay_ort=int(covidt.test.mean())
iyilesen_ay_ort=int(covidt.iyilesen.mean())
vefat_ay_ort=int(covidt.vefat.mean())
"""l=31
clist=[]
for i in range(l):
    z=covidt.vaka[i]
    clist.append(z)"""


#Anlam düzeyi 0~50 puan arasında
mont=int((covidt.vefat-covidt.vefat.mean()).pow(2).sum())
filt=(covidt.vaka<=1000)
c1=covidt[filt]
c2=covidt[~filt]
kont=int((c1.vefat-c1.vefat.mean()).pow(2).sum()+(c2.vefat-c2.vefat.mean()).pow(2).sum())
filt2=(c2.vaka<=1250)
c3=c2[filt2]
c4=c2[~filt2]
filt3=(c4.vaka<=1500)
c5=c4[filt3]
c6=c4[~filt3]
filt4=(c6.vaka<=1750)
c7=c6[filt4]
c8=c6[~filt4]

print(int(c1.vefat.mean())) #Anlam Düzeyi:
print(int(c3.vefat.mean())) #Anlam Düzeyi:
print(int(c5.vefat.mean())) #Anlam Düzeyi:
print(int(c7.vefat.mean())) #Anlam Düzeyi:
print(int(c8.vefat.mean())) #Anlam Düzeyi:
