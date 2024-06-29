from argnorm import lib
import pandas as pd

ARO = lib.get_aro_ontology()

[ab_molecule] = [t for t in ARO.terms() if t.name == 'antibiotic molecule']

nr_total_descendants = len(ab_molecule.subclasses(with_self=False).to_set())
direct_descendants = ab_molecule.subclasses(1, with_self=False).to_set()
assert any(t.name == 'antibiotic mixture' for t in direct_descendants)
nr_direct_descendants = len(direct_descendants)
nr_not_leaf = sum(bool(d.subclasses(with_self=False).to_set()) for d in ab_molecule.subclasses())

print(f'''# Antibiotic molecule descendant counts

Using ARO version bundled with argnorm {lib.__version__}
''')

print(pd.Series(
        {'Total descendants':   nr_total_descendants,
         'Direct descendants':  nr_direct_descendants,
         'Intermediate nodes':  nr_not_leaf - nr_direct_descendants,
         'Leaves':              nr_total_descendants - nr_not_leaf},
        name='Counts'
).to_frame().to_markdown())


print(f'# Other databases')
argannot = lib.get_aro_mapping_table('argannot').index\
        .str.split(')')\
        .str[0]\
        .str.replace('(','')\
        .str.lower() \
        .value_counts()
deeparg = lib.get_aro_mapping_table('deeparg').index\
                        .str.split('|')\
                        .str[3]\
                        .str.lower()\
                        .value_counts()
megares = lib.get_aro_mapping_table('megares').index\
                        .str.split('|')\
                        .str[2]\
                        .str.lower()\
                        .value_counts()
print(f'''## ARG-ANNOT

{argannot.to_markdown()}

Number of unique antibiotic classes: {argannot.shape[0]}


## DeepARG

{deeparg.to_markdown()}

Number of unique antibiotic classes: {deeparg.shape[0]}

## MEGARes

{megares.to_markdown()}

Number of unique antibiotic classes: {megares.shape[0]}
''')

