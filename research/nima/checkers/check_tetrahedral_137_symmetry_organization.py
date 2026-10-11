"""Compare reference-preserving symmetry policies for the 137-slot domain.
Combinatorial carrier hypotheses only; no electron identification or alpha fit.
"""
from itertools import product,permutations
from collections import Counter
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def parity(p):return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
def act(s,p,q):
    kind,a,b=s
    if kind=='state':return kind,p[a],q[b]
    return kind,tuple(p[i] for i in a),tuple(q[i] for i in b)
def census(slots,group):
    unseen=set(slots);orbits=[]
    while unseen:
        s=min(unseen);o={act(s,p,q) for p,q in group}
        assert o<=unseen;unseen-=o;orbits.append(o)
    return dict(group_order=len(group),orbit_count=len(orbits),
                orbit_size_histogram=dict(sorted(Counter(map(len,orbits)).items())),
                represented_slots=sum(map(len,orbits)))

def main():
    V=range(4);P=tuple(permutations(V));E=tuple((a,b) for a,b in product(V,repeat=2) if a!=b)
    q=(0,1);legs=tuple(e for e in E if e!=q)
    slots=tuple(('arrow',a,b) for a,b in product(legs,repeat=2))+tuple(('state',a,b) for a,b in product(V,repeat=2))
    stabilizer=tuple(p for p in P if (p[0],p[1])==q)
    oriented=tuple(p for p in stabilizer if parity(p)==1)
    assert len(E)==12 and len(legs)==11 and len(slots)==137
    independent=census(slots,tuple(product(stabilizer,repeat=2)))
    diagonal=census(slots,tuple((p,p) for p in stabilizer))
    proper=census(slots,tuple(product(oriented,repeat=2)))
    assert independent['orbit_size_histogram']=={1:5,2:14,4:26}
    assert diagonal['orbit_size_histogram']=={1:5,2:66}
    assert proper['orbit_size_histogram']=={1:137}
    assert {tuple(p[i] for i in q) for p in P}==set(E)
    # Other cardinalities or a different counted-domain policy change the count.
    size_family={n:(n*(n-1)-1)**2+n*n for n in range(2,7)}
    assert size_family[4]==137 and size_family[5]==386
    full=12**2+4**2;cross_typed=2*11*4
    assert full==160 and (11+4)**2==137+cross_typed==225
    result=dict(schema='marici.nima.tetrahedral-137-symmetry-organization.v1',status='pass',
        proposed_carrier='Four labelled states; physical electron identification remains unproved.',
        build_up={'states_per_factor':4,'directed_nonidentity_arrows_per_factor':12,
                  'retained_marked_reference_per_factor':1,'counted_arrow_legs_per_factor':11,
                  'arrow_pair_slots':121,'state_pair_slots':16,'total':137},
        independent_marked_relabellings=independent,
        common_marked_relabelling=diagonal,
        proper_tetrahedral_rotations_with_directed_marks=proper,
        count_by_state_cardinality=size_family,
        alternative_domains={'full_unexcluded_like_typed_pairs':full,
                             'with_cross_typed_pairs_if_separately_admitted':225},
        interpretation='137 exhausts the declared like-typed marked four-state comparison domain. It is not a maximum selected by symmetry alone, an orbit count, or a bound on electron states.',
        physical_gate='Specify the two comparison factors, their selected references, allowed relabellings and observable. Spin, statistics, U(1) charge and inverse fine-structure coupling are not derived by this census.')
    (ROOT/'results/tetrahedral-137-symmetry-organization.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
