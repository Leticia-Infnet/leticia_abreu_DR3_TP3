# Bem-vindo ao Assistente Bibliotecário, seu bibliotecário particular impulsionado por AI!

## Descrição do Problema:

Falta de uma aplicação que dê recomendações de livros e ao mesmo tempo seja capaz de prover informações disponíveis na internet sobre os livros.

## Solução:

Criar um agente inteligente usando o framework ReAct do LangChain, integrando a API do Google Books para gerar recomendações com base no input do usuário, e a API do GoogleSerper para fazer buscas no Google para informações mais detalhadas sobre os livros.

## Casos de Uso e Resultados Observados:

1. Apresentação do agente e serviços disponíveis:

![Apresentação do agente](https://github.com/user-attachments/assets/602395d0-e319-4dac-8204-9de1c1f80dc7)

2. Recomendação de livros por gênero:

![Recomendação de livros por gênero](https://github.com/user-attachments/assets/e840fced-4a35-4550-96fc-6680381a8949)

3. Memória conversacional:

![Memória conversacional](https://github.com/user-attachments/assets/6b402c5f-2489-4fd6-a91b-c9e9ffda4357)

4. Recomendações de livros por autor:

![Recomendações de livros por autor](https://github.com/user-attachments/assets/f5532f49-ffa7-47db-a8a3-cbb5b6f2cd56)

5. Recomendações de livros por gênero e subgênero:

![Recomendações de livros por gênero e subgênero](https://github.com/user-attachments/assets/8a59732b-decf-435a-899f-4a544ba3ae72)

6. Informações sobre um livro específico:

![Informações sobre um livro específico](https://github.com/user-attachments/assets/fd6f0ae7-c48e-4dc1-a73b-7e57c95998f1)

7. Informações específicas sobre um livro específico:

![Informações específicas sobre um livro específico](https://github.com/user-attachments/assets/cb381c7f-ca5a-46c5-a536-1ffa41d2897b)

## Como rodar a aplicação:

1. Clone este repositório para sua máquina:

```
git clone https://github.com/Leticia-Infnet/leticia_abreu_DR3_TP3.git
```

2. Na raíz do diretório, crie um arquivo .env com as seguintes chaves de API (substituindo por suas próprias chaves):

GOOGLE_API_KEY = SUA_API_KEY

SERPER_API_KEY = SUA_API_KEY

GOOGLE_BOOKS_API_KEY = SUA_API_KEY

3. Crie seu ambiente usando pip:

```
pip install -r requirements.txt
```

4. Da raíz do diretório, digite o seguinte comando:

```
python ./src/main.py
```

5. Pronto! O seu aplicativo estará rodando no próprio terminal.

## Como essa aplicação pode ajudar você:

1. Recomendações de Livros

    * Sugestões Personalizadas: Recomenda livros com base nos seus interesses, como gêneros favoritos ou obras similares às suas preferidas (ex.: "Me recomende livros parecidos com O Hobbit").
    
    * Foco em Temas: Encontre livros sobre tópicos específicos, como inteligência artificial ou segunda guerra mundial, utilizando a API do Google Books.

2. Informações sobre Autores e Livros

    * Detalhes sobre Autores: Obtenha informações sobre autores (ex.: "Quem foi Tolkien?" ou "Quais são as obras mais populares de J.K. Rowling?").
   
    * Visão Geral de Livros: Descubra informações sobre livros, seus personagens principais, temas e relevância histórica (ex.: "Sobre o que é Moby Dick?").

3. Companheiro Literário Interativo

    * Interação Conversacional: O sistema participa de diálogos para discutir literatura, ajudando a esclarecer dúvidas ou expandir tópicos de forma natural.
      
    * Respostas em Português: Apesar de toda lógica de pensamento do agente ser em inglês, sua resposta final é dada em português.

4. Acesso a Recursos da Internet

    * Busca em Tempo Real: Com a API do Google Serper, o aplicativo recupera recursos atualizados da internet para responder perguntas literárias, garantindo informações recentes.
      
    * Respostas Contextuais Aprimoradas: Os resultados da pesquisa são integrados às respostas, oferecendo um diálogo mais rico e fundamentado.

5. Customizável e Expansível

    * Funcionalidade Flexível: Permite adicionar mais ferramentas ou APIs para abordar outros domínios, como por exemplo artigos científicos.

## Limitações:

1. Inputs curtos: O agente apresenta falhas no raciocínio com inputs curtos e/ou com poucos detalhes. Se encontrar erros como Error: 'description' e Error: 'authors', reformule sua pergunta para ter mais detalhes na descrição ou autor específico. Exemplo:

![Reformulação da Pergunta](https://github.com/user-attachments/assets/4f6de2fe-8293-44ee-9fef-2a2d173e37c3)

2. Recomendações limitadas: A API do Google Books faz buscas, em sua maioria, em literatura estrangeira, mais especificamente em inglês. Se quiser recomendações de livros de autores brasileiros, especifique o gênero e, se possível o nome do autor.

## Sugestões de melhorias:

1. Adicionar busca para artigos científicos através de APIs como Google Scholar, PubMed e arXiv.

2. Procurar API's alternativas/ complementares à do Google Books para gerar melhores recomendações de literatura nacional.

3. Implementar uma interface Streamlit para experiência do usuário mais fácil e intuitiva. 
  
