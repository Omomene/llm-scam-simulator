from gpt4all import GPT4All
from prompts import VICTIM_PROMPT_TEMPLATE
from tools import play_dog_bark, play_cough, play_doorbell

# Paths
MODEL_FOLDER = "models"
MODEL_NAME = "gpt4all-falcon-newbpe-q4_0"

victim_llm = GPT4All(model_name=MODEL_NAME, model_path=f"{MODEL_FOLDER}/{MODEL_NAME}")
director_llm = GPT4All(model_name=MODEL_NAME, model_path=f"{MODEL_FOLDER}/{MODEL_NAME}")

# Simple conversation memory
conversation_history = ""


def run_victim(user_input, objective, audience_event="None"):
    global conversation_history

    # Fill in the template properly
    full_prompt = VICTIM_PROMPT_TEMPLATE.format(
        objective=objective,
        audience_event=audience_event
    )

    # Add conversation context
    full_prompt += f"""

Conversation so far:
{conversation_history}

Scammer: {user_input}
Jeanne:
"""

    response = victim_llm.generate(full_prompt)

    # Update conversation history
    conversation_history += f"\nScammer: {user_input}"
    conversation_history += f"\nJeanne: {response}"

    return response.strip()



def run_director(user_input):
    director_prompt = f"""
You are the director of a scam simulation.
Based on the scammer's latest message, update the victim's internal objective.

Scammer: {user_input}

New objective:
"""

    response = director_llm.generate(director_prompt)
    return response.strip()
