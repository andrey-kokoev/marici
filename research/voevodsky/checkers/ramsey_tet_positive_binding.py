"""Scope test for a positive request at a neutral-bound A address.
One N address, two positive A witnesses, and seven B addresses. Only the
2-by-2 comparison square varies. All Boolean observations are terminal.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json

A=tuple(range(3)); B=tuple(range(7)); square=((0,0),(0,1),(1,0),(1,1))

def bplus(j):return lambda full:j in full[1]

def certificate(i):
    # Immutable reference i is shared; no new responder is constructed per link.
    def resolve(full):
        return any(bplus(j)(full) for a,j in full[0] if a==i)
    return resolve

def neutral_minus():return lambda full:False

def local_plus(i):return lambda full:i in full[2]

def tet(full,mode):
    def own_plus(i):return certificate(i) if i==0 and mode=='delegate' else local_plus(i)
    def address_plus(i):return certificate(i) if i==0 and mode=='address' else own_plus(i)
    # No colored A has a negative witness in this control; N always declines negation.
    reds=[address_plus(i)(full) for i in A];neg=[neutral_minus()(full) if i==0 else i in full[3] for i in A];blues=[bplus(j)(full) for j in B]
    v=(all(reds),all(blues),not any(neg),not any(blues));return v+(v[2] or v[3],)

def run():
    counts=Counter();examples=[]
    for mask in range(16):
        es=frozenset(e for h,e in enumerate(square) if mask>>h&1)
        for signs in range(128):
            full=(es,frozenset(j for j in B if signs>>j&1),frozenset((1,2)),frozenset());a=tet(full,'address');d=tet(full,'delegate');l=tet(full,'local');assert a==d and a[1:]==l[1:];counts['cases']+=1;counts['changed_all_A_plus']+=int(a!=l)
            if signs==1 and mask in (6,9):examples.append(dict(edges=[(i+1,j+1) for i,j in sorted(es)],B_positive=[1],address=a,delegate=d,local=l))
    assert len(examples)==2 and examples[0]['address']!=examples[1]['address'];out=dict(scope='Synthetic positive certificate: neutral-bound address can use positive B support across an incident comparison. No assertion of native source rule.',order=['all A+','all B+','no A-','no B+','OR'],counts=counts,degree_preserving_example=examples);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_tet_positive_binding.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
