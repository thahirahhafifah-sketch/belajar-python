# kalo kondisinya benar=if jalan,kalo kondisinya salah=else jalan
inputan = int(input("masukan angka: "))
if inputan > 75:
    print("maka anda lulus")
else:
    print("anda tidak lulus")




# elif : beberapa kondisi setelah if, jika kondisi if salah maka akan mengecek kondisi elif, jika kondisi elif salah maka akan mengecek kondisi else



nilai = int(input("masukan angka: "))
if nilai > 75:
    print("maka anda lulus")
elif nilai > 50:
    print("anda lulus dengan nilai pas-pasan")
elif nilai > 25:
    print("anda lulus dengan nilai kurang")
else:
    print("anda tidak lulus")
