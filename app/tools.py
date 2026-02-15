from langchain.agents import tool

@tool
def dog_bark():
    """Play dog barking sound when the scammer is being pushy."""
    return "[SOUND_EFFECT: DOG_BARKING]"

@tool
def doorbell():
    """Play doorbell sound when someone rings at the door."""
    return "[SOUND_EFFECT: DOORBELL]"

@tool
def coughing():
    """Simulate a coughing fit of Jeanne Dubois."""
    return "[SOUND_EFFECT: COUGHING]"

@tool
def tv_background():
    """Play background TV noise."""
    return "[SOUND_EFFECT: TV_BACKGROUND]"
