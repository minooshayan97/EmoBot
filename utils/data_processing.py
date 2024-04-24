import pandas as pd
import tiktoken
from utils.embedding_utils import get_embedding

def open_doc_file(path):
  f = open(path, "r", encoding="utf8")
  return  f.readlines()


def createDataframe(path):
  document = open_doc_file(path)
  text = ' ' .join(document)

  # Split the text into chunks of 200 words
  # WE ACTUALLY USE 30?
  words = text.split()
  sections = [' '.join(words[i:i+30]) for i in range(0, len(words), 30)]

  # Convert paragraphs into a Pandas DataFrame
  df = pd.DataFrame({"sections": sections})

  # embedding model parameters
  embedding_model = "text-embedding-ada-002"
  embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
  max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191

  encoding = tiktoken.get_encoding("cl100k_base")

  df = df.rename(columns={'sections': 'text'})
  df=df[df.text.ne('')]
  # Counting the number of tokens for each text
  df["n_tokens"] = df.text.apply(lambda x: len(encoding.encode(str(x))))
  # filter too long text if any
  df = df[df.n_tokens <= max_tokens]

  df["embedding"] = df.text.apply(lambda x: get_embedding(x, embedding_model))

  return df
