## Read Me ##
## In this case, we have an object of Process, and the goal is to take off Criminal, Trabalhista and Tributaria kind of processes ##

def GetClaimedDefendantDocs():
    list_passive_process = []
    parties = open("C:\Code\People_Partes.txt", "r")
    for party in parties:
        type = party.split("|")
        if type[0] == type[4]:
            if type[7] != 'NEUTRAL' and type[7] != 'ACTIVE':
                list_passive_process.append(type[1])

    list_passive_process = list(set(list_passive_process))
    return list_passive_process

def RemoveCriminalProcess(passive_processes, list_criminal_words):
    list_civel_process = []
    documents = open("C:\Projects\Scripts\Processes_PessoaFisica.txt", "r")
    for process in documents:
        processInfo = process.split("|")
        if processInfo[1] not in passive_processes and processInfo[1] != 'Numero':
            continue
        elif processInfo[2] in list_criminal_words or processInfo[6] == 'TRABALHISTA' or processInfo[6] == 'TRIBUTARIA' or processInfo[6] == 'CRIMINAL':
            continue
        else:
            list_civel_process.append(process)

    with open('ProcessoCivel_PessoaFisica.txt', 'w') as f:
        for item in list_civel_process:
            f.write(str(item))


list_criminal_words = [
"AGRAVO DE EXECUCAO PENAL",
"AGRAVO DE INSTRUMENTO EM RECURSO ESPECIAL",
"AGRAVO DE INSTRUMENTO EM RECURSO EXTRAORDINARIO",
"AGRAVO REGIMENTAL CRIMINAL",
"ALIENACAO DE BENS DO ACUSADO",
"ANISTIA",
"APELACAO CRIMINAL",
"APELACAO EM MANDADO DE SEGURANCA",
"ARRESTO / HIPOTECA LEGAL",
"AUTO DE PRISAO",
"AUTO DE PRISAO EM FLAGRANTE",
"AVALIACAO PARA ATESTAR DEPENDENCIA DE DROGAS",
"ACAO PENAL",
"CARTA DE ORDEM CRIMINAL",
"CARTA PRECATORIA CRIMINAL",
"CARTA TESTEMUNHAVEL",
"CAUTELAR INOMINADA CRIMINAL",
"COMUTACAO DE PENA",
"CONVERSAO DE PENA",
"CORREICAO PARCIAL CRIMINAL",
"CRIMES AMBIENTAIS",
"CRIMES CONTRA A PROPRIEDADE IMATERIAL",
"CRIMES CONTRA A PROPRIEDADE INDUSTRIAL",
"CRIMES CONTRA A PROPRIEDADE INTELECTUAL",
"CRIMES DE CALUNIA, INJURIA E DIFAMACAO DE COMPETENCIA DO JUIZ SINGULAR",
"CRIMES DE IMPRENSA",
"CRIMES DE RESPONSABILIDADE DOS FUNCIONARIOS PUBLICOS",
"EMBARGOS DE DECLARACAO CRIMINAL",
"EMBARGOS DE TERCEIRO",
"EMBARGOS DO ACUSADO",
"EMBARGOS INFRINGENTES E DE NULIDADE",
"EXCESSO OU DESVIO",
"EXCECAO DA VERDADE",
"EXCECAO DE COISA JULGADA",
"EXCECAO DE ILEGITIMIDADE DE PARTE",
"EXCECAO DE IMPEDIMENTO",
"EXECUCAO CRIMINAL",
"EXECUCAO DA PENA",
"EXECUCAO DE MEDIDA DE SEGURANCA",
"EXIBICAO DE DOCUMENTO OU COISA CRIMINAL",
"HABEAS CORPUS CRIMINAL",
"HOMOLOGACAO EM ACORDO DE COLABORACAO PREMIADA",
"INCIDENTE DE ARGUICAO DE INCONSTITUCIONALIDADE CRIMINAL",
"INDULTO",
"INQUERITO POLICIAL",
"INSANIDADE MENTAL DO ACUSADO",
"INVESTIGACAO CONTRA MAGISTRADO",
"LIBERDADE PROVISORIA COM OU SEM FIANCA",
"LIVRAMENTO CONDICIONAL",
"MANDADO DE SEGURANCA CRIMINAL",
"MEDIDAS INVESTIGATORIAS SOBRE ORGANIZACOES CRIMINOSAS",
"MEDIDAS PROTETIVAS",
"ESTATUTO DO IDOSO CRIMINAL",
"LEI MARIA DA PENHA",
"NOTICIA DE CRIME",
"NOTICIA-CRIME",
"PEDIDO DE ARQUIVAMENTO EM REPRESENTACAO CRIMINAL",
"PEDIDO DE BUSCA E APREENSAO CRIMINAL",
"PEDIDO DE PRISAO",
"PEDIDO DE PRISAO PREVENTIVA",
"PEDIDO DE PRISAO TEMPORARIA",
"PEDIDO DE QUEBRA DE SIGILO DE DADOS E/OU TELEFONICO",
"PETICAO CRIMINAL",
"PROCEDIMENTO ESPECIAL DA LEI ANTITOXICOS",
"PROCEDIMENTO ESPECIAL DOS CRIMES DE ABUSO DE AUTORIDADE",
"PROCEDIMENTO INVESTIGATORIO CRIMINAL",
"PROCEDIMENTO INVESTIGATORIO CRIMINAL (PIC-MP)",
"PROCESSO DE APLICACAO DE MEDIDA DE SEGURANCA POR FATO NAO CRIMINOSO",
"PROCESSO ESPECIAL DO CODIGO DE PROCESSO PENAL",
"PRODUCAO ANTECIPADA DE PROVAS CRIMINAL",
"PROGRESSAO DE REGIME",
"PROTESTO POR NOVO JURI",
"REABILITACAO",
"RECLAMACAO CRIMINAL",
"RECURSO EM SENTIDO ESTRITO",
"RECURSO EM SENTIDO ESTRITO/RECURSO EX OFFICIO",
"REGRESSAO DE REGIME",
"RELAXAMENTO DE PRISAO",
"REMESSA NECESSARIA CRIMINAL",
"REMICAO DE PENA",
"REPRESENTACAO CRIMINAL",
"REPRESENTACAO CRIMINAL/NOTICIA DE CRIME",
"RESTAURACAO DE AUTOS",
"RESTITUICAO DE COISAS APREENDIDAS",
"REVISAO CRIMINAL",
"ROTEIRO DE PENA",
"SEQUESTRO",
"TRANSFERENCIA ENTRE ESTABELECIMENTOS PENAIS",
"UNIFICACAO DE PENAS",

]

if __name__ == "__main__":
    passive_processes = []
    passive_processes = GetClaimedDefendantDocs()
    RemoveCriminalProcess(passive_processes, list_criminal_words)