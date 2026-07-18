from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
def generated_post(topic, length, tone, language):
    model = ChatGroq(model="openai/gpt-oss-120b")

    prompt = f'''
        Generate a LinkedIn post using the below information. No preamble.

        1) Topic: {topic}
        2) Length: {length}
        3) Tone: {tone}
        4) Language: {language}
        If Language is Hinglish then it means it is a mix of Hindi and English. 
        The script for the generated post should always be English.
        '''
    
    response = model.invoke(prompt)
    return response.content