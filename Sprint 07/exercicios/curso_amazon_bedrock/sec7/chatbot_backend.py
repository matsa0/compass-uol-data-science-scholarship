from langchain_aws import ChatBedrock
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain


def demo_chatbot(input_text):
    demo_llm = ChatBedrock (
        credentials_profile_name='default',
        model_id = 'anthropic.claude-3-haiku-20240307-v1:0',
        #inference_profile_arn='arn:aws:bedrock:us-east-1:537124933216:inference-profile/us.anthropic.claude-3-haiku-20240307-v1:0',
        model_kwargs = {
            "max_tokens": 300,
            "temperature": 0.1,
            "top_p": 0.9,
            "stop_sequences": ["\n\nHuman:"]
        }
    )
    return demo_llm.invoke(input_text)
    #return demo_llm

response = demo_chatbot(input_text="Hi, list the top 10 rock bands of all time")
print(response)

# cria uma função para um buffer de conversas. Dessa forma que a memória do contexto é trabalhada
def demo_memory():
    llm_data = demo_chatbot()
    memory = ConversationSummaryBufferMemory(llm=llm_data, max_token_limit=300)
    return memory

# conversas com o input_text atual + a memória
def demo_conversation(input_text, memory):
    llm_chain_data=demo_chatbot()
    llm_conversation = ConversationChain(llm=llm_chain_data, memory=memory, verbose=True)
    # resposta do chat
    chat_reply = llm_conversation.invoke(input_text)
    return chat_reply['response']