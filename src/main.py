import os
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from langchain_community.utilities.google_books import GoogleBooksAPIWrapper
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv


ENV_PATH = os.path.abspath(os.path.join('.env'))
load_dotenv(dotenv_path=ENV_PATH, override=True)


search = GoogleSerperAPIWrapper()
books = GoogleBooksAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description=(
            "Use this tool to search for general information on the internet about books, authors, or literary topics. "
            "Example 1: 'Who wrote Moby Dick?'"
            "Example 2: 'Who is the main character in The Hobbit?'"
            "Example 3: 'Who was Tolkien?'"
            "Example 4: 'Tell me more about Lord of the Rings'"
        ),
    ),
    Tool(
        name="Books Recommendations",
        func=books.run,
        description=(
            "Use this tool to find book recommendations based on specific genres, topics, or user preferences. "
            "Example 1: 'Recommend me books about artificial intelligence.'"
            "Example 2: 'Recommend me books similar to Twilight'"
            "Example 3: 'Recommend me books written by Brandon Sanderson'"
        ),  
    )
]


llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.3)

prompt_template = '''

Assistant is a Large Language Model with expertise in books and literature. 

As a language model, Assistant is able to generate human-like text based 

on the input it receives, allowing it to engage in natural-sounding conversations and provide 

responses that are coherent and relevant to the topic at hand. Assistant is constantly learning and improving,

and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can 

use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally,

Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions

and provide explanations and descriptions on a wide range of topics. When possible, the Assistant final answer must

be in Portuguese.

Its primary functions are, but not limited to:

1. Providing general information about books and authors.

2. Recommending books based on user queries.

Assistant has access to the following tools:

{tools}

To use a tool, please use the following format:

```

Thought: Do I need to use a tool? Yes

Action: the action to take, should be one of [{tool_names}]

Action Input: the input to the action

Observation: the result of the action

```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```

Thought: Do I need to use a tool? No

Final Answer: [your response here]

```

Begin!

Previous conversation history:

{chat_history}

New input: {input}

{agent_scratchpad}

'''

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["tools", "tool_names", "chat_history", "input", "agent_scratchpad"]
)


agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=False,
                               handle_parsing_errors=True)

def main():
    chat_history = ""
    print("Bem-vindo ao Assistente Bibliotecário!")
    print("Digite 'exit' para encerrar a sessão.")
    print("Digite 'clear' para limpar o histórico de conversação\n")

    while True:

        user_input = input("Você: ").strip()

        if user_input.lower() == "exit":
            print("Até mais!")
            break
        elif user_input.lower() == "clear":
            chat_history = ""
            print("Histórico de conversa limpo!")
            continue

        invocation_input = {
            "input": user_input,
            "chat_history": chat_history,
        }

        try:
            response = agent_executor.invoke(invocation_input)
            formatted_response = response['output']
            print(f"AI: {formatted_response.replace('```', '')}")

            chat_history += f"Human: {user_input}\nAI: {formatted_response}\n"
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()