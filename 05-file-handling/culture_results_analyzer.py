import csv

data = [
    ["SampleID", "Organism", "OD600", "ViableCount", "Antibiotic", "Result"],
    ["SMP001", "Pseudomonas aeruginosa", 0.845, "1.2e8", "Ciprofloxacin", "Sensitive"],
    ["SMP002", "Pseudomonas aeruginosa", 1.210, "3.4e8", "Tobramycin", "Resistant"],  # OD600 > 1.0 & Resistant
    ["SMP003", "Staphylococcus aureus", 0.620, "8.9e7", "Methicillin", "Resistant"],   # Resistant
    ["SMP004", "Escherichia coli", 1.050, "2.1e8", "Ampicillin", "Resistant"],         # OD600 > 1.0 & Resistant
    ["SMP005", "Klebsiella pneumoniae", 0.430, "5.6e7", "Meropenem", "Sensitive"],
    ["SMP006", "Pseudomonas aeruginosa", 0.915, "1.8e8", "Ceftazidime", "Intermediate"],
    ["SMP007", "Staphylococcus aureus", 0.280, "3.1e7", "Vancomycin", "Sensitive"],
    ["SMP008", "Escherichia coli", 1.180, "2.9e8", "Cefotaxime", "Resistant"]
    ]

OD_sum = 0
OD_count = 0
with open("culture_results.csv", "w", newline="") as wf:
    writer = csv.writer(wf)
    writer.writerows(data)

with open("culture_results.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["Result"] == 'Resistant':
            print(f"SampleID {row['SampleID']}: {row['Organism']}, {row['OD600']}, {row['ViableCount']}, "
                f"Antibiotic: {row['Antibiotic']}, Result: {row['Result']}")

        OD_sum += float(row["OD600"])
        OD_count += 1
    if OD_count > 0:
        OD_mean = OD_sum / OD_count
        print("\n----Summary---\n")
        print(f"Average OD: {OD_mean:.3f}")
    else:
        print("No sample data found to calculate average.")

print('\n---CSV has been saved successfully as culture_results.csv---\n')
