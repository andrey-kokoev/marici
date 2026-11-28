"""Corrected tet: bounds over unspecified neutral positive continuations, not source frequencies."""
from itertools import product
from collections import Counter
from pathlib import Path
import json


def request(i,sign):
    def on(binding,positive_refs):
        return (i in positive_refs if sign=='+' else False) if binding[i]=='N' else binding[i]==sign
    return on


def read(binding,positive_refs):
    def responses(ids,sign):return [request(i,sign)(binding,positive_refs) for i in ids]
    a=not any(responses(range(3),'-'));b=all(responses(range(3),'+'));c=not any(responses(range(3,10),'+'));d=all(responses(range(3,10),'-'));return (a,b,c,d,a or c)


def audit():
    fixed=Counter();pair=Counter();cases=0;R=set(range(3));B=set(range(3,10));ex={}
    for binding in product('+-N',repeat=10):
        # Four extremal continuations suffice: all-red-positive and no-blue-positive
        # are monotone on disjoint reference domains. No temporal order assumed.
        readings={read(binding,mask) for mask in (set(),R,B,R|B)};vary=tuple(len({v[i] for v in readings})==2 for i in range(5));cases+=1
        assert not vary[0] and not vary[3];pair[vary[1],vary[2]]+=1
        for i in range(5):fixed[i]+=not vary[i]
    for r,b in [('++N','-------'),('+++','------N'),('++N','------N'),('++-','------N')]:
        binding=r+b;ex[r+' / '+b]=sorted(read(binding,m) for m in (set(),R,B,R|B));ex[r+' / '+b]=sorted(set(ex[r+' / '+b]))
    out=dict(scope='Exclusive signed controls at non-neutral addresses; N minus always false. Positive continuations may resolve differently at distinct immutable references. Conditional bounds, not a law supplied by Excel.',order=['no red-','all red+','no blue+','all blue-','OR'],bindings=cases,fixed_counts=[fixed[i] for i in range(5)],ambiguous_positive_vertices={str(k):v for k,v in pair.items()},examples=ex);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_tet_partial_source.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
