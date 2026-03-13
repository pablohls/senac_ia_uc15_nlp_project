(05/03/2026)
Realizei o clone do repositório criado pelo Pablo e configurei o ambiente virtual local (venv) e analisei os 4 arquivos trazidos pelo Marcelo para identificar o padrão de codificação e a viabilidade da extração de texto. 

06/03/2026
Apoiei a pesquisa de base de dados iniciada pelo Pablo. Sugeri a utilização de documentos oficiais de bibliotecas (NLTK) como fonte, dados que são textos técnicos e estruturados sem muitas imagens. Iniciei o rascunho script doa sanatização para limpar caracteres especiais que podem surgir na extração dos documentos.

09/03
Validei a saída do script da extração do Marcelo. Notei que alguns cabeçalhos de página estavam mesclados ao corpo do texto e iniciei a implementação de um filtro para ignorar esses ruídos. Comecei a estruturar as 10 perguntas padrão ouro, baseadas no texto extraído, focando em garantir que as respostas existam de forma explícita na base de dados 

10/03
Realizei o cruzamento das respostas extraídas via script como texto original do PDFpara garantir a fidelidade literal. O objetivo foi estabelecer o Ground Truth sólido, eliminando qualquer risco de alucinação do modelo durante as fases testes, assegurando que o sistema responda apenas o que está contido na base de dados.

11/03
Trabalhei na lógica da extruturação de metadados utilizando o framework LangChain, que foi eleito pelo grupo. Auxiliei na configuração dos documentos para cada fragmento de texto extraído carregue consigo a referência da página original do PDF. Com isso, temos transparência do pipeline RAG (Retrival-Argumented Generation), permitindo que, no futuro, o usuário possa verificar a fonte da resposta fornecida pela IA.

12/03
Realizei testes de Sanity Check comparando manualmente as saídas geradas pelo modelo de embeddings com o nosso Gold Standart. 