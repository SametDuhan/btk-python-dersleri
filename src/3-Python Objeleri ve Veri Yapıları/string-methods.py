message = 'Hello There. My name is Sadık Turan'
message = message.split()


# message = message.upper()  TÜM STRİNGİ BÜYÜK YAZAR
# message = message.lower()  TÜM STRİNG KÜÇÜK HARFLE YAZILIR
# message = message.title()  STRİNGDELİ KELİMLERİN YALNIZCA BAŞ HARFİ BÜYÜK HARFKE YAZILIR
# message = message.capitalize()  STRİNGİN SADECE İLK KELİMESİNİN İLK HARFİNİ BÜYÜK YAZAR

# message = message.strip()  STRİNGİN BAŞINDA BOŞLUK VARSA O BOŞLUĞU SİLER
# message = message.split()  STRİNGDEKİ KELİMELERİ BOŞLUKLARA GÖRE AYIRIP HER BİRİNİ BİR LİSTENİN ELEMANI YAPAR
# message = message.split('.')  STRİNGDEKİ KELİMELERİ NOKTALARA GÖRE AYIRIP HER BİRİNİ BİR LİSTENİN ELEMANI YAPAR
#message = ' '.join(message)  STRİNDEKİ ELEMANLARI ARALARINDA BOŞLUK OACAK ŞEKİLDE BİRLEŞTİRİR
# message= '---'.join(message)  

# index = message.find('Sadık')  VERİLEN KELİMEYİ ARAR EĞER BULURSA KELİMENİN İLK STRİNGİNİN İNDEXİNİ DÖNER , BULAMAZSA -1 DÖNER
# isFound = message.startswith('H') 
# isFound = message.endswith('n') 

# message = message.replace('Sadık','Çınar') SADIK YERİNE ÇINAR YAZ
# message = message.replace('ç','c') Ç YERİNE C YAZ
#                  .replace('ö','o') Ö YERİNE O YAZ
#                  .replace(' ','-') BOŞLUK YERİNE - YAZ

# message = message.center(50,'*')  STRİNGİ 50 KARAKTERLİK BİR YERE YAZAR VE BOŞ OLAN YERLERE YILDIZ KOYAR

print(message)
