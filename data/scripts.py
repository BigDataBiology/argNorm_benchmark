import pandas as pd
import os
import csv

def create_csv_files(output_file_name, field_names, data):
    with open(output_file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

def get_count_not_mapped():
    data = []
    curation_root = 'C:/Users/vedan/BDB-FUDAN/argNorm_benchmark/data/manual_curation/'
    manual_curation_files = os.listdir(curation_root)

    for file in manual_curation_files:
        manual_curation_file = pd.read_csv(curation_root + file, sep='\t')
        count = 0

        for i in range(manual_curation_file.shape[0]):
            if not manual_curation_file.loc[i, 'ARO Replacement'].isnumeric():
                count += 1
                print(manual_curation_file.loc[i, 'ARO Replacement'])

        data.append({
            'File': file,
            'Num Not Mapped': count,
        })

    create_csv_files('num_not_mapped.csv', ['File', 'Num Not Mapped'], data)

get_count_not_mapped()