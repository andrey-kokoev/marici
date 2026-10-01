"""Apply the existing section-field constructor to the six-arrow seed."""
from math import prod
from check_section_endpoint_promotion import promote

seed=('AB','BC','CA','AD','DB','BA')
vertices=tuple('ABCD')
domains=(seed,vertices,vertices)
rows=[(e,e[0],e[1]) for e in seed]
origins=list(seed)
source_rows=None
print('rung 12: field sizes 6,4,4; rows 6')
for depth in range(3):
    old_rows=rows
    old_origins=origins
    domains,rows,history,fibers=promote(domains,rows,depth)
    origins=[old_origins[e] for _,_,e in history]
    assert set(origins)==set(seed)
    for new,(sigma,key,e) in zip(rows,history):
        assert old_rows[e][depth]==key
        assert all(new[j]==old_rows[e][j] for j in range(3) if j!=depth)
    print(f'rung {11-depth}: field sizes {tuple(map(len,domains))}; rows {len(rows)}; fiber sizes {list(map(len,fibers))}')
    if depth==1:
        source_rows=rows[:]
        source_origins=origins[:]
    if depth==2:
        coherent=[]
        for section in domains[2]:
            selected=[source_rows[e] for e in section]
            if len({r[1] for r in selected})==1:
                coherent.append(section)
        assert len(coherent)==1
        assert {source_origins[e] for e in coherent[0]}=={'AD','DB','BC','CA'}
        # Four evaluation rows under that target section, one per old target.
        selected_rows=[r for r in rows if r[2]==coherent[0]]
        assert len(selected_rows)==4
        assert len({r[1] for r in selected_rows})==1
        print('unique constant-source target section retains AD,DB,BC,CA; four evaluation rows')
assert tuple(map(len,domains))==(1,4,144)
assert len(rows)==576
# A fourth transition has one old label fiber of size 576: still manageable.
domains,rows,history,fibers=promote(domains,rows,0)
assert len(rows)==576 and tuple(map(len,domains))==(576,4,144)
assert sorted(e for _,_,e in history)==list(range(576))
print('rung 8: field sizes 576,4,144; rows 576; evaluation bijective')
# Count next step without materializing an enormous Cartesian product.
fiber_sizes=[sum(r[1]==a for r in rows) for a in domains[1]]
sections=prod(fiber_sizes)
assert all(fiber_sizes)
print(f'rung 7 (count only): source fibers {fiber_sizes}; sections {sections}; rows {4*sections}')
print('PASS: existing promotion rule applied; provenance retained and unique coherent routing lifted.')
print('No claim that the unique routing filter is a physical law or a complete promoted carrier.')
