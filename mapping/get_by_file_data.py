import pandas as pd
import csv

def create_csv_files(output_file_name, field_names, data):
    with open(output_file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

df = pd.read_csv('C:/Users/vedan/BDB-FUDAN/argNorm_benchmark/data/./manual_curation/aro_nan_subsitution.tsv', sep='\t')

data = []

i = 1

while i in range(df.shape[0]):
    if (i > 1 and df.loc[i, 'File'] != df.loc[i - 2, 'File']):
        create_csv_files(f'{df.loc[i - 2, 'File']}.manual_curation.csv', ['Original ID', 'ARO Replacement'], data)
        data = []

    data.append({
        'Original ID': df.loc[i, 'Original ID'],
        'ARO Replacement': df.loc[i, 'ARO:number']
    })

    print(df.loc[i, 'Original ID'], df.loc[i, 'ARO:number'])

    if (i == df.shape[0] - 1):
        create_csv_files(f'{df.loc[i - 2, 'File']}.manual_curation.csv', ['Original ID', 'ARO Replacement'], data)
        data = []

    i += 2

