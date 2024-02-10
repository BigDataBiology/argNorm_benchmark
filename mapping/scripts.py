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
    not_mapped_list = []
    curation_root = 'C:/Users/vedan/BDB-FUDAN/argNorm_benchmark/data/manual_curation/'
    manual_curation_files = os.listdir(curation_root)

    for file in manual_curation_files:
        manual_curation_file = pd.read_csv(curation_root + file, sep='\t')
        count = 0

        for i in range(manual_curation_file.shape[0]):
            if not manual_curation_file.loc[i, 'ARO Replacement'].isnumeric() and not "{'ARO:" in manual_curation_file.loc[i, 'ARO Replacement']:
                count += 1
                not_mapped_list.append([manual_curation_file.loc[i, 'ARO Replacement'], i])
                print(manual_curation_file.loc[i, 'ARO Replacement'])

        for i in not_mapped_list:
            data.append({
                'File': file,
                'Mapping': i[0],
                'Position': i[1]
            })

        # data.append({
        #     'File': file,
        #     'Num Not Mapped': count,
        # })

    create_csv_files('not_mapped_mapping.csv', ['File', 'Mapping', 'Position'], data)

get_count_not_mapped()