
05/03/2026
procurei arquivos para o projeto
encontrei 4 arquivos para ser analisado com o grupo
conversamos sobre as estruturas

09/03/2026
abri um arquivo em PDF, transformei em texto e criou
e salvou no drive.
usando a biblioteca pypdf.
elaborei perguntas para projeto

10/03/2026
conclui as 10 perguntas.

11/03/2026
comecei a criar o script
configurei para instalar as bibliotecas
-pip install langchain-community pypdf
-import getpass
-import os
-from langchain_core.documents import Document
li os conceitos e começando entender os codigos

12/03/2026
- montando o projeto.
- organizado os comando.
- teste de buscas e respostas.
- feito algumas testes de consultas.

Primeira pesquisa_similaridade
# pergunta  " local sindilojas"

# resposta: 
Sindicato dos Comerciários de São Paulo 
Rua Formosa, 99 Centro 
CEP 01049-000 - São Paulo - SP 
Fone:. 2121-5900 
e-mail: 
atendimento@comerciarios.org.br  
Sindicato do Comércio Varejista e Lojista do Comércio de São 
Paulo-Sindilojas-SP 
Rua. Cel. Xavier de Toledo, 99 - Centro Histórico de São Paulo.

- estudando mais sobre o script
- tentando mudar e obter novos resultados
- mudando os comandos e tentando ter outros resultados

16/03/2026

- Testando a VM e testando
- começando a fazer os teste no trabalho
- começando a fazer o programa 
- instalando os programas
- VS Code
- Pytorch

17/03/2026

estou testando com o cross-encoders-marco-TinyBERT-L4

dando o resultado 

Cross-Encoder Relevance Scores:
tensor([[ 0.8305],
        [-0.9714],
        [-0.8356],
        [ 0.9199]])
 
 vou testar outros modelos 

 18/03/2026

 apos explicação do professor.
 tentando usar e modificar o codigo para meu projeto.

alguns resultados apos teste de codigo pronto sem usar o do professor.

 Input question: Qual é o índice de reajustamento previsto na cláusula  REAJUSTAMENTO?
Top-3 lexical search (BM25) hits
	5.728	O 13º salário deve ser calculado com base no salário reajustado integralmente, conforme previsto no caput da cláusula de    reajustamento, sem parcelamento ou compensações.
	2.524	As horas extras diárias serão remuneradas com o adicional legal de 60% (sessenta por cento), incidindo o percentual sobre o valor da hora normal
	2.450	Se as férias foram concedidas entre 1º/09/2025 e a assinatura da convenção, as diferenças salariais decorrentes do reajuste devem ser pagas na folha de janeiro/2026

        Top-3 Cross-Encoder Re-ranker hits
	6.261	A empresa deve pagar as diferenças salariais de setembro a novembro de 2025 em parcela única, integrando a base de cálculo das verbas rescisórias, e comunicar o empregado no prazo máximo de 10 dias da assinatura da convenção para recebimento.
	-0.590	Empresas enquadradas como MEI, ME ou EPP (até 20 empregados) que aderirem ao REPIS têm pisos diferenciados: R$ 1.580,00 para office-boy, R$ 1.977,00 para demais e garantia de comissionista de R$ 2.372,00, além de obrigatoriedade do Plano de Assistência (cláusula 60).
	-3.436	O 13º salário deve ser calculado com base no salário reajustado integralmente, conforme previsto no caput da cláusula de reajustamento, sem parcelamento ou compensações.
Pergunta de entrada: Quais as particularidades de remuneração para MEIs, MEs e EPPs? 
Top-3 lexical search (BM25) hits 
	3.233 A empresa deve pagar as diferenças salariais de setembro a novembro de 2025 em parcela única, integrando a base de cálculo das verbas rescisórias, e comunicar o empregado no prazo máximo de 10 dias da assinatura da convenção para recebimento. 
	2.937 Empresas enquadradas como MEI, ME ou EPP (até 20 empregados) que aderirem ao REPIS têm pisos diferenciados: R$ 1.580,00 para office-boy, R$ 1.977,00 para demais e garantia de comissionista de R$ 2.372,00, além de obrigatoriedade do Plano de Assistência (cláusula 60). 
	2.820 O empregado fará jus a um abono correspondente a 02 (dois) dias de sua remuneração mensal de outubro de 2025. 

	19/03/2026

	utilizei o cogido do professor.
	fiz alteraçõoes para ler o PDF

	pdf_file_path = '/content/drive/MyDrive/UC15/PDF/sindilojas_2025_2026.pdf'
    texts_from_pdf = []
    metadatas_from_pdf = []

	alterei a query
	 query = "Como é definida a Contribuição Assistencial Negocial Empresarial na cláusula 8??"

	obtive o resultado:
	e buscou dentro do pdf e retornou:
	Reranker score: 1.573921
----------------------------------------------------------------------------------------------------
Parágrafo 1º  – A discussão em acordos coletivos de trabalho de cláusulas q ue detenham 
característica intersindical, assim entendida a matéria objeto de neg ociação (pauta) entre as 
categorias laboral e empresarial, deverá ter, sob pena de nulidade d o que venha a ser 
avençado, obrigatoriamente, a participação da entidade empresarial. 

tambem criei na query.
new_query = "Empresas fornecem vale transporte e fiscalização de uso?"
new_results = retriever.invoke(new_query)
Rank: 1
Source: /content/drive/MyDrive/UC15/PDF/sindilojas_2025_2026.pdf_page_25_chunk_2
Reranker score: 5.360256
----------------------------------------------------------------------------------------------------
excluídos quaisquer adicionais ou vantagens. 
 
Parágrafo 2º -  As empresas fornecerão o vale transporte sempre no mês anterior ao m ês a 
ser utilizado pelo empregado. 
 
Parágrafo 3º - Nos termos do Decreto n.º 95.247/87, e baseado na Declaração emi tida pelo 
empregado acerca do uso do vale transporte, é direito da empresa fi scalizar sua correta 

mais uma query
new_query = "Qual é o índice de reajustamento previsto na cláusula  REAJUSTAMENTO?"
new_results = retriever.invoke(new_query)
Results for query: 'Qual é o índice de reajustamento previsto na cláusula  REAJUSTAMENTO?'
====================================================================================================
Rank: 1
Source: /content/drive/MyDrive/UC15/PDF/sindilojas_2025_2026.pdf_page_3_chunk_3
Reranker score: 4.603594
----------------------------------------------------------------------------------------------------
instrumento,   as diferenças salariais em razão do reajuste salarial previst o no caput desta 
cláusula deverão ser pagas na folha de pagamento de janeiro/2026. 
 
2 - EMPREGADOS ADMITIDOS APÓS 1º DE SETEMBRO/24 - Aos empregados admitidos a 
partir de 16 de setembro de 20 24 e até 15 de agosto de 20 25, o reajustamento será 
proporcional, conforme tabelas a seguir: 


20/03/2026

baixei um pdf com 124 paginas para teste

====================================================================================================
Rank: 1
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_41_chunk_4
Reranker score: 9.195508
----------------------------------------------------------------------------------------------------
Forense 17 6 6 
Cargo 6: Perito Criminal Federal – Área 7: 
Engenharia Civil 11 6 6 
Cargo 7: Perito Criminal Federal – Área 11: 
Engenharia Cartográfica 6 6 6 
Cargo 8: Perito Criminal Federal – Área 12: 
Medicina Legal 6 6 6 
Cargo 9: Perito Criminal Federal – Área 16: Física 
Forense 6 6 6

====================================================================================================
Rank: 2
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_29_chunk_4
Reranker score: 8.835571
----------------------------------------------------------------------------------------------------
Elétrica/Eletrônica 6 6 6 
Cargo 4: Perito Criminal Federal – Área 3: Informática Forense 69 11 69 
Cargo 5: Perito Criminal Federal – Área 5: Geologia Forense 17 6 17 
Cargo 6: Perito Criminal Federal – Área 7: Engenharia Civil 11 6 11 
Cargo 7: Perito Criminal Federal – Área 11: Engenharia Cartográfica 6 6 6 
Cargo 8: Perito Criminal Federal – Área 12: Medicina Legal 6 6 6 
Cargo 9: Perito Crimi

====================================================================================================
Rank: 3
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_9_chunk_2
Reranker score: 8.820333
----------------------------------------------------------------------------------------------------
Cargo 5: Perito Criminal Federal 
– Área 5: Geologia Forense 3 1 1 5 
Cargo 6: Perito Criminal Federal 
– Área 7: Engenharia Civil 2 * * 2 
Cargo 7: Perito Criminal Federal 
– Área 11: Engenharia 
Cartográfica 
1 * * 1 
Cargo 8: Perito Criminal Federal 
– Área 12: Medicina Legal 1 * * 1 
Cargo 9: Perito Criminal Federal 
– Área 16: Física Forense 1 * * 1 
Cargo 10: Perito Criminal 
Federal – Área

====================================================================================================
Rank: 4
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_47_chunk_2
Reranker score: 7.637212
----------------------------------------------------------------------------------------------------
Cargo 8: Perito Criminal Federal – Área 12: 
Medicina Legal 6 6 6 
Cargo 9: Perito Criminal Federal – Área 16: Física 
Forense 6 6 6 
Cargo 10: Perito Criminal Federal – Área 17: 
Engenharia de Minas 6 6 6 
Cargo 11: Perito Criminal Federal – Área 19: 
Genética Forense 6 6 6 
Cargo 12: Perito Criminal Federal – Área 20: 
Engenharia Ambiental 6 6 6 
Cargo 13: Perito Criminal Federal – Área 21: 
Ant

====================================================================================================
Rank: 5
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_41_chunk_3
Reranker score: 5.926595
----------------------------------------------------------------------------------------------------
aplicados os critérios de desempate de que tratam a alíneas “a” a “e” do subitem 18.10.1 deste edital; 
b) para os cargos de Perito Criminal Federal: os candidatos não eliminados na avaliação médica, e mais 
bem classificados, de acordo com a soma algébrica das notas obtidas na prova objetiva e na p rova 
discursiva, até os quantitativos estabelecidos a seguir, aplicados os critérios de desempate








Results for query: 'CARGO 7: PERITO CRIMINAL FEDERAL – ÁREA 11: ENGENHARIA CARTOGRÁFICA'
====================================================================================================
Rank: 1
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_41_chunk_4
Reranker score: 9.150510
----------------------------------------------------------------------------------------------------
Forense 17 6 6 
Cargo 6: Perito Criminal Federal – Área 7: 
Engenharia Civil 11 6 6 
Cargo 7: Perito Criminal Federal – Área 11: 
Engenharia Cartográfica 6 6 6 
Cargo 8: Perito Criminal Federal – Área 12: 
Medicina Legal 6 6 6 
Cargo 9: Perito Criminal Federal – Área 16: Física 
Forense 6 6 6

====================================================================================================
Rank: 2
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_9_chunk_2
Reranker score: 9.128271
----------------------------------------------------------------------------------------------------
Cargo 5: Perito Criminal Federal 
– Área 5: Geologia Forense 3 1 1 5 
Cargo 6: Perito Criminal Federal 
– Área 7: Engenharia Civil 2 * * 2 
Cargo 7: Perito Criminal Federal 
– Área 11: Engenharia 
Cartográfica 
1 * * 1 
Cargo 8: Perito Criminal Federal 
– Área 12: Medicina Legal 1 * * 1 
Cargo 9: Perito Criminal Federal 
– Área 16: Física Forense 1 * * 1 
Cargo 10: Perito Criminal 
Federal – Área

====================================================================================================
Rank: 3
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_29_chunk_4
Reranker score: 8.982639
----------------------------------------------------------------------------------------------------
Elétrica/Eletrônica 6 6 6 
Cargo 4: Perito Criminal Federal – Área 3: Informática Forense 69 11 69 
Cargo 5: Perito Criminal Federal – Área 5: Geologia Forense 17 6 17 
Cargo 6: Perito Criminal Federal – Área 7: Engenharia Civil 11 6 11 
Cargo 7: Perito Criminal Federal – Área 11: Engenharia Cartográfica 6 6 6 
Cargo 8: Perito Criminal Federal – Área 12: Medicina Legal 6 6 6 
Cargo 9: Perito Crimi

====================================================================================================
Rank: 4
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_47_chunk_2
Reranker score: 8.136305
----------------------------------------------------------------------------------------------------
Cargo 8: Perito Criminal Federal – Área 12: 
Medicina Legal 6 6 6 
Cargo 9: Perito Criminal Federal – Área 16: Física 
Forense 6 6 6 
Cargo 10: Perito Criminal Federal – Área 17: 
Engenharia de Minas 6 6 6 
Cargo 11: Perito Criminal Federal – Área 19: 
Genética Forense 6 6 6 
Cargo 12: Perito Criminal Federal – Área 20: 
Engenharia Ambiental 6 6 6 
Cargo 13: Perito Criminal Federal – Área 21: 
Ant

====================================================================================================
Rank: 5
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_42_chunk_1
Reranker score: 7.667668
----------------------------------------------------------------------------------------------------
Cargo 10: Perito Criminal Federal – Área 17: 
Engenharia de Minas 6 6 6 
Cargo 11: Perito Criminal Federal – Área 19: 
Genética Forense 6 6 6 
Cargo 12: Perito Criminal Federal – Área 20: 
Engenharia Ambiental 6 6 6 
Cargo 13: Perito Criminal Federal – Área 21: 
Antropologia Forense 6 6 6 
Cargo 14: Perito Criminal Federal – Área 22: Meio 
Ambiente 48 6 17 
14.1.1 Caso o número de candidatos que t




Results for query: 'CARGO 9: PERITO CRIMINAL FEDERAL – ÁREA 16: FÍSICA FORENSE'
====================================================================================================
Rank: 1
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_47_chunk_2
Reranker score: 9.275080
----------------------------------------------------------------------------------------------------
Cargo 8: Perito Criminal Federal – Área 12: 
Medicina Legal 6 6 6 
Cargo 9: Perito Criminal Federal – Área 16: Física 
Forense 6 6 6 
Cargo 10: Perito Criminal Federal – Área 17: 
Engenharia de Minas 6 6 6 
Cargo 11: Perito Criminal Federal – Área 19: 
Genética Forense 6 6 6 
Cargo 12: Perito Criminal Federal – Área 20: 
Engenharia Ambiental 6 6 6 
Cargo 13: Perito Criminal Federal – Área 21: 
Ant

====================================================================================================
Rank: 2
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_5_chunk_2
Reranker score: 9.036112
----------------------------------------------------------------------------------------------------
CARGO 9: PERITO CRIMINAL FEDERAL – ÁREA 16: FÍSICA FORENSE 
REQUISITO: diploma, devidamente registrado, de conclusão de curso de graduação de nível superior em 
Física, fornecido por instituição de ensino superior reconhecida pelo MEC. 
DESCRIÇÃO SUMÁRIA DAS ATIVIDADES: realizar exames periciais em locais de infração pe nal; realizar 
exames em instrumentos utilizados, ou presumivelmente utilizado

====================================================================================================
Rank: 3
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_9_chunk_2
Reranker score: 8.703821
----------------------------------------------------------------------------------------------------
Cargo 5: Perito Criminal Federal 
– Área 5: Geologia Forense 3 1 1 5 
Cargo 6: Perito Criminal Federal 
– Área 7: Engenharia Civil 2 * * 2 
Cargo 7: Perito Criminal Federal 
– Área 11: Engenharia 
Cartográfica 
1 * * 1 
Cargo 8: Perito Criminal Federal 
– Área 12: Medicina Legal 1 * * 1 
Cargo 9: Perito Criminal Federal 
– Área 16: Física Forense 1 * * 1 
Cargo 10: Perito Criminal 
Federal – Área

====================================================================================================
Rank: 4
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_41_chunk_4
Reranker score: 8.653947
----------------------------------------------------------------------------------------------------
Forense 17 6 6 
Cargo 6: Perito Criminal Federal – Área 7: 
Engenharia Civil 11 6 6 
Cargo 7: Perito Criminal Federal – Área 11: 
Engenharia Cartográfica 6 6 6 
Cargo 8: Perito Criminal Federal – Área 12: 
Medicina Legal 6 6 6 
Cargo 9: Perito Criminal Federal – Área 16: Física 
Forense 6 6 6

====================================================================================================
Rank: 5
Source: /content/drive/MyDrive/UC15/PDF/Ed_1_PF_25_Abertura.pdf_page_29_chunk_4
Reranker score: 8.653397
----------------------------------------------------------------------------------------------------
Elétrica/Eletrônica 6 6 6 
Cargo 4: Perito Criminal Federal – Área 3: Informática Forense 69 11 69 
Cargo 5: Perito Criminal Federal – Área 5: Geologia Forense 17 6 17 
Cargo 6: Perito Criminal Federal – Área 7: Engenharia Civil 11 6 11 
Cargo 7: Perito Criminal Federal – Área 11: Engenharia Cartográfica 6 6 6 
Cargo 8: Perito Criminal Federal – Área 12: Medicina Legal 6 6 6 
Cargo 9: Perito Crimi

23/03/2026

preparando o codigo 
DOCCANO
preparando o 
DOCKER
tudo baixado e configurando  
agora e so lutar
docker container start doccano
127.0.0.1:8000
Deu certo  :)


24/03/2026

apos configurar 
fazer 4 perguntas
apos fazer rotulos
obtive estes resultados
"label":[[2473,2761,"reajustamento previsto na cláusula  REAJUSTAMENTO"],[2904,3084,"1º da cláusula 1 sobre salários superiores a R$ 11.000,00"],[9867,9956,"salário de admissão para empregados em geral em empresas com mais de 20 empregados"],[10361,10411,"salário de admissão para empregados em geral em empresas com mais de 20 empregados"],[34045,34359,"garantia de emprego ao futuro aposentado prevista na cláusula 21"]],"Comments":[]}


24/03/2026
Em sala de aula
inclui mais 4 perguntas totalizando 8 perguntas
refazendo os rotulos
saiu isto 
"label":[[2473,2761,"reajustamento previsto na cláusula  REAJUSTAMENTO"],[2904,3084,"1º da cláusula 1 sobre salários superiores a R$ 11.000,00"],[9867,9956,"salário de admissão para empregados em geral em empresas com mais de 20 empregados"],[10361,10411,"salário de admissão para empregados em geral em empresas com mais de 20 empregados"],[10793,11259,"O que estabelece a cláusula 5 – GARANTIA DO COMISSIONISTA quanto ao valor mínimo"],[12103,12568,"o que determina a cláusula 7 sobre a contribuição assistencial dos empregados"],[17328,17669,"O que estabelece a cláusula 5 – GARANTIA DO COMISSIONISTA quanto ao valor mínimo"],[25542,25827,"Como é calculada a remuneração do repouso semanal dos comissionistas"],[34045,34359,"garantia de emprego ao futuro aposentado prevista na cláusula 21"]],"Comments":[]}


depois de fazer com novas metrica: 

Primeiro estágio: busca os 20 pedaços mais similares
Segundo estágio: reordena os 20 com modelo mais preciso, mantém os 5 melhores
Mostra os resultados com página e score

resultados:
Rank: 1
Source: /content/drive/MyDrive/UC15/PDF/sindilojas_2025_2026.pdf_page_3_chunk_3
Reranker score: 4.979145
----------------------------------------------------------------------------------------------------
instrumento,   as diferenças salariais em razão do reajuste salarial previst o no caput desta 
cláusula deverão ser pagas na folha de pagamento de janeiro/2026. 
 
2 - EMPREGADOS ADMITIDOS APÓS 1º DE SETEMBRO/24 - Aos empregados admitidos a 
partir de 16 de setembro de 20 24 e até 15 de agosto de 20 25, o reajustamento será 
proporcional, conforme tabelas a seguir: 

Rank: 2
Source: /content/drive/MyDrive/UC15/PDF/sindilojas_2025_2026.pdf_page_7_chunk_4
Reranker score: 3.101576
----------------------------------------------------------------------------------------------------
Capital acima de R$ 150.000,00 R$ 2.710,00 
CONTRIBUIÇÃO MÍNIMA 
Filial sem capital social destacado (vide parágrafo 6º)  R$ 295,00 
Empresas sem empregados (vide parágrafo 7º) R$ 295,00 
 
Parágrafo 1º  - O recolhimento deverá ser feito até o dia 07 de outubro de 2025 , em 
qualquer agência bancária ou pela internet, em impresso próprio, que será envi ado pelos 
Correios

ETC...

25/03/2026

procurando nas bibliotecas como fazer funcionar
tentando utilizar o codigo de saiu deu este resultado:

--- Resultados para: O que diz a cláusula 7 sobre contribuição assistencial? ---

1. Página 17 - Score: 2.445
   prevista no “caput” desta cláusula. 
 
Parágrafo 2º - Ficam desobrigadas do cumprimento desta cláusula as empresas 
obrigadas à cumprir o disposto na cláusula 60 que trata do Auxí lio Plano de Assistência 
e Cuidado Pessoal, e aquelas que promoverem a adesão à referida  cláusula de forma 
espontânea...

2. Página 17 - Score: 2.445
   prevista no “caput” desta cláusula. 
 
Parágrafo 2º - Ficam desobrigadas do cumprimento desta cláusula as empresas 
obrigadas à cumprir o disposto na cláusula 60 que trata do Auxí lio Plano de Assistência 
e Cuidado Pessoal, e aquelas que promoverem a adesão à referida  cláusula de forma 
espontânea...

3. Página 17 - Score: 2.445
   prevista no “caput” desta cláusula. 
 
Parágrafo 2º - Ficam desobrigadas do cumprimento desta cláusula as empresas 
obrigadas à cumprir o disposto na cláusula 60 que trata do Auxí lio Plano de Assistência 
e Cuidado Pessoal, e aquelas que promoverem a adesão à referida  cláusula de forma 
espontânea...

4. Página 17 - Score: 2.445
   prevista no “caput” desta cláusula. 

   26/03/2026

   tentando fazer o codigo 
   lendo bibliotecas
   resultado de muitos erros


   27/03/2026

   baixe o codigo do professor 
   estou fazendo mudanças e adquações
   muito sofrimento
   muitas falhas
   mas lutando

   