from argnorm.lib import get_aro_mapping_table
from argnorm.lib import DATABASES
import pandas as pd

dbs = DATABASES
mapping_tables = []
groot_added = False

for db in DATABASES:
    if 'groot' in db:
        if not groot_added:
            mapping_tables.append(get_aro_mapping_table(db))
            groot_added = True
    else:
        mapping_tables.append(get_aro_mapping_table(db))

combined_mapping_table = pd.concat(mapping_tables)

tot_num_genes = len(combined_mapping_table['Cut_Off'])
print(f'Total number of genes: {tot_num_genes}\n')

value_counts = combined_mapping_table['Cut_Off'].value_counts().to_dict()
print(f'Total # of perfect hits: {value_counts["Perfect"]}. This is {value_counts["Perfect"] / tot_num_genes * 100}% of the total hits.')
print(f'Total # of strict hits: {value_counts["Strict"]}. This is {value_counts["Strict"] / tot_num_genes * 100}% of the total hits.')
print(f'Total # of loose hits: {value_counts["Loose"]}. This is {value_counts["Loose"] / tot_num_genes * 100}% of the total hits.') 
print(f'Total # of manual curation genes: {value_counts["Manual"]}. This is {value_counts["Manual"] / tot_num_genes * 100}% of the total hits.')
