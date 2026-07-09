#Build a nested dictionary representing a clinical microbiology report for 3 patients. Each patient should have: name, age, ward, and culture_results (itself a dictionary of organism → sensitivity: "sensitive" or "resistant").
#**********************************************
#(c)Samson Samuel Ikhayere, July 2026

patients = {
    "patient1":{
        "name":"Samson",
        "age": 27,
        "ward":"ICU",
        "culture_result": {
            "E. coli": "resistant",
            "S. aureus": "sensitive"
        }
    },
    "patient2":{
        "name":"John",
        "age": 30,
        "ward":"E&A",
        "culture_result":{
            "E. coli": "sensitive",
            "S. aureus": "sensitive"
        }
    },
    "patient3":{
        "name":"Victor",
        "age": 24,
        "ward":"Paediatric",
        "culture_result":{
            "E. coli": "resistant",
            "S. aureus": "resistant"
        }
    }
}


for patient_id, info in patients.items():
  for key, value in info.items():
    if key == "culture_result":
      for organism, sensitivity in value.items():
        if sensitivity == "resistant":
          print (f"Patient: {info['name']} | Age: {info['age']} | Ward: {info['ward']} | Resistant Organism: {organism}")
        #print (f"{patient_id}, {organism, info}")
    #print(key)
  #print(patient_id, info)
#print(patients)
