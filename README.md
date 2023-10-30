# Classificação de Perfil de Investidores

Este é um projeto de classificação de perfil de investidores usando algoritmos de aprendizado de máquina. O projeto é implementado em Python e faz uso de bibliotecas como Pandas.

## Descrição

O objetivo deste projeto é classificar o perfil de investidores com base em informações sobre seus investimentos. Para isso, utilizamos um algoritmo de classificação que leva em consideração diversos atributos financeiros, respectivamente renda_fixa, multimercado, fundo_imobiliario, acoes.

Vale ressaltar que o objetivo deste projeto era implementar o algorítimo com o mínimo de bibliotecas/módulos possíveis, sendo assim, encontrará funções como a counter(), que poderia ser resolvida simplesmente importando-a "from collections import Counter".


## Dados

O projeto utiliza dois conjuntos de dados: `data` e `no_class`. O conjunto `data` contém dados de investidores com perfis conhecidos, enquanto o conjunto `no_class` contém investidores a serem classificados. Também temos uma matriz de confusão que será usada para avaliar o desempenho do modelo.

## Algoritmo de Classificação

O algoritmo de classificação utilizado neste projeto é baseado na distância euclidiana entre os investimentos de um investidor desconhecido e os investimentos de investidores com perfis conhecidos. O perfil do investidor desconhecido é determinado com base nos K investidores mais próximos em termos de distância euclidiana.

## Uso

Para usar o projeto, siga estas etapas:

1. Defina o valor de K.
2. Execute o código Python.
3. O código classificará os investidores do conjunto `no_class` com base nos investidores do conjunto `data`.
4. O resultado será apresentado em um DataFrame do Pandas com os perfis dos investidores no conjunto `no_class`.

## Resultado

O projeto fornece uma avaliação do desempenho do modelo, incluindo:

- Acurácia
- Precisão para cada perfil (Conservador, Moderado, Agressivo)
- Recall para cada perfil

A acurácia mostra a proporção de investidores classificados corretamente em relação ao total.

A precisão mede a proporção de investidores classificados como um perfil específico que realmente pertence a esse perfil.  
Exemplo alternativo: De todos os comentários classificados como positivos, qual percentual realmente é positivo?

O recall mede a proporção de investidores que pertencem a um perfil específico e foram corretamente classificados como tal.  
Exemplo alternativo: De todos os comentários que realmente são positivos, qual percentual é identificado corretamente pelo modelo?


## Meu Aprendizado

1 - Foi um projeto desafiador, especialmente por não poder usar determinadas bibliotecas, saí com uma visão de que posso fazer funções pra qualquer coisa.  
2 - Pude ver por dentro como é a estrutura de um KNN, fazer na mão foi um aprendizado e tanto.  
3 - O "por quê" é muito importante na definição dos parâmetros. A visão do negócio era proteger sempre os conservadores e correr atrás de bons números nesta categoria, que é o que foi de acordo com a proposta do negócio.

## Requisitos

- Python
- Pandas

## Contribuição

Sinta-se à vontade para contribuir com este projeto, abrir problemas ou enviar solicitações de pull.


---

[Luiz Antônio]
