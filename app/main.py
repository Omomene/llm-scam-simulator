# app/main.py
from agents import run_victim, run_director

current_objective = "Be polite but slow."
audience_event = "None"

print("=== Scam Simulator Started ===")
print("Type 'exit' to stop.\n")

while True:
    scammer_input = input("Scammer: ")

    if scammer_input.lower() == "exit":
        break

    # Director updates objective based on scammer input
    current_objective = run_director(scammer_input)

    # Victim generates response
    victim_response = run_victim(scammer_input, current_objective, audience_event)

    # Print victim response
    print(f"\nJeanne: {victim_response}\n")

print("Simulation ended.")
