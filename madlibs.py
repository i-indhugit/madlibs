print(" Welcome to Mad Libs: Secret Agent Adventure! ")
print("Fill in the blanks to create your own secret agent story.\n")
agent_name = input("Enter a secret agent name: ")
adjective1 = input("Enter an adjective: ")
gadget = input("Enter a fancy gadget: ")
vehicle = input("Enter a type of vehicle: ")
city = input("Enter the name of a city: ")
evil_name = input("Enter the name of an evil villain: ")
silly_action = input("Enter a silly action (e.g., 'juggling monkeys'): ")
adjective2 = input("Enter another adjective: ")
weapon = input("Enter a type of weapon: ")
story = f"""
Agent {agent_name}, the world’s most {adjective1} spy, received a mysterious message.
"Your mission, should you choose to accept it, involves the {gadget} prototype stolen in {city}."
Without hesitation, Agent {agent_name} jumped into their {vehicle} and raced off to stop the evil mastermind, {evil_name}.
But {evil_name} had a plan. Inside a hidden lair filled with lasers and {silly_action}, the villain waited, laughing like a {adjective2} hyena.
With only a {weapon} in hand, Agent {agent_name} kicked open the door and shouted, “Justice is served — shaken, not stirred!”
What happened next? Well… that’s classified.
"""
print("\n Your Secret Agent Story ")
print(story)
