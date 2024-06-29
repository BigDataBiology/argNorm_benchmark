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

