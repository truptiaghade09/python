import difflib

# 🔹 Knowledge Base (rules with weights)
DISEASES = {
    "Flu": {
        "symptoms": {"fever", "cough", "fatigue"},
        "advice": "Take rest, drink fluids, consult a doctor."
    },
    "Dengue": {
        "symptoms": {"fever", "rash", "joint pain"},
        "advice": "Seek immediate medical attention."
    },
    "Migraine": {
        "symptoms": {"headache", "nausea", "sensitivity to light"},
        "advice": "Rest in a quiet, dark room."
    },
    "Heart Problem": {
        "symptoms": {"chest pain", "shortness of breath"},
        "advice": "Seek emergency care immediately!"
    },
    "COVID-19": {
        "symptoms": {"fever", "cough", "breathing difficulty"},
        "advice": "Get tested and isolate."
    }
}

# 🔹 Known symptoms (for typo correction)
ALL_SYMPTOMS = set()
for d in DISEASES.values():
    ALL_SYMPTOMS.update(d["symptoms"])


# 🔹 Normalize / correct symptoms
def normalize_symptom(symptom):
    symptom = symptom.strip().lower()
    match = difflib.get_close_matches(symptom, ALL_SYMPTOMS, n=1, cutoff=0.6)
    return match[0] if match else symptom


# 🔹 Diagnose with scoring
def diagnose(symptoms):
    symptoms = {normalize_symptom(s) for s in symptoms}

    results = []

    for disease, data in DISEASES.items():
        match_count = len(symptoms & data["symptoms"])
        total = len(data["symptoms"])
        score = match_count / total

        if match_count > 0:
            results.append((disease, score, data["advice"]))

    # Sort by highest match
    results.sort(key=lambda x: x[1], reverse=True)

    if not results:
        return "❗ Diagnosis unclear. Please consult a healthcare professional."

    # Build output
    output = "\n🩺 Possible Diagnoses:\n"
    for disease, score, advice in results:
        confidence = round(score * 100)
        output += f"\n➡ {disease} ({confidence}% match)\nAdvice: {advice}\n"

    return output


# 🔹 Main Program
def main():
    print("🏥 Smart Medical Expert System")
    print("Enter symptoms separated by commas (e.g., fever, cough)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter symptoms: ").lower()

        if user_input == "exit":
            print("Stay healthy! Goodbye 👋")
            break

        symptoms = [s.strip() for s in user_input.split(",") if s.strip()]
        result = diagnose(symptoms)

        print(result)


# Run
main()
