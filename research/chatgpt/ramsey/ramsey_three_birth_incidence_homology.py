"""Three-birth completion complexes and integral homology from oriented contacts.

Uses the contact-only pair-witness and triple-parity rules, not link optimization.
All 3,360 oriented three-birth assemblies, grouped into 56 symmetry orbits.
"""
from collections import Counter
from itertools import combinations
from ramsey_three_birth_oriented_contact_law import (
    orientations, orbit, pair_obstruction_witness, triple_parity_witness)


def complex_from_contacts(pairs):
    bad_pairs={frozenset((i,j)) for i,j in combinations(range(3),2)
               if pair_obstruction_witness(pairs,i,j) is not None}
    triple_forbidden=not bad_pairs and triple_parity_witness(pairs) is not None
    edges={frozenset((i,j)) for i,j in combinations(range(3),2)
           if frozenset((i,j)) not in bad_pairs}
    face=(len(edges)==3 and not triple_forbidden)
    # H_0 and H_1 via exact chain ranks for at most three vertices.
    components=3-len(edges) if len(edges)<=2 else 1
    assert components in (1,2)
    cycles=len(edges)-3+components
    b1=cycles-(1 if face else 0)
    return (len(edges),int(face),components-1,b1),bad_pairs,triple_forbidden


def main():
    remaining=set(orientations())
    classes=Counter();representatives={}
    while remaining:
        pairs=min(remaining)
        orb=orbit(pairs)
        assert orb<=remaining
        remaining-=orb
        topo,bad,tri=complex_from_contacts(pairs)
        classes[topo]+=len(orb)
        representatives.setdefault(topo,(pairs,bad,tri))
    assert classes==Counter({(3,1,0,0):1968,(2,0,0,0):624,
                            (3,0,0,1):576,(1,0,1,0):192}),classes
    assert not remaining
    print('All 3,360 oriented three-birth assemblies, grouped by contact symmetry:')
    for topo,n in sorted(classes.items(),key=lambda x:-x[1]):
        e,f,b0,b1=topo
        print(f'{n:4} cases: edges={e}, filled triangles={f}, '
              f'reduced Betti_0={b0}, Betti_1={b1}; example={representatives[topo]}')
    print('No full B-link computation or homology library required.')

if __name__=='__main__':main()
