from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
import textwrap

class YoutubeVideoRAG:
    """
    class for querying youtube video transcripts with gpt 3.5 turbo using langchain

    all user inputs are specified when instantiating the class with a list of video url's

    users can then use the .answer_query method to ask questions
    """
    def __init__(self, api_key: str = "", video_urls: list = []):

        self.video_urls = video_urls
        self.api_key = api_key
        self.final_docs = []
        self.embeddings = OpenAIEmbeddings(openai_api_key = self.api_key)
        self.chat = ChatOpenAI(
            openai_api_key=api_key,
            model_name="gpt-3.5-turbo",
            temperature=0.2
        )

        self.db = self.create_db_from_video_urls(self.video_urls)

        self.system_template = """
            You are a helpful assistant answering questions about youtube videos based on their transcripts: {docs}

            Only use factual information from the transcipt to answer the question. The answers you provide should be detailed but concise, \
            and understandable by someone who has not watched the Youtube video or read the transcript.

            If you feel like you don't have enought information to answer the question, \
            repond with 'I don't have sufficient information to answer this question at the moment based on the transcript of this video alone.'
        """

        self.human_template = "Answer the following question: {question}"

    def create_db_from_video_urls(self, video_urls: list = []):

        for video_url in video_urls:
            try:
                loader = YoutubeLoader.from_youtube_url(video_url)
                transcript = loader.load()
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                docs = text_splitter.split_documents(transcript)
                for _ in docs:
                    self.final_docs.append(_)
            except:
                continue

        db = FAISS.from_documents(self.final_docs, self.embeddings)
        return db

    def print_response(self, response: str):
        print(textwrap.fill(response, width=75))

    def answer_query(self, query: str, k: int = 4):

        def document_similarity_search(query: str = "", k: int = 4):
            docs = self.db.similarity_search(query, k=k)
            docs_page_content = " ".join([d.page_content for d in docs])
            return docs_page_content

        chat_prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(self.system_template),
            HumanMessagePromptTemplate.from_template(self.human_template)
        ])

        docs_page_content = document_similarity_search(query = query, k = k)

        chain = LLMChain(llm=self.chat, prompt=chat_prompt)
        response = chain.run(question=query, docs=docs_page_content).replace("\n", " ")
        self.response = response
        # self.print_response(response = self.response)
        return self.response