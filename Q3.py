# Simple Medical Expert System using DFS

knowledge_base = {
    "Headache": {
        "Migraine": {
            "Cause": "Abnormal brain activity",
            "Symptoms": ["Headache", "Nausea", "Light sensitivity"],
            "Treatment": "Painkillers and rest"
        },
        "Sinusitis": {
            "Cause": "Sinus infection",
            "Symptoms": ["Headache", "Nasal congestion", "Facial pain"],
            "Treatment": "Steam inhalation and antibiotics"
        }
    },
    "Stomach Pain": {
        "Gastritis": {
            "Cause": "Stomach lining inflammation",
            "Symptoms": ["Stomach Pain", "Nausea", "Loss of appetite"],
            "Treatment": "Antacids and light diet"
        },
        "Food Poisoning": {
            "Cause": "Contaminated food",
            "Symptoms": ["Stomach Pain", "Vomiting", "Diarrhea"],
            "Treatment": "Hydration and rest"
        }
    }
}

# Depth-First Search to explore diseases in depth
def dfs(symptom):
    if symptom not in knowledge_base:
        print("No information for:", symptom)
        return
    for disease, info in knowledge_base[symptom].items():
        print(f"\nPossible Disease: {disease}")
        print("  Cause:", info["Cause"])
        print("  Symptoms:", ", ".join(info["Symptoms"]))
        print("  Treatment:", info["Treatment"])

# Example: Diagnose based on a symptom
dfs("Stomach Pain")
