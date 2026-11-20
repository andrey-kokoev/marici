"""Recover every coloring compatible with bare blue-five-set incidence, record 36.
Standard library. Variables are pair colors (positive = red); exhaustive DPLL.
The decoder reads only the 16 vertex IDs and the face half of the matrix.
"""
import json
from itertools import combinations as comb
from pathlib import Path
from collections import Counter

HOME=Path(__file__).resolve().parents[1];TARGET=(9,11)
def main():
    doc=json.loads((HOME/'results/ramsey_square_index_patch.json').read_text());n=doc['vertex_count'];V=range(n);P=list(comb(V,2));idx={e:j for j,e in enumerate(P,1)}
    F={tuple(i for i in V if int(r,16)>>i&1) for r in doc['rows_hex'][n:]};assert all(len(f)==5 for f in F)
    # Negative units fix witnessed blue pairs. Every absent five-set must contain red.
    covered={e for f in F for e in comb(f,2)};U=set(P)-covered;clauses=[frozenset([-idx[e]]) for e in sorted(covered)]
    forced={}
    for f in comb(V,5):
        if f not in F:
            es=set(comb(f,2))&U;clauses.append(frozenset(idx[e] for e in es));
            if len(es)==1:forced.setdefault(next(iter(es)),f)
    clauses += [frozenset(-idx[e] for e in comb(t,2)) for t in comb(V,3) if set(comb(t,2))<=U]
    # A blue six-set would require all six of its five-faces to occur.
    assert all(any(f not in F for f in comb(t,5)) for t in comb(V,6))
    def solve(cs,a):
        while True:
            rem=[c for c in cs if c.isdisjoint(a)];rem=[{x for x in c if -x not in a} for c in rem];
            if any(not c for c in rem):return
            units={next(iter(c)) for c in rem if len(c)==1}
            if not units:break
            if any(-x in units for x in units):return
            a=a|units;cs=rem
        if len(a)==len(P):yield a;return
        v=next(i for i in idx.values() if i not in a and -i not in a)
        for t in (v,-v):yield from solve(rem,a|{t})
    counts=Counter();models=[]
    for a in solve(clauses,set()):
        E={p for p,i in idx.items() if i in a};assert not any(set(comb(t,2))<=E for t in comb(V,3));assert {t for t in comb(V,5) if E.isdisjoint(comb(t,2))}==F
        counts['red' if TARGET in E else 'blue']+=1;models.append(sorted(E))
    x,y=TARGET;proof=next(({'middle':z,'forced_red_pairs':[(e,forced[e]) for e in [tuple(sorted((x,z))),tuple(sorted((z,y)))]]} for z in V if z not in TARGET and all(e in forced for e in [tuple(sorted((x,z))),tuple(sorted((z,y)))])),None)
    print(json.dumps(dict(faces=len(F),covered_pairs=len(covered),uncovered_pairs=len(U),forced_red_by_single_gap=len(forced),target=TARGET,blue_models=counts['blue'],red_models=counts['red'],short_proof=proof,models=models),indent=2))
if __name__=='__main__':main()
