
## Read me ##
## This code was made to get a Addresses Object and separate the relationed State from each other and print the quantity in each one ##


def SeparateDocsBreakingLines():

    list_Estados = []
    acre = 0
    alagoas = 0
    amazonas = 0
    amapa = 0
    bahia = 0
    ceara = 0
    distFederal = 0
    EspSanto = 0
    Goias = 0
    Maranhao = 0
    MinasGerais=0
    MGdoSul=0
    MatoGrosso=0
    Para=0
    Paraiba=0
    Pernambuco=0
    Piaui=0
    Parana=0
    RioDeJaneiro=0
    RioGrandeNorte=0
    Rondonia=0
    Roraima=0
    RioGrandeSul=0
    SantaCatarina=0
    Sergipe=0
    SaoPaulo=0
    Tocantins=0
    documents = open("C:\Code\Enderecos.txt", "r")
    for doc in documents:
        temp = doc.split("  ")
        for temp in temp:
            if "\tAC\tBrazil" in temp and "AdressesMainTrue" in temp:
                acre+=1
            elif "\tAL\tBrazil" in temp and "AdressesMainTrue" in temp:
                alagoas+=1
            elif "\tAM\tBrazil" in temp and "AdressesMainTrue" in temp:
                amazonas+=1
            elif "\tAP\tBrazil" in temp and "AdressesMainTrue" in temp:
                amapa+=1
            elif "\tBA\tBrazil" in temp and "AdressesMainTrue" in temp:
                bahia+=1
            elif "\tCE\tBrazil" in temp and "AdressesMainTrue" in temp:
                ceara+=1
            elif "\tDF\tBrazil" in temp and "AdressesMainTrue" in temp:
                distFederal+=1
            elif "\tES\tBrazil" in temp and "AdressesMainTrue" in temp:
                EspSanto+=1
            elif "\tGO\tBrazil" in temp and "AdressesMainTrue" in temp:
                Goias+=1
            elif "\tMA\tBrazil" in temp and "AdressesMainTrue" in temp:
                Maranhao+=1
            elif "\tMG\tBrazil" in temp and "AdressesMainTrue" in temp:
                MinasGerais+=1
            elif "\tMS\tBrazil" in temp and "AdressesMainTrue" in temp:
                MGdoSul+=1
            elif "\tMT\tBrazil" in temp and "AdressesMainTrue" in temp:
                MatoGrosso+=1
            elif "\tPA\tBrazil" in temp and "AdressesMainTrue" in temp:
                Para+=1
            elif "\tPB\tBrazil" in temp and "AdressesMainTrue" in temp:
                Paraiba+=1
            elif "\tPE\tBrazil" in temp and "AdressesMainTrue" in temp:
                Pernambuco+=1
            elif "\tPI\tBrazil" in temp and "AdressesMainTrue" in temp:
                Piaui+=1
            elif "\tPR\tBrazil" in temp and "AdressesMainTrue" in temp:
                Parana+=1
            elif "\tRJ\tBrazil" in temp and "AdressesMainTrue" in temp:
                RioDeJaneiro+=1
            elif "\tRN\tBrazil" in temp and "AdressesMainTrue" in temp:
                RioGrandeNorte+=1
            elif "\tRO\tBrazil" in temp and "AdressesMainTrue" in temp:
                Rondonia+=1
            elif "\tRR\tBrazil" in temp and "AdressesMainTrue" in temp:
                Roraima+=1
            elif "\tRS\tBrazil" in temp and "AdressesMainTrue" in temp:
                RioGrandeSul+=1
            elif "\tSC\tBrazil" in temp and "AdressesMainTrue" in temp:
                SantaCatarina+=1
            elif "\tSE\tBrazil" in temp and "AdressesMainTrue" in temp:
                Sergipe+=1
            elif "\tSP\tBrazil" in temp and "AdressesMainTrue" in temp:
                SaoPaulo+=1
            elif "\tTO\tBrazil" in temp and "AdressesMainTrue" in temp:
                Tocantins+=1

    list_Estados.append(acre)
    list_Estados.append(alagoas)
    list_Estados.append(amazonas)
    list_Estados.append(amapa)
    list_Estados.append(bahia)
    list_Estados.append(ceara)
    list_Estados.append(distFederal)
    list_Estados.append(EspSanto)
    list_Estados.append(Goias)
    list_Estados.append(Maranhao)
    list_Estados.append(MinasGerais)
    list_Estados.append(MGdoSul)
    list_Estados.append(MatoGrosso)
    list_Estados.append(Para)
    list_Estados.append(Paraiba)
    list_Estados.append(Pernambuco)
    list_Estados.append(Piaui)
    list_Estados.append(Parana)
    list_Estados.append(RioDeJaneiro)
    list_Estados.append(RioGrandeNorte)
    list_Estados.append(Roraima)
    list_Estados.append(Rondonia)
    list_Estados.append(RioGrandeSul)
    list_Estados.append(SantaCatarina)
    list_Estados.append(Sergipe)
    list_Estados.append(SaoPaulo)
    list_Estados.append(Tocantins)

    with open('States.txt', 'w') as f:
        for item in list_Estados:
            f.write(str(item)+"\n")

if __name__ == "__main__":
    SeparateDocsBreakingLines()