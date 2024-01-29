CPF = []
testes = []
qtd_testes,cpf_validos,cpf_invalidos = 0,0,0
while True:
    if qtd_testes != 0:
        print('\n')
    verify = input("Deseja testar CPF? [s/n]: ")
    if verify == 's':
        dados = dict()
        while True:
            dados['CPF'] = input("Digite seu CPF: ")
            if len(dados['CPF']) < 11:
                print("Digite CPF completo!")
            elif len(dados['CPF']) > 11:
                print("Numeros demais para ser CPF!")
            else:
                break

        CPF = dados['CPF']
        dig = [CPF[0],CPF[1],CPF[2],CPF[3],CPF[4],CPF[5],CPF[6],CPF[7],CPF[8]]
        mult = [10,9,8,7,6,5,4,3,2]

        soma1 = 0
        for i in range(9):
            soma1 = soma1 + (int(dig[i])*int(mult[i]))


        if soma1%11 <2:
            v1 = 0
        else:
            v1 = 11-(soma1%11)


        dig2 = [CPF[0],CPF[1],CPF[2],CPF[3],CPF[4],CPF[5],CPF[6],CPF[7],CPF[8],v1]
        mult2 = [11,10,9,8,7,6,5,4,3,2]
        soma2 = 0
        for i in range(10):
            soma2 = soma2 + (int(dig2[i])*int(mult2[i]))


        if soma2%11 <2:
            v2 = 0
        else:
            v2 = 11-(soma2%11)

        CPF_gerado = [CPF[0],CPF[1],CPF[2],CPF[3],CPF[4],CPF[5],CPF[6],CPF[7],CPF[8],str(v1),str(v2)]
        CPF_usuario = [CPF[0],CPF[1],CPF[2],CPF[3],CPF[4],CPF[5],CPF[6],CPF[7],CPF[8],CPF[9],CPF[10]]

        if CPF_usuario == CPF_gerado:
            dados['VALIDACAO'] = 'VÁLIDO'
            cpf_validos = cpf_validos + 1
        else:
            dados['VALIDACAO'] = 'INVÁLIDO'
            cpf_invalidos = cpf_invalidos + 1

        qtd_testes = qtd_testes + 1
        testes.append(dados.copy())
        print(dados['VALIDACAO'])
    else:
        break

if qtd_testes > 0:
    print("\n"+30*'='+'\n')
    print(f"QTD de CPF's testados: {qtd_testes}")
    print(f"QTD de CPF's VALIDOS: {cpf_validos}")
    print(f"QTD de CPF's INVALIDOS: {cpf_invalidos}")
    print(f"Porcentagem de CPF's VALIDOS: {(cpf_validos/qtd_testes)*100}%")
    print(f"Porcentagem de CPF's INVALIDOS: {(cpf_invalidos/qtd_testes)*100}%")
