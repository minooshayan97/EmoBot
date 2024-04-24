from utils.embedding_utils import embedding_model, cosine_similarity, get_embedding
from utils.categories import categories

def provide_context(df, prompt):

  prompt_embedding = get_embedding(prompt, embedding_model)
  df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, prompt_embedding))
  results = (df.sort_values("similarity", ascending=False))

  llmchain_information = results["text"][:3]

  return llmchain_information


def generate_augQuery(df, inpt, topic):
  context = provide_context(df, inpt)
  source_knowledge = " ".join(context)

  augmented_prompt = f"""We are talking about {categories[int(topic)]}. Use contexts to provide relevant support to the students' problem. Respond empathetically.
    Contexts:{source_knowledge}
    Query: {inpt}"""

  return augmented_prompt


def new_subject(df, inpt, topic, nxt):
  context = provide_context(df, inpt)
  source_knowledge = " ".join(context)

  augmented_prompt = f"""We were talking about {categories[int(topic)]}. Use contexts to provide relevant support to the students' problem in 1-2 sentences. Respond empathetically shortly. Conclude this topic and ask the next question in one final sentence: how often have they been bothered by the following over the past 2 weeks {categories[int(nxt)]}?
    Contexts:{source_knowledge}
    Query: {inpt}"""

  return augmented_prompt


def endConversation(inpt):
  augmented_prompt = f"""Time to finish this conversation because you have asked all the questions. Conclude the conversation in 1-2 sentences. Respond empathetically. In your final sentence, tell them to contact you again anytime in the future.
    Query: {inpt}"""

  return augmented_prompt