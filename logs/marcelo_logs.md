
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


30/03/2026

instalando e configurando o docker
instalando o sentence_transformers
consguindo configurar o container no docker
fazendo teste e avançando   

31/03/2026
docker pronto
sentence_transformers instado
conteiner configurado na maquina local
VM formataram e zerou tudo

01/04/2026
excutando e codigo de treino
estourou a memoria
estourou o espaço
um caos

06/04/2026
lendo biblioteca do VLLM
fazendo as configurações 
tentando rodar
tentando entender
montando no container do VM
montando docker na VM 
pois zeraram minha VM
tenho que instalar tudo de novo :(

07/04/2026
montando o codigo para teste
pesquisando como melhor fazer este codigo
depois de fazer o codigo saiu estes testes
com a convenção coletiva 2025-2026

===========================================================
ASSISTENTE DA CONVENCAO COLETIVA 2025-2026
Sindicato dos Comerciarios e Sindilojas-SP
============================================================

Pergunta: qual salario mimino 
Consultando convenção...

============================================================
Resposta (1.8s):
Com base nas cláusulas da Convenção Coletiva de Trabalho (CCT) dos Comerciários em São Paulo para os anos 2025/2026, não há informações específicas sobre salário mínimo algum no texto fornecido. Para responder à pergunta "Qual é o salário mínimo?" com precisão e coerência dentro do contexto da convenção:

"Não encontrado na convenção."
============================================================

Pergunta: qual o intervalo de descanço?
Consultando convenção...

============================================================
Resposta (2.3s):
O intervalo de descanso é estabelecido para funcionários que tenham trabalhado mais de seis horas por dia desde a entrada em vigor da Convenção Coletiva até o final do mês, e este período será concedido durante as férias anuais. O acordo não especifica diretamente um intervalo entre as horas de trabalho que constitui descanso legal; no entanto, a CLT (Consolidação das Leis em Matéria de Trabalho) estabelece como padrão para o Brasil 12h30min - sessões não excedendo um dia e meio semanal. Como essa normativa é obrigacional no país, pode-se considerar que as empresas devem seguir práticas similares ou mais generosas para garantir descanso suficiente aos seus funcionários conforme a cláusula (III) da CLT:
"Artigo 146 - O trabalhador tem direito ao dia e meia de férias anuais, fixadas pelo estado por lei. Aos fins desta parte, os empregadores são obrigados a dar-lhes o descanso legalmente devido." (cláusula III da CLT). 
No entanto, para uma resposta precisa e diretamente relacionada à Convenção Coletiva dos Comerciários de São Paulo 2025/2026 mencionada no documento original, não foi encontrado um intervalo específico de descanso citado. Portanto, a referência para o intervalo padrão do descanso mínimo conforme lei brasileira é apresentada como suporte contextual ao entendimento das regras laborais gerais no Brasil. 
Não encontrado na convenção
============================================================

Pergunta: qual o intervalo minimo de descanso que deverar ser assegurado ao empregado?
Consultando convenção...

============================================================
Resposta (1.1s):
A pergunta não é diretamente respondida pela Convenção Coletiva dos Comerciários de São Paulo 2025/2026. Não há nenhum intervalo mínimo específico mencionado para o descanso no texto fornecido da convenção coletiva, portanto a resposta é: "Não encontrada na convenção."
============================================================

09/04/2023

o codigo pronto.
lista dos teste que estou fazendo para aprimorar

============================================================
ASSISTENTE DE IA - GPU NVIDIA L40S
============================================================
Modelo: Phi-3-mini via Ollama
Idioma: Portugues
============================================================

[1] Pergunta: qual pais mais populoso
Processando na GPU...
------------------------------------------------------------
Resposta (0.4s):
O país com a maior população no mundo é o China, seguido pelo segundo Brasil. No entrante da lista seria apenas países como Estados Unidos e Índia que estão próximos aos números anteriores na tabela de países por população. No geral, essas são as cinco posições nas classificações globais atuais até o momento em 2023.
------------------------------------------------------------

[2] Pergunta: onde esta localizado o mar morto
Processando na GPU...
------------------------------------------------------------
Resposta (1.1s):
O Mar Morto está situado no Mediterrâneo Oriental, entre as ilhas de Sicília e Malta. É famoso por sua salinidade extrema e pela aparência verde-escura dos seus fundos devido à presença do mineral sódio natrocarbonato.

Em termos específicos: 
O Mar Morto está localizado na região mediterrânea entre as ilhas da Sicília, Itália e Malta. A latitude é aproximadamente 36 graus Norte e a longitude 14 de grau Leste. É um mar natural cujas águas são extremamente salinas, o que dificulta muito a vida das espécies aquáticas ali encontradas. Este fato lhe confere o título de "mar morto". As ilhas próximas incluem Malta e as ilhas Maltese mais orientais da Sicília italiana. O Mar Morto é um dos mares com salinidade extremamente elevada do mundo, tornando-se uma unicidade geográfica mundial.

Espera que esta resposta seja satisfatória para você!
------------------------------------------------------------

[3] Pergunta: qual o endereço da casa branca usa
Processando na GPU...
------------------------------------------------------------
Resposta (0.4s):
A Casa Branca está localizada no 1600 Pennsylvania Avenue NW, Washington D.C., Estados Unidos. Se você quiser visitar pela Internet ou por algum outro meio de comunicação digital e não puder verificar visualmente o endereço físico, essa informação deve servir para identificá-la corretamente.
------------------------------------------------------------
===========================================================
CONVENCAO COLETIVA 2025-2026
Respostas detalhadas baseadas no documento
============================================================

Pergunta: qual endereço do sindilojas
Consultando convenção...

============================================================
Resposta (1.0s):
A sede da Sindicato dos Comerciários de São Paulo está localizada na Rua Formosa, número 99 no Centro histórico de São Paulo. O Código de Regra do sindicato é o CEP 01048-100 - São Paulo – SP. Essa informação se encontra nos artigos da Convenção Coletiva dos Comerciários que detalham a sede e localização do sindicato em São Paulo, com base no registro específico nº 4.009/41. O endereço é declarado como um fator importante para o reconhecimento oficial da entidade nos documentos oficiais relacionados ao trabalho dos comerciários na região.
============================================================

Pergunta: qual o maior salario 
Consultando convenção...

============================================================
Resposta (6.7s):
De acordo com a Convenção Coletiva de Trabalho dos Comerciários de São Paulo para o período de 2025/2026, não há uma cláusula específica que declare um salário "maior" dentro do documento fornecido. Portanto, sem informações adicionais ou contextos relacionados a níveis salariais individuais e títulos no mercado de trabalho localizado em São Paulo, não é possível determinar qual seria o maior salário baseada apenas nas partes apresentadas da Convenção Coletiva. A questão do maior salário normalmente envolveria discussões sobre hierarquias profissionais e remunerações diferenciadas com base no cargo ocupado, experiência ou nível de complexidade das funções exercidas pelas pessoas dentro dos sindicatos mencionados na Convenção Coletiva. No entanto, esses detalhes não estão incluídos nos trechos disponíveis da convenção e a questão do "maior salário" não pode ser respondida com as informações fornecidas no documento acima. Portanto, precisaríamos de mais contexto ou uma referência adicional para responder essa pergunta especificamente sobre os termos estabelecidos nessa Convenção Coletiva em 2025/2026.

Pergunta: Quando ocorrerá a última reunião sindical antes da convenção?
Resposta detalhada baseada na convenção (NÃO ENCONTROU NATURALMENTE NA CONVENÇÃO COLETIVA DE TRABALHO FORNECIDA): 
- Não encontrou a informação sobre o horário da última reunião sindical antes do início da Convenção Coletiva de Trabalho no texto fornecido. Normalmente, as datas e horários das reuniões são estabelecidos em documentos separados ou anexos à Convenção Coletiva ou podem ser decididas pelo próprio sindicato antes do início da convenção semelhante ao que ocorre no texto acima. Para obter a informação específica sobre quando acontecerá a última reunião, seria necessário consultar esses documentos adicionais ou entrar em contato diretamente com os representantes do sindicato para descobrir as datas e horários da próxima reunião.

Pergunta: Qual o principal objetivo dessa convenção? 
Resposta detalhada baseada na convenção (NÃO FOI CITADA NO TEXTO PARA PROOCUPANTE): O texto fornecido não aborda explicitamente os principais objetivos da Convenção Coletiva de Trabalho dos Comerciários, como é o caso com as convenções do mercado salarial. No entanto, embora a maioria das convenções trabalhistas tenha por objetivo garantir um salário justo e razoável para os seus membros ao estabelecer termos gerais de conduta dos empregadores - incluindo o reajuste do salário fixo ou parte do salário misto, conforme mencionado na cláusula 1 da Convenção Coletiva citada:
- Cláusula 1 (NÃO FOI CITADA NO TEXTO PARA PROOCUPANTE): "Os salários fixos ou parte fixa dos salários mistos serão reajustados a partir de 01 de setembro do exercício atual, mediante aplicação do índice referente aos anteriores anos consecutivos com prazo para assegurar igualdade e justiça salarial."
Os objetivos adicionais da Convenção Coletiva normalmente incluem a defesa dos direitos trabalhistas, como convenções sobre jornadas de trabalho mínimas (não mencionada no texto), horas extras pagáveis e direito ao descanso remunerado. Esses objetivos geralmente são estruturados na Convenção Coletiva para proteger os interesses dos sindicalizados, mas não foram citadas explicitamente nos trechos fornecs que contêm informações sobre a reajuste salarial e as empresas abrangidas. Portanto, embora possamos inferir certos objetivos através da prática comum das Convenções Coletivas de Trabalho em geral (o estabelecimento do índice para o reajuste dos salários), essa informação específica sobre os principais objetivos dessa convenção não foi encontrada nos textos fornecidos. Para mais detalhes, seria necessário consultar a Convenção Coletiva completa ou entrar em contato diretamente com o sindicato para obter uma compreensão abrangente dos seus principais objetivos e termos acordados durante a convenção 2025/2026.
============================================================


13/04/2026

Tentando melhorar mais as respostas
![alt text](image.png)

as resposta estao melhorando 
os teste estao apresentando melhoras 
montei o grafica para melhorar visualmente
ficou top

14/04/2026
melhorando o resulado das respostas
dando muito trabalho 
no primeiro momento nao melhorou nada
estou pesquisando novas soluções 

15/04/2026
Meu VM deu problema

instalei no windows.

CARREGUEI O SCRIPT DO PROGRAMA 

CARREGOU O ARQVUIVO EM PDF
Convencao Coletiva dos Comerciarios de Sao Paulo
Periodo 2025/2026

CARREGOU TODAS AS 38 PAGINAS
Documento carregado - 38 paginas

ORGANIZOU O PDF 
Total de 342 paragrafos organizados

FIZ A PERGUNTA:
Digite sua pergunta:

Por qual prazo fica assegurado a manutenção do contrato de trabalho do empregado ao retornar em razão de afastamento por doença?

RESPOSTA DANDO DE ACORDO MOSTRANDO A PAGINA E PARAGRAFO DA RESPOSTA

Resposta encontrada
Localizacao: Pagina 21, Paragrafo 8

Resposta:

42 - GARANTIA DE EMPREGO APÓS RETORNO DO AUXÍLIO DOENÇA - Ao comerciário que retorna ao trabalho em razão de afastamento por doença, fica assegurada a manu tenção de seu contrato de trabalho pelo período de 30 (trinta) dias, a partir da alta previd enciária.

CRIANDO A API E TENTANDO FAZER FUNCIONAR
Utilizei o fastAPI
APOS MUITO TRABALHO 
ESTA FUNCIONANDO :)

Terminal 1  Rodando na porta 8000
Terminal 2  Rodando na porta 8501

Convenção Coletiva dos Comerciários de São Paulo
Período 2025/2026

Usando API para consultas


OK - API conectada com sucesso!

Digite sua pergunta:

Pergunta: vale transporte?

Encontrado(s) 3 resultado(s)

Resultado 1 - Página 24, Parágrafo 11

Resposta:

54 – VALE TRANSPORTE - Fica facultado às empresas o pagamento em dinheiro do vale transporte, em recibo próprio, sem que esse valor sofra qualquer incid ência de INSS, Clicksign 5ccd231f-5127-4696-84df-b576074c6eba

Resultado 2 - Página 25, Parágrafo 4

Resposta:

Parágrafo 2º - As empresas fornecerão o vale transporte sempre no mês anterior ao m ês a ser utilizado pelo empregado.

Resultado 3 - Página 25, Parágrafo 5

Resposta:

Parágrafo 3º - Nos termos do Decreto n.º 95.247/87, e baseado na Declaração emi tida pelo empregado acerca do uso do vale transporte, é direito da empresa fi scalizar sua correta utilização quanto ao deslocamento exclusivo residência-trabalho e vice-versa, sendo que a declaração falsa ou o uso indevido do vale transporte constituem f alta grave, passível das sanções legais, tais como advertência, suspensão ou demissão por justa causa.


┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Interface      │────▶│  API (FastAPI)  │────▶│  PDF            │
│  Streamlit      │◀────│  Porta 8000     │◀────│  Convenção      │
│  Porta 8501     │     │                 │     │                 │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
       Usuário                 Backend                 Dados


27/04/2026

baixei um gravação de reuniao de um hospital Sao Joao de Deus
e usei o whisper para transcrever.
e tive este resultado


meu_env) 202473505@senacgoon.local@VDI-UBU-GPU-05:~/audios_para_transcrever$ whisper "reuniao Sao Joao de Deus 15-04-2025.mp3" --language Portuguese --model small
[00:00.000 --> 00:05.000]  a Câmara Municipal de Divinópolis através da Comissão de Saúde recebe o diretor
[00:05.000 --> 00:10.000]  presidente do Complexo de Saúde, São João de Deus, para realizar a prestação de contas
[00:10.000 --> 00:15.000]  das verbas públicas recebidas pela instituição e dos seus novos projetos.
[00:15.000 --> 00:20.000]  Informo que essa prestação de contas está em transmissão ao vivo pela TV Câmara
[00:20.000 --> 00:27.000]  através do canal 13.1, através do canal do Legislativo Oficial no YouTube e também pelo Facebook.
[00:28.000 --> 00:33.000]  Destaco e registra a presença dos membros dos vereadores da 16ª Legislatura,
[00:33.000 --> 00:37.000]  membros da Comissão de Saúde. Convido o presidente da Comissão de Saúde,
[00:37.000 --> 00:42.000]  vereador doutor Delano Santiago, para saudar e dar início à reunião.
[00:44.000 --> 00:48.000]  Boa tarde ao representante do São João de Deus.
[00:48.000 --> 00:56.000]  Eu vou deixar marcado que seja a última vez que essa instituição que tem dinheiro público municipal
[00:56.000 --> 01:01.000]  vai fazer uma prestação de contas sem abordar a Comissão de Saúde.
[01:01.000 --> 01:07.000]  Nós não fomos convidados, ora alguma, a não ser no final essa comissão tem presidente
[01:07.000 --> 01:11.000]  e ele vai ter que ser respeitado e a casa também.
[01:11.000 --> 01:19.000]  Então, o presidente me passou a presidência para que eu tecnicamente conduzisse a reunião.
[01:19.000 --> 01:25.000]  É inaceitável não ser convidado como presidente da Comissão de Saúde,
[01:25.000 --> 01:32.000]  nominalmente, inclusive, para participar da reunião e colocarem no nome do presidente da casa.
[01:32.000 --> 01:39.000]  É inaceitável, mas nós vamos continuar o trabalho porque a gente precisa de prestar contas do dinheiro
[01:39.000 --> 01:43.000]  que usa para o povo de divinópolis e que sai dessa casa.
[01:43.000 --> 01:49.000]  Mas não façam novamente, porque nós abraçamos você sempre, de coração aberto,
[01:49.000 --> 01:56.000]  sempre pusemos a inteira disposição, nós precisamos de ser respeitados.
[01:56.000 --> 02:01.000]  E respeito-se da, é trocando de ambas as partes.
[02:01.000 --> 02:06.000]  Sempre que eu fui à instituição representando a casa e na presidência da Comissão de Saúde
[02:06.000 --> 02:12.000]  me declarei solícito, aberto e sempre disposto a ajudar.
[02:12.000 --> 02:17.000]  E esqueceram, como diz o filme, esqueceram de mim, mas eu estou aqui.
[02:17.000 --> 02:21.000]  Fáciles mais não, porque ficou feio para a instituição.
[02:21.000 --> 02:26.000]  Mas agora eu dou as boas-vindas, tenho um material aqui muito bacana,
[02:26.000 --> 02:28.000]  que é o que eu acho que eles vão apresentar aqui para nós,
[02:28.000 --> 02:34.000]  é uma pressação de conta do dinheiro municipal, porque é o que nos interessa
[02:34.000 --> 02:38.000]  aonde tem dinheiro emendas do município, a gente precisa saber
[02:38.000 --> 02:41.000]  porque o município vem atrás é de nós aqui.
[02:41.000 --> 02:45.000]  Então nós vamos dar andamento, a condução dos trabalhos.
[02:45.000 --> 02:49.000]  Quem vai apresentar diretamente, vai ser quem?
[02:49.000 --> 02:51.000]  Virgínia.
[02:51.000 --> 02:54.000]  Ah tá, o Dr. André, ele está convidado então,
[02:54.000 --> 02:57.000]  pode, por favor, Dr. André, como presidente da instituição,
[02:57.000 --> 02:59.000]  ele vai apresentar os dados para nós.
[02:59.000 --> 03:03.000]  Essa reunião, ela é aberta a todos os colegas, vereadores,
[03:03.000 --> 03:06.000]  em qualquer momento que qualquer umqueira questioná-lo,


apos varias tentativas 
consegui identigicar os falantes

[11:10] FALANTE 03:  Então, mesmo que a gente tenha 53 cidades de municípios,
[11:13] FALANTE 03:  a gente tem que ter interesse.
[11:15] FALANTE 03:  Porque a pressação de conta é nossa.
[11:17] FALANTE 03:  Então, nós queremos dinheiro de divinópolis.
[11:19] FALANTE 03:  Segundo, eu queria ter uma dúvida.
[11:21] FALANTE 03:  Me encontraram, que tem dinheiro ali
[11:23] FALANTE 03:  para comprar jaleco para o povo de hospital.
[11:26] FALANTE ?:  Vai me encontrar que o povo do hospital
[11:28] FALANTE 03:  vem debitado, o jaleco, quando é entregado, entrega.
[11:32] FALANTE 03:  Então...
[11:33] FALANTE ?:  Não entendi, vereador.
[11:35] FALANTE 02:  O pessoal do hospital tem dito...
[11:37] FALANTE 02:  Que eles tem pago o próprio uniforme
[11:39] FALANTE 03:  debitado em porcentagem no salário.
[11:42] FALANTE 02:  Não, debitado no salário não.
[11:44] FALANTE 02:  O que tem acontecido...
[11:46] FALANTE 02:  Não, isso realmente não acontece.
[11:48] FALANTE 03:  Então, eles não pagam o uniforme dele.
[11:51] FALANTE 02:  Eles pagam.
[11:52] FALANTE 03:  Ah, porque me encontraram, está vendo?
[11:54] FALANTE 02:  O que tem acontecido...
[11:55] FALANTE 03:  Mas ele não deu emenda para pagar.
[11:57] FALANTE 02:  Determinadas equipes querem ter
[11:59] FALANTE 02:  algum uniforme diferenciado.
[12:01] FALANTE 02:  Se vocês andarem no hospital lá hoje,
[12:03] FALANTE 02:  a gente vai encontrar uniforme rosa,
[12:06] FALANTE 02:  a gente vai encontrar uniforme roxo.
[12:08] FALANTE 02:  A instituição está uniformizando com a emenda do senhor,
[12:11] FALANTE ?:  mas a gente, infelizmente,
[12:13] FALANTE 02:  houve um problema com o anterior prestador,
[12:15] FALANTE 02:  tivemos que recomeçar todo o processo
[12:17] FALANTE 02:  e já está agora o atual,
[12:19] FALANTE 02:  era um daquilo, inclusive de Vinópolis,
[12:21] FALANTE 02:  porque a gente sempre toma cuidado
[12:23] FALANTE 02:  de favorecer as pessoas da região.
[12:25] FALANTE 02:  A gente tem muita essa consciência
[12:27] FALANTE 02:  que a gente falou do ESG ali.
[12:29] FALANTE 02:  E aí, inclui a governância,
[12:31] FALANTE 02:  inclui o social.
[12:33] FALANTE 02:  Então, buscamos empresas aqui,
[12:35] FALANTE 02:  fizemos a cotação,
[12:37] FALANTE 02:  e nenhuma empresa conseguiu entregar
[12:39] FALANTE 02:  o que é necessário.
[12:41] FALANTE ?:  Falava, senhor presidente.
[12:43] FALANTE ?:  Emitida.
[12:45] FALANTE 05:  Doutor André, Doutor Delano,
[12:47] FALANTE 05:  questionamento do Doutor Delano,
[12:49] FALANTE 05:  presidente dessa condição,
[12:51] FALANTE 05:  é muito importante porque justamente,
[12:53] FALANTE 05:  vou falar com toda humildade,
[12:55] FALANTE 05:  por não achar justo que o servidor
[12:57] FALANTE 05:  da instituição do complexo,
[12:59] FALANTE 05:  esse enorme complexo onjão de Deus,
[13:01] FALANTE ?:  que ganha hoje a receita,
[13:03] FALANTE 05:  e aí eu vou falar de emenda,
[13:05] FALANTE 05:  já passou nesses últimos quatro anos
[13:07] FALANTE 05:  mais de 50 milhões de reais
[13:09] FALANTE 05:  do posto do dinheiro público.
[13:11] FALANTE 05:  Isso é bom a gente falar isso aí.
[13:13] FALANTE 05:  Eu não acho justo
[13:15] FALANTE 05:  que o funcionário do hospital
[13:17] FALANTE 05:  São João de Deus custei o jaleque.
[13:19] FALANTE 05:  Por isso, mandei a emenda significativa.
[13:21] FALANTE 05:  Talvez, eu sou campeão de emenda ali,
[13:23] FALANTE 05:  se você olhar aqui, quadrinho ali,
[13:25] FALANTE 05:  eu só perco pra demir.
[13:27] FALANTE 05:  375 mil reais pra gente poder
[13:29] FALANTE 05:  custiar pra você servidor
[13:31] FALANTE 05:  do hospital São João de Deus.
[13:33] FALANTE 05:  Esse jaleque.
[13:35] FALANTE 05:  Não é possível que aí,
[13:37] FALANTE 05:  mesmo tendo a emenda,
[13:39] FALANTE 05:  o hospital São João de Deus não quere acreditar
[13:41] FALANTE 05:  que mesmo cobre do servidor
[13:43] FALANTE 05:  esse material,
[13:45] FALANTE 05:  que é importante, que é o uniforme,
[13:47] FALANTE 05:  é o jaleco.
[13:49] FALANTE 05:  O jaleco hoje é uma ferramenta de uniforme
[13:51] FALANTE 05:  pro profissional, seja médico,
[13:53] FALANTE 05:  seja também enfermeiro, técnico,
[13:55] FALANTE 05:  de enfermagem, farmacêutico,
[13:57] FALANTE 05:  toda equipe do hospital São João de Deus.
[13:59] FALANTE 05:  Então, a gente destinou essa emenda
[14:01] FALANTE 05:  justamente pra tirar,
[14:03] FALANTE 05:  pra aliviar pra esses trabalhadores
[14:05] FALANTE 05:  que pagam
[14:07] FALANTE 05:  até o ano passado,
[14:09] FALANTE 05:  e não é justo pagar esse ano,
[14:11] FALANTE 05:  esses uniformes aí.
[14:13] FALANTE 05:  Com certeza, vereador,
[14:15] FALANTE 02:  isso aí, como eu disse pra senhor,
[14:17] FALANTE 02:  pra essa casa,

28/04/2026

tentando melhorar a transcrição consegui estes resultados:

58:48] FALANTE 02:  Está no nome da ordem até hoje.
[58:50] FALANTE 03:  Ele doou para essa ordem que faria.
[58:52] FALANTE 03:  Mas enfim, a prestação, isso que nós estamos aqui, é para a prestação de contas.
[58:57] FALANTE 03:  Depois em outro momento a gente...
[58:58] FALANTE 03:  Eu até não entendi quem colocou essa pauta, porque nunca foi prestação de contas mesmo.
[59:02] FALANTE 03:  Foi colocado para nós que deveriam prestar contas do trimestre.
[59:05] FALANTE 03:  Não, né?
[59:06] FALANTE 03:  Mas foi.
[59:07] FALANTE 03:  Foi.
[59:08] FALANTE 03:  Na verdade, a gente...
[59:09] FALANTE 03:  É, painel de emendas e coisas, não...
[59:10] FALANTE 03:  A finalidade nessa, não.
[59:11] FALANTE 03:  O intuito era mais...
[59:12] FALANTE 03:  A finalidade foi em sofias muito bem.
[59:14] FALANTE 03:  Era mais?
[59:15] FALANTE 03:  Então o trabalho...
[59:16] FALANTE 03:  A gente tornou as emendas dos colegas e estiraram as dúvidas desde os que ficaram.
[59:22] FALANTE 03:  Para onde foi cada emenda, acho que ficou bacana.
[59:24] FALANTE 03:  E cada um incentivou, né?
[59:26] FALANTE 03:  Está o nome deles aqui.
[59:27] FALANTE 03:  Eu acho que esse é um incentivo.
[59:28] FALANTE 03:  Fulano, você direcionou e isso aqui é bacana.
[59:32] FALANTE 03:  Eu acho que tem que manter.
[59:33] FALANTE 03:  Isso foi bonito.
[59:34] FALANTE 03:  Porque ele viu o que ele fez e está em andamento, ficou claro.
[59:38] FALANTE 03:  Alguns de nós estamos aqui, uns estão até mortos.
[59:41] FALANTE 03:  Mas pelo menos sabe o final, onde foi a verba dele.
[59:45] FALANTE 03:  Eu agradeço muito.
[59:46] FALANTE 03:  Está encerrado a sessão.
[59:47] FALANTE 03:  Muito obrigado.
[59:48] FALANTE 02:  Obrigado.

============================================================
✅ Arquivo salvo: transcricao_com_falantes.txt
Total de segmentos transcritos: 1448
Total de falantes detectados: 6
============================================================

Coloquei para rodar no COLAB

consegui este resultado
============================================================
TRANSCRIÇÃO DA REUNIÃO COMPLETA
============================================================

Arquivo: reuniao Sao Joao de Deus 15-04-2025.mp3.mpeg
Tamanho: 27.5 MB
Este é o áudio completo da reunião de 60 minutos

Carregando modelo Whisper (small)...
Isso pode levar alguns segundos...

Transcrevendo áudio completo...
Isso pode levar vários minutos. Aguarde...
--------------------------------------------------
[00:00.000 --> 00:04.240]  a Câmara Municipal de Divinópolis, através da Comissão de Saúde,
[00:04.240 --> 00:08.080]  recebe o diretor presidente do Complexo de Saúde, São João de Deus,
[00:08.080 --> 00:13.120]  para realizar a prestação de contas das verbas públicas recebidas pela instituição
[00:13.120 --> 00:15.000]  e dos seus novos projetos.
[00:15.000 --> 00:20.240]  Informo que esta prestação de contas está em transmissão ao vivo pela TV Câmara
[00:20.240 --> 00:25.640]  através do canal 13.1, através do canal do Legislativo Oficial no YouTube
[00:25.640 --> 00:27.440]  e também pelo Facebook.
[00:27.440 --> 00:32.680]  Destaco e registro a presença dos membros dos vereadores da 16ª Legislatura,
[00:32.680 --> 00:34.600]  membros da Comissão de Saúde.
[00:34.600 --> 00:39.000]  Convido o presidente da Comissão de Saúde, vereador doutor Delano Santiago,
[00:39.000 --> 00:41.560]  para saudar e dar início à reunião.
[00:41.560 --> 00:47.200]  Boa tarde ao representante do São João de Deus.
[00:47.200 --> 00:53.720]  Eu vou deixar marcado que seja a última vez que essa instituição,

E as perguntas no colob  no Convenção do Sindilojas consegui isto:
============================================================
CONVENÇÃO SINDILOJAS 2025-2026
Digite sua pergunta
Digite 'sair' para encerrar
============================================================

Pergunta: endereço sindilojas

============================================================
RESPOSTA:
1. Paulo-Sindilojas- SP
2. e-mail: sindilojas@sindilojas-sp
3. Paulo-Sindilojas- SP
4. e-mail: sindilojas@sindilojas-sp
5. Paulo-Sindilojas- SP
============================================================

Pergunta: reajuste salario

============================================================
RESPOSTA:
1. dezembro de 2025, deverá aplicar o reajuste salarial já no mês de  competência dezembro, e
2. 2025, o reajuste e a tabela constante na
3. todos os fins o reajuste salarial integral previsto no caput desta cláusul a
4. instrumento,   as diferenças salariais em razão do reajuste salarial previst o no caput  desta
5. 1º de setembro de 2024 até 31 de agosto de 2025, terão os reajustes das  cláusulas anteriores
============================================================

cada vez que tenta melhorar piora mais :( 
