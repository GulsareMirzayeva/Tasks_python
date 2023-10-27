#Task1

# veritabanı = {
#     "Aslan": "Aslan, Aslan emi ogludur",
#     "Imran": "Imran, Imran dayi ogludur",
#     "Afaq": "Afaq, Afaq bibi qizidir",
#     "Uzeyir": "Uzeyir, Uzeyir xala ogludur",
#     "Shahin": "Shahin, Shahin yaxin dostdur"
# }

# ad = input("Zəhmət olmasa bir ad daxil edin: ")

# if ad:
#     if ad in veritabanı:
#         print(veritabanı[ad])
#     else:
#         print(f"{ad} kimdir? Mən onu tanımadım")
# else:
#     print("Siz ad daxil etməmisiniz")



# Task2
# Login və parol yoxlanışı

# login = input("Login: ")
# parol = input("Parol: ")

# dogru_login = "test"
# dogru_parol = "12345"

# if login == dogru_login and parol == dogru_parol:
#     print("Hoş geldiniz")
# elif login != dogru_login and parol != dogru_parol:
#     print("Login və parol yanlışdır")
# elif login != dogru_login:
#     print("Login yanlışdır")
# elif parol != dogru_parol:
#     print("Parol yanlışdır")
# elif not login:
#     print("Login daxil etmədiniz")
# elif not parol:
#     print("Parol daxil etmədiniz")


# Task3
# istifadəçidən 3 rəqəm alın və ən böyük rəqəmi ekrana yazdırın

# try:
#     r1 = int(input("Birinci rəqəmi daxil edin: "))
#     r2 = int(input("İkinci rəqəmi daxil edin: "))
#     r3 = int(input("Üçüncü rəqəmi daxil edin:"))

#     en_boyuk_reqem = max(r1, r2, r3)

#     print(f"Ən böyük rəqəm: {en_boyuk_reqem}")
# except ValueError:
#     print("Xahiş edirik yalnızca rəqəm daxil edin.")

# Task4

# boy = float(input("Boyunuzu Daxil edin (metr): "))
# kütle = float(input("Kütləni Daxil edin (kilogram): "))

# bki = kütle / (boy ** 2)

# if bki < 18.5:
#     durum = "Zəif"
# elif 18.5 <= bki < 25:
#     durum = "Normal"
# elif 25 <= bki < 30:
#     durum = "Kilolu"
# else:
#     durum = "Obez"

# print(f"Vücut Kitle İndeksi (BKİ): 63")
# print(f"Durum: {durum}")


# Task 6

# test_list = [5, 6, [], 3, [], [], 9]

# temiz_list = []
# for item in test_list:
#     if item != []:
#         temiz_list.append(item)

# for eded in temiz_list:
#     print(eded)


# Task 7

# adlar = []

# while True:
#     ad = input("Ad daxil edin (maksimum 15 hərf): ").strip()

#     if len(ad) == 0:
#         print("Ad daxil etmediniz.")
#     elif len(ad) > 15:
#         print("Ad çox uzundur, maksimum 15 hərf daxil edin.")
#     else:
#         adlar.append(ad)
#         print(f"Ad {ad} Bazaya uğurla əlavə edildi.")
