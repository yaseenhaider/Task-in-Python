def dfs_medical_system(symptom_tree, current_symptom, diagnosis_path):
    if current_symptom in symptom_tree:
        for disease, symptoms in symptom_tree[current_symptom].items():

            # Record diagnosis
            diagnosis_path.append(disease)
            for symptom in symptoms:
                dfs_medical_system(symptom_tree, symptom, diagnosis_path)
    return diagnosis_path

symptom_tree = {
    'bukhar': {
        'Flu': ['Cough', 'Chills'],
        'Malaria': ['Chills', 'Fatigue'],
    },
    'khansi': {
        'Flu': [],
        'Cold': ['Sore Throat'],
    },
    'Chills': {
        'Flu': [],
        'Malaria': [],
    },
}

current_symptom = 'Fever'
diagnosis_path = []
diagnoses = dfs_medical_system(symptom_tree, current_symptom, diagnosis_path)
print("Possible diagnoses:", set(diagnoses))