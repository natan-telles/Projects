x=0
while True:
    verify = input('Deseja iniciar o programa? s/n ')
    if verify == "s":
        nome = input("Atleta: ")
        print(10*'=',"Entrada dos saltos em metros [m]",10*'=')
        s1 = float(input("1ºsalto: "))
        s2 = float(input("2ºsalto: "))
        s3 = float(input("3ºsalto: "))
        s4 = float(input("4ºsalto: "))
        s5 = float(input("5ºsalto: "))

        for i in range(4):
            for j in range(i+1,5):
                if globals()[f"s{j+1}"] > globals()[f"s{i+1}"]:
                    globals()[f"s{j+1}"],globals()[f"s{i+1}"] = globals()[f"s{i+1}"],globals()[f"s{j+1}"]


        melhor_salto = s1
        pior_salto = s5
        media = (s2+s3+s4)/3

        print(f"Melhor salto: {melhor_salto} m")
        print(f"Pior salto: {pior_salto} m")
        print(f"Média dos demais saltos: {media} m")
        print("")
        print("Resultado Final:")
        print(f"{nome}: {media} m")
        print("")
        print(50 * '-')
        print("")

        if x == 0:
            media_global = media
            campeao = nome


        x = x+1
        if media >= media_global:
            media_global = media
            campeao = nome


    if verify != "s":
        print(f"ATLETA CAMPEÃO: {campeao.upper()}")
        print(50*'=')
        break