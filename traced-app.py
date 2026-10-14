from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [ "Explain LangSmith tracing in one sentence.", "Give three practical benefits of using LangSmith to debug an LLM application.", """Analyze the following scenario: an AI customer-support application uses an LLM to answer questions about refunds, shipping, and returns. Explain five possible causes of inaccurate answers, propose a debugging plan using traces, and recommend metrics for evaluating improvements. Present your answer with headings and concrete examples.""" ]

for i, prompt in enumerate(prompts, start=1): 
    response = llm.invoke(prompt) 
    print(f"\n--- Run {i} ---") 
    print(f"Prompt: {prompt}") 
    print(f"Answer:\n{response.content}")