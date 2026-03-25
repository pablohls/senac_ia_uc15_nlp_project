05/03/2026

    Criação do repositorio e intruções para os demais participantes.
    Testes na maquina do Marcelo.

06/03/2026

    Fiz pesquisas sobre documentos para utilizar como fonte dos dados, foquei em alguns dados publicos de sites como dados.gov.br, mas não encontrei nada de interessante ainda.
    Estou inclinado em buscar alguma documentação de alguma stack como o proprio python para usar como fonte.

09/03/2026

    Ajuda os demais participantes com questões técnicas.
    Alinhamento de escolhas do grupo para prosseguirmos com as tarefas.
    Criação do *data/pablo/gold_standard.md*.

11/03/2026

    Criação do pipeline base seguindo a documentação do Langchain.

12/03/2026

    Tentativas de aprimoramento do pipeline e melhoria dos resultados.

16/03/2026

    Configuração do setup na VM e inicio da analise do colab sugerido.

17/03/2026

    Criação do novo notebook "base_retrieve_rerank_notebook" usando de base colab fornecido em aula.

18/03/2026

    Avaliação dos notebooks de exemplo do professor e inicio da adaptação dos exemplos para meu caso..

19/03/2026

    Conclusão do novo notebook com base no codigo exemplo do professor e também adicionei uma etapa de validação usando Mean Reciprocal Rank (MRR) e Revocação (Recall).

23/03/2026

    Criação do docker e inicialização da configuração do doccano para utilização como "avaliador" do notebbok de trabalho.
    
24/03/2026

    Analise do "avaliador", realmente o mesmo não está muito bom, comecei a implementar um "is_relevant_llm", usando LLM as a judge, mas ainda precisa de ajustes. 