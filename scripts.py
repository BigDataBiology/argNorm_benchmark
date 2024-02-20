from argnorm import normalizers
import pandas as pd
import os

MAPPING_ROOT = normalizers._ROOT + '/data'
MAPPING_FILES = filter(lambda file: 'ARO_mapping.tsv' in file, os.listdir(MAPPING_ROOT))
CURATION_ROOT = normalizers._ROOT + '/data/manual_curation'

def count_num_args():
    output = {}

    for file in MAPPING_FILES:
        df = pd.read_csv(os.path.join(MAPPING_ROOT, file), sep='\t')
        output.update({file : df.shape[0]})

    print(output)

def count_num_unique_aros():
    mapping_files = []
    for x in list(MAPPING_FILES):
        if 'ncbi' not in x and 'resfinder' not in x:
            mapping_files.append(x)

    #TODO: Clean this up
    zipped_ref = list(zip(mapping_files, os.listdir(CURATION_ROOT))) + [
                        ('abricate_ncbi_both_ARO_mapping.tsv', 'ncbi_manual_curation.tsv'),
                        ('amrfinderplus_ncbi_both_ARO_mapping.tsv', 'ncbi_manual_curation.tsv'),
                        ('abricate_resfinder_both_ARO_mapping.tsv', 'resfinder_manual_curation.tsv'),
                        ('resfinder_resfinder_both_ARO_mapping.tsv', 'resfinder_manual_curation.tsv')
                    ]

    output = {}
    for zips in zipped_ref:
        aro_list = []

        mapping = pd.read_csv(os.path.join(MAPPING_ROOT, zips[0]), sep='\t')
        curation = pd.read_csv(os.path.join(CURATION_ROOT, zips[1]), sep='\t')

        for aro in mapping['ARO']:
            aro_list.append(str(aro))

        for aro in curation['ARO Replacement']:
            aro_list.append(str(aro))

        while 'nan' in aro_list:
            aro_list.remove('nan')

        filtered_aro_list = []
        for aro in aro_list:
            if "{'ARO:" in aro:
                filtered_aro_list.append(aro)

            if aro.replace('.0', '').isnumeric():
                filtered_aro_list.append(aro)

        unique_aros = list(set(filtered_aro_list))

        output.update({zips[0]: len(unique_aros)})

    print(output)

def count_num_unmapped_args():
    output = {}

    for file in os.listdir(CURATION_ROOT):
        df = pd.read_csv(os.path.join(CURATION_ROOT, file), sep='\t')
        count = 0

        for i in range(df.shape[0]):
            aro = str(df.loc[i, 'ARO Replacement']).strip()
            if not aro.isnumeric() and not "{'ARO:" in aro:
                count += 1

        output.update({file : count})

    print(output)

def count_num_manually_curated_args():
    output = {}

    for file in os.listdir(CURATION_ROOT):
        df = pd.read_csv(os.path.join(CURATION_ROOT, file), sep='\t')
        output.update({file : df.shape[0]})

    print(output)

count_num_unique_aros()