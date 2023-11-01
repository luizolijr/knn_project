import pandas as pd
import numpy as np
import streamlit as st
import folium
from streamlit_folium import folium_static
from statistics import mean




data = [[66707599984, 'Conservador', (5100., 3500., 1400., 200.)],
[55695397315, 'Conservador', (4900., 3000., 1400., 200.)],
[55941368774, 'Conservador', (4600., 3100., 1500., 200.)],
[75486280874, 'Conservador', (5000., 3600., 1400., 200.)],
[53164949799, 'Conservador', (5400., 3900., 1700., 400.)],
[39898704131, 'Conservador', (4600., 3400., 1400., 300.)],
[53740901207, 'Conservador', (5000., 3400., 1500., 200.)],
[51735950236, 'Conservador', (4400., 2900., 1400., 200.)],
[47305108951, 'Conservador', (4900., 3100., 1500., 100.)],
[63858864633, 'Conservador', (5400., 3700., 1500., 200.)],
[53363167240, 'Conservador', (4800., 3400., 1600., 200.)],
[72133754195, 'Conservador', (4800., 3000., 1400., 100.)],
[52802483512, 'Conservador', (4300., 3000., 1100., 100.)],
[57925287214, 'Conservador', (4800., 3400., 1900., 200.)],
[64020216626, 'Conservador', (5000., 3400., 1600., 400.)],
[78223722856, 'Conservador', (5200., 3500., 1500., 200.)],
[58245228846, 'Conservador', (5200., 3400., 1400., 200.)],
[74490686776, 'Conservador', (4700., 3200., 1600., 200.)],
[77381458676, 'Conservador', (5400., 3400., 1500., 400.)],
[70276304567, 'Conservador', (4900., 3100., 1500., 200.)],
[56457227894, 'Conservador', (4900., 3600., 1400., 100.)],
[46939428126, 'Conservador', (4400., 3000., 1300., 200.)],
[60979942480, 'Conservador', (5100., 3400., 1500., 200.)],
[41648583220, 'Conservador', (5000., 3500., 1300., 300.)],
[50376331791, 'Conservador', (4500., 2300., 1300., 300.)],
[62830733382, 'Conservador', (5100., 3800., 1900., 400.)],
[56716675811, 'Conservador', (4800., 3000., 1400., 300.)],
[61089667146, 'Conservador', (5100., 3800., 1600., 200.)],
[47795509468, 'Conservador', (4600., 3200., 1400., 200.)],
[53433670705, 'Conservador', (5000., 3300., 1400., 200.)],
[54850120580, 'Moderado', (7000., 3200., 4700., 1400.)],
[67692777563, 'Moderado', (6900., 3100., 4900., 1500.)],
[43133573182, 'Moderado', (5500., 2300., 4000., 1300.)],
[55150612815, 'Moderado', (6500., 2800., 4600., 1500.)],
[48211725243, 'Moderado', (5700., 2800., 4500., 1300.)],
[76686463776, 'Moderado', (6300., 3300., 4700., 1600.)],
[40307235992, 'Moderado', (6600., 2900., 4600., 1300.)],
[45735414894, 'Moderado', (5900., 3200., 4800., 1800.)],
[57137146514, 'Moderado', (6100., 2800., 4000., 1300.)],
[53657058251, 'Moderado', (6300., 2500., 4900., 1500.)],
[52941460485, 'Moderado', (6100., 2800., 4700., 1200.)],
[44306600683, 'Moderado', (6400., 2900., 4300., 1300.)],
[75590376075, 'Moderado', (6800., 2800., 4800., 1400.)],
[77567920298, 'Moderado', (6000., 2900., 4500., 1500.)],
[67600419504, 'Moderado', (5700., 2600., 3500., 1000.)],
[44902189811, 'Moderado', (5500., 2400., 3800., 1100.)],
[56182108880, 'Moderado', (5800., 2700., 3900., 1200.)],
[78299785392, 'Moderado', (6000., 2700., 5100., 1600.)],
[57381925887, 'Moderado', (6000., 3400., 4500., 1600.)],
[65654934891, 'Moderado', (6700., 3100., 4700., 1500.)],
[56130640481, 'Moderado', (6300., 2300., 4400., 1300.)],
[59667611672, 'Moderado', (5600., 3000., 4100., 1300.)],
[40349334385, 'Moderado', (5500., 2500., 4000., 1300.)],
[68422640081, 'Moderado', (5500., 2600., 4400., 1200.)],
[55245923439, 'Moderado', (6100., 3000., 4600., 1400.)],
[41065279767, 'Moderado', (5000., 2300., 3300., 1000.)],
[42866454119, 'Moderado', (5600., 2700., 4200., 1300.)],
[49475220139, 'Moderado', (6200., 2900., 4300., 1300.)],
[52245218531, 'Moderado', (5100., 2500., 3000., 1100.)],
[50932926697, 'Moderado', (5700., 2800., 4100., 1300.)],
[47432932248, 'Agressivo', (6300., 3300., 6000., 2500.)],
[39321991579, 'Agressivo', (5800., 2700., 5100., 1900.)],
[46283759608, 'Agressivo', (7100., 3000., 5900., 2100.)],
[56996272538, 'Agressivo', (6300., 2900., 5600., 1800.)],
[77232189978, 'Agressivo', (6500., 3000., 5800., 2200.)],
[42857147573, 'Agressivo', (4900., 2500., 4500., 1700.)],
[71422443953, 'Agressivo', (7200., 3600., 6100., 2500.)],
[72508507904, 'Agressivo', (6900., 3200., 5700., 2300.)],
[41188727558, 'Agressivo', (5600., 2800., 4900., 2000.)],
[66934042323, 'Agressivo', (6300., 2700., 4900., 1800.)],
[40622495567, 'Agressivo', (6700., 3300., 5700., 2100.)],
[45159362930, 'Agressivo', (6200., 2800., 4800., 1800.)],
[45018975174, 'Agressivo', (6100., 3000., 4900., 1800.)],
[56363906548, 'Agressivo', (7400., 2800., 6100., 1900.)],
[39646194720, 'Agressivo', (7900., 3800., 6400., 2000.)],
[75796138061, 'Agressivo', (6300., 2800., 5100., 1500.)],
[53595767857, 'Agressivo', (6100., 2600., 5600., 1400.)],
[48758828080, 'Agressivo', (7700., 3000., 6100., 2300.)],
[58387651356, 'Agressivo', (6300., 3400., 5600., 2400.)],
[72846931192, 'Agressivo', (6400., 3100., 5500., 1800.)],
[47046896346, 'Agressivo', (6000., 3000., 4800., 1800.)],
[48177836349, 'Agressivo', (6700., 3100., 5600., 2400.)],
[57976326635, 'Agressivo', (6900., 3100., 5100., 2300.)],
[55710813002, 'Agressivo', (5800., 2700., 5100., 1900.)],
[64028580439, 'Agressivo', (6800., 3200., 5900., 2300.)],
[47250893163, 'Agressivo', (6700., 3000., 5200., 2300.)],
[75559276274, 'Agressivo', (6300., 2500., 5000., 1900.)],
[58529878272, 'Agressivo', (6500., 3000., 5200., 2000.)],
[76005896622, 'Agressivo', (6200., 3400., 5400., 2300.)],
[49212614633, 'Agressivo', (5900., 3000., 5100., 1800.)]]

no_class = [[45926320819, '', (5800., 4000., 1200., 200.)],
 [52559670741, '', (5700., 4400., 1500., 400.)],
 [59016004832, '', (5400., 3900., 1300., 400.)],
 [66175672425, '', (5100., 3500., 1400., 300.)],
 [53330429526, '', (5700., 3800., 1700., 300.)],
 [43765563403, '', (5100., 3800., 1500., 300.)],
 [68020822591, '', (5400., 3400., 1700., 200.)],
 [53939481689, '', (5100., 3700., 1500., 400.)],
 [47014057561, '', (4600., 3600., 1000., 200.)],
 [57183542047, '', (5100., 3300., 1700., 500.)],
            
 [68518284363, '', (5000., 2000., 3500., 1000.)],
 [65806049885, '', (5900., 3000., 4200., 1500.)],
 [54128073086, '', (6000., 2200., 4000., 1000.)],
 [41306785494, '', (6100., 2900., 4700., 1400.)],
 [65234831039, '', (5600., 2900., 3600., 1300.)],
 [50964498067, '', (6700., 3100., 4400., 1400.)],
 [50810951429, '', (5600., 3000., 4500., 1500.)],
 [48765044397, '', (5800., 2700., 4100., 1000.)],
 [41960083761, '', (6200., 2200., 4500., 1500.)],
 [76657763082, '', (5600., 2500., 3900., 1100.)],
            
 [64726487742, '', (6500., 3200., 5100., 2000.)],
 [75746566283, '', (6400., 2700., 5300., 1900.)],
 [78576734793, '', (6800., 3000., 5500., 2100.)],
 [56440141847, '', (5700., 2500., 5000., 2000.)],
 [66827423000, '', (5800., 2800., 5100., 2400.)],
 [45267873396, '', (6400., 3200., 5300., 2300.)],
 [46387191493, '', (6500., 3000., 5500., 1800.)],
 [54273611732, '', (7700., 3800., 6700., 2200.)],
 [75135392881, '', (7700., 2600., 6900., 2300.)],
 [64703873108, '', (6000., 2200., 5000., 1500.)],
            
 [65441690046, '', (5500., 3500., 1300., 200.)],
 [48646824781, '', (4800., 3100., 1600., 200.)],
 [52163844491, '', (5500., 4200., 1400., 200.)],
 [63743886918, '', (4700., 3200., 1300., 200.)],
 [72149193419, '', (5000., 3500., 1600., 600.)],
 [74354632224, '', (5000., 3000., 1600., 200.)],
 [67008801023, '', (4400., 3200., 1300., 200.)],
 [69119828185, '', (5000., 3200., 1200., 200.)],
 [41615431874, '', (5200., 4100., 1500., 100.)],
 [60899885693, '', (5300., 3700., 1500., 200.)],
            
 [44826533081, '', (5200., 2700., 3900., 1400.)],
 [62966866614, '', (5500., 2400., 3700., 1000.)],
 [68267282206, '', (6700., 3000., 5000., 1700.)],
 [71971000560, '', (4900., 2400., 3300., 1000.)],
 [43460747924, '', (6600., 3000., 4400., 1400.)],
 [51286696873, '', (5800., 2600., 4000., 1200.)],
 [45206071878, '', (5400., 3000., 4500., 1500.)],
 [48623501235, '', (5700., 2900., 4200., 1300.)],
 [71457789994, '', (6400., 3200., 4500., 1500.)],
 [61962944542, '', (5700., 3000., 4200., 1200.)],
            
 [61358776640, '', (7700., 2800., 6700., 2000.)],
 [57221661311, '', (7200., 3200., 6000., 1800.)],
 [70685429140, '', (6400., 2800., 5600., 2100.)],
 [49962942971, '', (6700., 3300., 5700., 2500.)],
 [48130345228, '', (6700., 2500., 5800., 1800.)],
 [61808723477, '', (7200., 3000., 5800., 1600.)],
 [55385494438, '', (6400., 2800., 5600., 2200.)],
 [77183282421, '', (7600., 3000., 6600., 2100.)],
 [39331584043, '', (7300., 2900., 6300., 1800.)],
 [69730292799, '', (6900., 3100., 5400., 2100.)]]            
    
matriz_confusao = [[65441690046, 'Conservador', (5500., 3500., 1300., 200.)],
[48646824781, 'Conservador', (4800., 3100., 1600., 200.)],
[52163844491, 'Conservador', (5500., 4200., 1400., 200.)],
[63743886918, 'Conservador', (4700., 3200., 1300., 200.)],
[72149193419, 'Conservador', (5000., 3500., 1600., 600.)],
[74354632224, 'Conservador', (5000., 3000., 1600., 200.)],
[67008801023, 'Conservador', (4400., 3200., 1300., 200.)],
[69119828185, 'Conservador', (5000., 3200., 1200., 200.)],
[41615431874, 'Conservador', (5200., 4100., 1500., 100.)],
[60899885693, 'Conservador', (5300., 3700., 1500., 200.)],
[44826533081, 'Moderado', (5200., 2700., 3900., 1400.)],
[62966866614, 'Moderado', (5500., 2400., 3700., 1000.)],
[68267282206, 'Moderado', (6700., 3000., 5000., 1700.)],
[71971000560, 'Moderado', (4900., 2400., 3300., 1000.)],
[43460747924, 'Moderado', (6600., 3000., 4400., 1400.)],
[51286696873, 'Moderado', (5800., 2600., 4000., 1200.)],
[45206071878, 'Moderado', (5400., 3000., 4500., 1500.)],
[48623501235, 'Moderado', (5700., 2900., 4200., 1300.)],
[71457789994, 'Moderado', (6400., 3200., 4500., 1500.)],
[61962944542, 'Moderado', (5700., 3000., 4200., 1200.)],
[61358776640, 'Agressivo', (7700., 2800., 6700., 2000.)],
[57221661311, 'Agressivo', (7200., 3200., 6000., 1800.)],
[70685429140, 'Agressivo', (6400., 2800., 5600., 2100.)],
[49962942971, 'Agressivo', (6700., 3300., 5700., 2500.)],
[48130345228, 'Agressivo', (6700., 2500., 5800., 1800.)],
[61808723477, 'Agressivo', (7200., 3000., 5800., 1600.)],
[55385494438, 'Agressivo', (6400., 2800., 5600., 2200.)],
[77183282421, 'Agressivo', (7600., 3000., 6600., 2100.)],
[39331584043, 'Agressivo', (7300., 2900., 6300., 1800.)],
[69730292799, 'Agressivo', (6900., 3100., 5400., 2100.)]]




# Contar maior número de ocorrências
def counter(vizinhos):
    conservador = 0
    moderado = 0
    agressivo = 0
    lista = []
    perfil_e_ocorrencia = []

    perfil = [vizinho[0] for vizinho in vizinhos]
    for i in perfil:
        if i == 'Conservador':
            conservador += 1
        if i == "Moderado":
            moderado += 1
        if i == "Agressivo":
            agressivo += 1

    lista.append([conservador, moderado, agressivo])
    lista = lista[0]
    ordenacao = sorted(lista, reverse=True)
    maior_ocorrencia = ordenacao[0]
    indice = lista.index(maior_ocorrencia)
    if indice == 0:
        perfil_e_ocorrencia.append((f'Conservador', maior_ocorrencia))
    if indice == 1:
        perfil_e_ocorrencia.append((f'Moderado', maior_ocorrencia))
    if indice == 2:
        perfil_e_ocorrencia.append((f'Agressivo', maior_ocorrencia))

    return perfil_e_ocorrencia[0][0]


# Calcular a distância Euclidiana entre dois pontos
def distancia_euclidiana(ponto1, ponto2):
    distancia = 0
    for i in range(len(ponto1)):
        distancia += (ponto1[i] - ponto2[i]) ** 2
    return (distancia**0.5)


# Ordenação dos vizinhos mais proximos com base na distancia
def segundo_elemento(item):
    return item[1]


# Classificação do ponto com base nos vizinhos mais próximos
def classificar_ponto(data, ponto, k):

    distancias = []

    for item in data:
        perfil = item[1]
        investimento = item[2]
        distancia = (distancia_euclidiana(ponto, investimento))
        distancias.append((perfil, distancia))

    distancias.sort(key=segundo_elemento)

    vizinhos = distancias[:k]


    perfil = counter(vizinhos)

    return perfil
    return distancias[1]


def gerar_resultado(matriz_confusao, no_class):

    resultado = []
    conservador_previsto = 0
    moderado_previsto = 0
    agressivo_previsto = 0

    conservador_gabarito = 0
    moderado_gabarito = 0
    agressivo_gabarito = 0


    for item_mc in matriz_confusao:
        cpf_mc, perfil_mc, _ = item_mc
        for item_nc in no_class:
            cpf_nc, perfil_nc, _ = item_nc
            if cpf_mc == cpf_nc:
                resultado.append((cpf_mc, perfil_nc, perfil_mc))

    for i in resultado:
        if i[1] == 'Conservador':
            conservador_previsto += 1
        if i[1] == 'Moderado':
            moderado_previsto += 1
        if i[1] == 'Agressivo':
            agressivo_previsto += 1

        if i[2] == 'Conservador':
            conservador_gabarito += 1
        if i[2] == 'Moderado':
            moderado_gabarito += 1
        if i[2] == 'Agressivo':
            agressivo_gabarito += 1


    # PRECISÃO(quando eu chuto, eu acerto) - sabemos que no gabarito temos 10 de cada classe
    # tp/(tp+fp)
    # Precisão Conservador
    if conservador_previsto <= conservador_gabarito:
      precisao_conservador = conservador_previsto/conservador_previsto

    elif conservador_previsto > conservador_gabarito:
      precisao_conservador = conservador_gabarito/(conservador_gabarito+(conservador_previsto-conservador_gabarito))

    # Precisão Moderado
    if moderado_previsto <= moderado_gabarito:
        if moderado_previsto != 0:
            precisao_moderado = moderado_previsto/moderado_previsto
        else:
            precisao_moderado = 0
            pass

    elif moderado_previsto > moderado_gabarito:
      precisao_moderado = moderado_gabarito/(moderado_gabarito+(moderado_previsto-moderado_gabarito))

    # Precisão Agressivo
    if agressivo_previsto <= agressivo_gabarito:
        if agressivo_previsto != 0:
            precisao_agressivo = agressivo_previsto/agressivo_previsto
        else:
            precisao_agressivo = 0
            pass

    elif agressivo_previsto > agressivo_gabarito:
      precisao_agressivo = agressivo_gabarito/(agressivo_gabarito+(agressivo_previsto-agressivo_gabarito))


    # RECALL(dos que existem, não esqueço nenhum)
    # tp/(tp+fn)
    # Recall Conservador
    if conservador_previsto <= conservador_gabarito:
      recall_conservador = conservador_previsto/(conservador_previsto+(conservador_gabarito-conservador_previsto))

    elif conservador_previsto > conservador_gabarito:
      recall_conservador = conservador_gabarito/conservador_previsto

    # Recall Moderado
    if moderado_previsto <= moderado_gabarito:
      recall_moderado = moderado_previsto/(moderado_previsto+(moderado_gabarito-moderado_previsto))

    elif moderado_previsto > moderado_gabarito:
      recall_moderado = moderado_gabarito/moderado_previsto

    # Recall Agressivo
    if agressivo_previsto <= agressivo_gabarito:
      recall_agressivo = agressivo_previsto/(agressivo_previsto+(agressivo_gabarito-agressivo_previsto))

    elif agressivo_previsto > agressivo_gabarito:
      recall_agressivo = agressivo_gabarito/agressivo_previsto


    # ACURÁCIA
    if conservador_previsto == conservador_gabarito:
        acc_conservador = conservador_previsto
    elif conservador_previsto > conservador_gabarito:
        acc_conservador = conservador_gabarito
    else:
        acc_conservador = conservador_previsto

    if moderado_previsto == moderado_gabarito:
        acc_moderado = moderado_previsto
    elif moderado_previsto > moderado_gabarito:
        acc_moderado = moderado_gabarito
    else:
        acc_moderado = moderado_previsto

    if agressivo_previsto == agressivo_gabarito:
        acc_agressivo = agressivo_previsto
    elif agressivo_previsto > agressivo_gabarito:
        acc_agressivo = agressivo_gabarito
    else:
        acc_agressivo = agressivo_previsto

    

    acuracia = (acc_conservador + acc_moderado + acc_agressivo) / (conservador_gabarito + moderado_gabarito + agressivo_gabarito)

    # st.markdown(f"""
    # **Conservador previsto:** {conservador_previsto}, **Gabarito:** {conservador_gabarito}\n
    # **Moderado previsto:** {moderado_previsto}, **Gabarito:** {moderado_gabarito}\n
    # **Agressivo previsto:** {agressivo_previsto}, **Gabarito:** {agressivo_gabarito}

    # """)

    perfis = ['Conservador', 'Moderado', 'Agressivo']
    previstos = [conservador_previsto, moderado_previsto, agressivo_previsto]
    gabaritos = [conservador_gabarito, moderado_gabarito, agressivo_gabarito]

    
    df_teste = pd.DataFrame(perfis, columns=['Perfis'])
    df_teste['Previsto'] = previstos
    df_teste['Gabarito'] = gabaritos
    df_teste = df_teste.set_index('Perfis')
    st.dataframe(df_teste)
    
    # 'Conservador Previsto', 'Conservador'
    # st.write(f'Conservador previsto: {conservador_previsto}, gabarito: {conservador_gabarito}\nModerado previsto: {moderado_previsto}, gabarito: {moderado_gabarito}\nAgressivo previsto: {agressivo_previsto}, gabarito: {agressivo_gabarito}\n\n Acurácia = {acuracia*100}%\n Precisão (Conservador, Moderado, Agressivo):\n {precisao_conservador*100}%, {precisao_moderado*100}%, {precisao_agressivo*100}%\n Recall (Conservador, Moderado, Agressivo):\n {recall_conservador*100}%, {recall_moderado*100}%, {recall_agressivo*100}%')

    

def funcao_media(valores):
    return sum(valores) / len(valores)
    


def filtrar_resultados(no_class):
    df = pd.DataFrame(no_class)
    df = df.rename(columns={0: "CPF", 1: "Perfil", 2: "Investimentos"})

    # Cria colunas para cada tipo de investimento
    df['Renda Fixa'] = df['Investimentos'].apply(lambda x: x[0])
    df['Multimercado'] = df['Investimentos'].apply(lambda x: x[1])
    df['Fundo Imobiliario'] = df['Investimentos'].apply(lambda x: x[2])
    df['Ações'] = df['Investimentos'].apply(lambda x: x[3])

    df['Média de Investimentos'] = df['Investimentos'].apply(lambda x: (x[0]+x[1]+x[2]+x[3])/4)

    df = df.drop(columns='Investimentos')

    df = df.sort_values(by=['Ações'])


    filtro_perfis = st.sidebar.multiselect('Por Perfil', df['Perfil'].unique())
    filtro_cpf = st.sidebar.multiselect('Por CPF', df['CPF'].unique())

    if (filtro_perfis == []) & (filtro_cpf == []):
        df = df
    
    elif (filtro_perfis != []) & (filtro_cpf == []):
        df = df.loc[df['Perfil'].isin(filtro_perfis), :]

    elif (filtro_perfis == []) & (filtro_cpf != []):
        df = df.loc[df['CPF'].isin(filtro_cpf), :]
    
    elif (filtro_perfis != []) & (filtro_cpf != []):
        df = df.loc[df['Perfil'].isin(filtro_perfis), :]
        df = df.loc[df['CPF'].isin(filtro_cpf), :]   

    resultados_busca = df['Perfil'].count()
    st.dataframe(df)
    st.write('Clientes Filtrados: ', f'<span color ="#57F688" style="font-size: 17px;">{resultados_busca}</span>', unsafe_allow_html=True)

    # Média de investimento por Perfil
    st.subheader("Média de Investimento por Perfil")    
    media_por_perfil = df.groupby('Perfil')['Média de Investimentos'].mean()
    media_por_perfil = pd.DataFrame(media_por_perfil)
    media_por_perfil['Média de Investimentos'] = media_por_perfil['Média de Investimentos'].map('{:,.2f}'.format)
    media_por_perfil = media_por_perfil.sort_values(by=['Média de Investimentos'])
    

    st.dataframe(media_por_perfil)



    



st.set_page_config(layout='wide')

st.cache(allow_output_mutation=True)

st.sidebar.title('KNN')

k = st.sidebar.number_input('Escolha um valor para "K"', min_value=1, max_value=90, value=1, step=1)

st.sidebar.title('Filtro de investidores')

st.write('Valor escolhido para K: ', f'<span color ="#57F688" style="font-size: 17px;">{k}</span>', unsafe_allow_html=True)






if __name__ == '__main__':    
    # Itera sobre os dados a serem classificados e os classifica
    for ponto in no_class:
        perfil = classificar_ponto(data, ponto[2], k)
        ponto[1] = perfil

    # Printa o resultado
    st.subheader("Classificação de Novos Investidores")
    filtrar_resultados(no_class)
    
    


    # Printa acurácia, precisão e recall do algorítimo
    st.subheader("Resultados da Matriz de Confusão")
    gerar_resultado(matriz_confusao, no_class)