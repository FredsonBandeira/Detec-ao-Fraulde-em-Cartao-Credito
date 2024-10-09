# Projeto de Detecção de Fraudes em Transações com Cartão de Crédito

## Introdução
Neste projeto, criei um sistema que pode detectar automaticamente transações fraudulentas em cartões de crédito. O objetivo é ajudar bancos e empresas a identificar possíveis fraudes e proteger seus clientes. Utilizei técnicas avançadas de aprendizado de máquina para ensinar o sistema a diferenciar transações normais de transações suspeitas.

## Como Funciona o Sistema
1. **O que é uma transação fraudulenta?**
   Fraude com cartão de crédito acontece quando alguém usa informações do cartão de outra pessoa para fazer compras ou transações sem autorização. O desafio é identificar essas transações rapidamente, para evitar maiores prejuízos.

2. **O que é aprendizado de máquina?**
   Aprendizado de máquina é uma forma de ensinar um computador a reconhecer padrões a partir de dados. Nesse projeto, usei informações de várias transações (como valor, horário, local, etc.) e ensinei o sistema a reconhecer quando algo parece suspeito ou fora do comum, indicando possível fraude.

3. **Como o sistema aprende?**
   - **Primeiro passo:** O sistema analisa um conjunto de transações antigas, onde já sabemos quais foram normais e quais foram fraudulentas.
   - **Segundo passo:** A partir desses exemplos, ele aprende a identificar características comuns em fraudes (por exemplo, transações de valor muito alto em um curto espaço de tempo).
   - **Terceiro passo:** Depois de aprender, o sistema passa a receber novas transações e faz previsões sobre quais são legítimas e quais podem ser fraudes.

4. **Quais dados são analisados?**
   O sistema analisa diversas informações de cada transação, como:
   - O valor da compra.
   - O horário da transação.
   - O local onde foi feita a compra.
   - E outras variáveis importantes que podem indicar um comportamento suspeito.

## Dataset
O dataset utilizado neste projeto foi obtido do Kaggle e contém informações sobre transações de cartões de crédito. Ele inclui uma variedade de características sobre cada transação, permitindo que o modelo aprenda a identificar padrões que podem indicar fraude.

### Descrição do Dataset
- **Total de Transações:** 113726
- **Características:** O dataset inclui as seguintes colunas:
  - **V1 a V28:** Variáveis de entrada que representam características extraídas das transações.
  - **Amount:** O valor da transação.
  - **Class:** A variável alvo, onde 0 indica uma transação legítima e 1 indica uma transação fraudulenta.

## Resultados do Projeto
O modelo criado foi capaz de identificar fraudes com alta precisão. Ou seja, ele conseguiu reconhecer a maioria das fraudes com poucos erros, o que significa mais segurança para os clientes e menos prejuízo para as empresas.

### Principais Métricas Avaliadas:
- **Acurácia:** Mede a porcentagem de previsões corretas. Meu modelo foi capaz de prever corretamente tanto transações legítimas quanto fraudulentas na maioria dos casos.
- **Precisão:** Mostra quantas das transações classificadas como fraudes realmente eram fraudulentas.
- **Revocação:** Mede a capacidade do modelo de identificar todas as fraudes presentes no conjunto de dados.
- **Matriz de Confusão:** Uma ferramenta usada para avaliar o desempenho do modelo, comparando as previsões com os resultados reais.

## Passo a Passo do Projeto
1. **Coleta e Preparação dos Dados**
   Carreguei um conjunto de dados com transações reais de cartões de crédito. Este conjunto de dados foi organizado para que pudéssemos diferenciar as transações normais das fraudulentas.

2. **Balanceamento dos Dados**
   Como as fraudes são eventos raros (apenas uma pequena parte das transações), utilizei uma técnica chamada SMOTE para equilibrar as classes, ou seja, aumentei a quantidade de exemplos de fraudes para que o modelo pudesse aprender melhor a identificá-las.

3. **Treinamento do Modelo**
   Usei uma técnica chamada Random Forest (Floresta Aleatória). Imagine que é como se tivéssemos várias "árvores de decisão", cada uma avaliando as transações de forma diferente. A resposta final é dada pela combinação dessas árvores, o que torna o modelo mais confiável.

4. **Testes e Avaliação**
   Após treinar o modelo, testei em novas transações para ver se ele conseguia prever corretamente quais eram fraudes e quais eram legítimas. Com isso, consegui medir o desempenho e ajustar o modelo para torná-lo mais preciso.

5. **Explicando o Modelo**
   Utilizei uma ferramenta chamada SHAP, que nos permite entender por que o modelo classificou uma transação como fraude ou não. Isso é importante para garantir que o sistema seja transparente e que possamos confiar em suas previsões.

## Ferramentas Utilizadas
- **Python:** Linguagem de programação que usei para criar o sistema.
- **Pandas e Numpy:** Para organizar e analisar os dados.
- **Scikit-Learn:** Biblioteca usada para construir e treinar o modelo de aprendizado de máquina.
- **Imbalanced-learn (SMOTE):** Para equilibrar a quantidade de transações normais e fraudulentas no conjunto de dados.
- **Matplotlib e Seaborn:** Para criar gráficos e ajudar a visualizar os dados.
- **SHAP:** Para explicar como o modelo toma suas decisões.

## Como Executar o Projeto
Aqui estão os passos para rodar o projeto, caso queira testar:

1. **Pré-requisitos:** Certifique-se de que tem o Python instalado no seu computador.




## Resultados

 Ao final, o sistema mostrará se as transações são legítimas ou suspeitas, e você verá algumas estatísticas sobre o desempenho do modelo.

## Conclusão

 Com este projeto, mostrei que é possível usar a tecnologia para detectar fraudes em tempo real, ajudando a prevenir perdas financeiras e aumentando a segurança das transações. O sistema pode ser ajustado para atender às necessidades específicas de diferentes empresas e pode ser expandido para analisar outras áreas além de cartões de crédito.
