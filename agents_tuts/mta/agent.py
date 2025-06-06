from google.adk.agents import Agent, LlmAgent, SequentialAgent, ParallelAgent
from google.adk.models.lite_llm import LiteLlm
from textblob import TextBlob

MODEL = LiteLlm(model="groq/llama3-8b-8192")


def get_sentiment(text:str):
    sentiment = TextBlob(text).sentiment
    return sentiment.polarity


# root agent: must
# root_agent = Agent(
#     name="text_analysis_agent",
#     #  model="gemini-2.0-flash",
#     model=MODEL,
#     description=(
#         "Agent to analyse a given text"
#     ),
#     instruction=(
#         "You are a text analyst agent with the ability to analyse a given text and also to provide the sentiment of the text"
#     ),
#     tools=[get_sentiment],

# )


# writer_agent = LlmAgent(
#     name="WriterAgent",
#     model=MODEL,
#     instruction="""You are a Writer Agent. Write a comprehensive article about the given topic and also use information from the search results from the internet
#     """,
#     description="Write Comprehensive Article",
#     output_key="written_results"
# )

# summarizer_agent = LlmAgent(
#     model=MODEL,
#     name="SummarizeContent",
#     instruction="Summarize the webpage content found in 'written_results' ",
#     output_key="summary"
# )

# translator_agent = LlmAgent(
#     name="TranslatorAgent",
#     model=MODEL,
#     instruction="""You are an expert Translator Agent. Convert the given text and document from the "written results" to the german and french language
#     """,
#     description="Translate Comprehensive Article",
# )

# root_agent = SequentialAgent(
#     name="ResearchWriterPipelineAgent",
#     sub_agents=[writer_agent,summarizer_agent,translator_agent]
#     # The agents will run in the order provided: Writer -> Translator/Summarizer 
# )

# Parallel Agents
sentiment_agent = LlmAgent(
    name="SentimentAnalyzer",
    model=MODEL,
    description="Provide the sentiment of the text",
    instruction="Analyze the sentiment of the provided text.",
    output_key="sentiment"
)

keyword_agent = LlmAgent(
    name="KeywordExtractor",
    model=MODEL,
    description="Extract the relevant keywords from the text",
    instruction="Extract main keywords from the provided text.",
    output_key="keywords"
)

summarizer_agent = LlmAgent(
    name="Summarizer",
    model=MODEL,
    description="Summarize the given text",
    instruction="Create a concise summary of the text.",
    output_key="summary"
)

root_agent = ParallelAgent(
    name="ParallelTextAnalysisAgent",
    sub_agents=[sentiment_agent, keyword_agent, summarizer_agent],
    description="Runs multiple specialist agents in parallel to analyse a text" 
)


