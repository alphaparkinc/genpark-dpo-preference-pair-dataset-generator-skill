from client import DPOPreferenceGenerator

pair = DPOPreferenceGenerator.create_preference_pair(
    "Explain recursion",
    "Recursion is a programming technique where a function calls itself to solve a smaller instance of a problem.",
    "It loops.",
    1.0, 0.2
)
print("Pair valid:", pair["is_valid"])
print("Score margin:", pair["margin"])
print("JSONL line:\n" + DPOPreferenceGenerator.to_jsonl([pair]))
