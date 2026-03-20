
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
