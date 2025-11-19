# Simple European capitals quiz

questions = {
    "France": "paris",
    "Germany": "berlin",
    "Italy": "rome",
    "Spain": "madrid",
    "Portugal": "lisbon",
    "Belgium": "brussels",
    "Netherlands": "amsterdam",
    "Sweden": "stockholm",
    "Norway": "oslo",
    "Greece": "athens"
}

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")

    if answer.lower() == capital:
        print("Correct!")
    else:
        print("Wrong!")
