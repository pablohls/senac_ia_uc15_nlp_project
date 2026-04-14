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

25/03/2026

    Continuei a implementação de um LLM as a Judge, sem sucesso devido a limitações. Refiz o meu gold standard para testar a acuracia, mas aparentemente não tive muita melhoria.

26/03/2026

    Fiz um novo notebook, usando LLM, para testar algumas abordagens. Consegui implementar por completo, mas ainda falta avaliar melhor os resultados.

27/03/2026

    Aparentemente o novo notebook, usando LLM, apresentou bons resultados finais, mas ainda estou explorando o funcionamento do mesmo para entender melhor sobre o codigo.

30/03/2026

    Criação do "fine_tunning_test.ipynb" com base no tutorial de finetuning passado em aula.

02/04/2026

    Ajuste no ambiente local da VM para executar os notebooks das aulas do dia 30/03 e do dia 01/04, pendente apenas o download dos arquivos e qualquer eventual falha que possa ocorrer nos codigos, mas aparentemente está quase tudo certo.

06/04/2026

    Criação da imagem e configuração para rodar um modelo de LLM localmente usando Ollama.

07/04/2026

    Conclusão da configuração do Ollama local, criação da implementação da chamada nos notebooks para que a LLM possa avaliar as respostas.

08/04/2026

    Crição de um novo notebook simples, para testar a integração com a LLM rodando localmente As a judge.

09/04/2026

    Inicio da criação de uma interface para "prompting" com o RAG.

13/04/2026

    Ajustes em busca de melhorar os resultados, como alterar a forma de gerar os chunks e outros ajustes. Auxiliar os demais membros com dificuldades tecnicas.