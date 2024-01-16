cont=0
while True:
    verify = input('Deseja iniciar o programa? s/n ')
    if verify == "s":
        nome = input("Atleta: ")
        print(10*'=',"Entrada dos saltos em metros [m]",10*'=')
        saltos = [float(input("1ºsalto: ")), float(input("2ºsalto: ")), float(input("3ºsalto: ")),
                  float(input("4ºsalto: ")), float(input("5ºsalto: "))]

        x = saltos
        x.remove((max(saltos)))
        x.remove(min(saltos))
        media = (x[0] + x[1] + x[2]) / 3

        print(f"Melhor salto: {max(saltos)} m")
        print(f"Pior salto: {min(saltos)} m")
        print(f"Média dos demais saltos: {media} m")
        print("")
        print("Resultado Final:")
        print(f"{nome}: {media} m")
        print("")
        print(50 * '-')
        print("")

        if cont == 0:
            media_global = media
            campeao = nome


        cont = cont+1
        if media >= media_global:
            media_global = media
            campeao = nome


    if verify != "s":
        print(f"ATLETA CAMPEÃO: {campeao.upper()}")
        print(50*'=')
        break