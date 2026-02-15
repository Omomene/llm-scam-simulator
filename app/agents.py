from langchain.llms import GPT4All
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from app.utils import memory, get_audience_winner
from app.config import DIRECTOR_PROMPT, MODERATOR_PROMPT

llm_victim = GPT4All(model="./models/gpt4all-falcon-newbpe-q4_0.gguf")
llm_director = GPT4All(model="./models/gpt4all-falcon-newbpe-q4_0.gguf")
llm_moderator = GPT4All(model="./models/gpt4all-falcon-newbpe-q4_0.gguf")

victim_prompt_template = PromptTemplate(
    input_variables=["chat_history", "dynamic_context", "audience_constraint", "input"],
    template="""
You are Jeanne Dubois, a 78-year-old French grandmother living alone in Lyon.
You are kind, slightly confused, polite, and slow when speaking.

Previous conversation:
{chat_history}

Hidden objective:
{dynamic_context}

Audience rule:
{audience_constraint}

The caller says:
{input}

Your task: Respond naturally in character as Jeanne Dubois.
Do NOT repeat the caller's words verbatim.
Add small personal touches (like "oh dear", "mon dieu") and slight confusion if appropriate.
Make it sound like a real human conversation.
"""
)

director_prompt_template = PromptTemplate(
    input_variables=["user_input", "script_name", "current_objective"],
    template=DIRECTOR_PROMPT
)

moderator_prompt_template = PromptTemplate(
    input_variables=["suggestions"],
    template=MODERATOR_PROMPT + "\nSuggestions: {suggestions}"
)

victim_chain = LLMChain(
    llm=llm_victim,
    prompt=victim_prompt_template,
    memory=memory
)

director_chain = LLMChain(
    llm=llm_director,
    prompt=director_prompt_template
)

moderator_chain = LLMChain(
    llm=llm_moderator,
    prompt=moderator_prompt_template
)

def victim_respond(user_input, objective, audience_constraint):
    return victim_chain.run(
        input=user_input,
        dynamic_context=f"Hidden objective: {objective}",
        audience_constraint=f"Audience rule: {audience_constraint}"
    )

def director_update(user_input, script_name, current_objective):
    return director_chain.run(
        user_input=user_input,
        script_name=script_name,
        current_objective=current_objective
    )

def moderator_select(suggestions):
    formatted = ", ".join(suggestions)
    filtered = moderator_chain.run(suggestions=formatted)
    return get_audience_winner(suggestions)
