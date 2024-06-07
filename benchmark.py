from argnorm.lib import get_aro_mapping_table
import argnorm.lib
import pandas as pd
import os

CURATION_ROOT = argnorm.lib._ROOT + '/data/manual_curation'
dbs = ['argannot', 'resfinder', 'resfinderfg', 'ncbi', 'deeparg', 'megares', 'sarg']

def count_num_args():
    output = {}

    for db in dbs:
        mapping_table = get_aro_mapping_table(db)
        output.update({db: mapping_table.shape[0]})

    return output

print(count_num_args())

def get_num_manual_curation():
    output = {}

    for file in os.listdir(CURATION_ROOT):
        df = pd.read_csv(os.path.join(CURATION_ROOT, file), sep='\t')
        output.update({file: df.shape[0]})

    return output

print(get_num_manual_curation())

def get_num_unmapped_args():
    output = {}

    for db in dbs:
        mapping_table = get_aro_mapping_table(db)
        count = mapping_table['ARO'].isnull().sum()

        output.update({db: count})

    return output

print(get_num_manual_curation())

def get_num_unique_args():
    output = {}

    for db in dbs:
        mapping_table = get_aro_mapping_table(db)
        count = len(set(mapping_table['ARO']))

        output.update({db: count})

    return output

print(get_num_unique_args())