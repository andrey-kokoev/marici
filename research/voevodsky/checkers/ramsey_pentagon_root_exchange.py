"""Marked reduced cells: paired by common midpoint, rooted inversion m -> -m. Seek both square roots exchanging the two blocks and preserving all four labeled decoder incidences. Do not use input dilation to filter candidates."""
from itertools import permutations
from pathlib import Path
import json,hashlib
from ramsey_pentagon_contrast_transport import L,orbits,neighborhood_tests

def main():
    labels=[(3*(a+b)%5,int((a-b)%5 not in (1,4))) for a,b in L]; lookup={x:i for i,x in enumerate(labels)};dec=[]
    for mask in range(1<<len(orbits)):
        E=set().union(*(o for i,o in enumerate(orbits) if mask>>i&1));S=neighborhood_tests(E)
        if S is not None:dec.append((E,S))
    assert len(dec)==4
    def move(E,p):return {tuple(sorted((p[a],p[b]))) for a,b in E}
    def cells(f):return tuple(lookup[f[m],1-t] for m,t in labels)
    roots=[f for f in permutations(range(5)) if all(f[f[m]]==(-m)%5 for m in range(5))];ok=[]
    for f in roots:
        p=cells(f)
        if not all(move(E,p)==E for E,S in dec):continue
        assert all({sum(1<<p[i] for i in range(10) if s>>i&1) for s in S}==S for E,S in dec);ok.append(f)
    # Compare only after constructing the candidate family.
    target=tuple(L.index(tuple(sorted((2*a%5,2*b%5)))) for a,b in L);matches=[f for f in ok if cells(f)==target];assert len(matches)==1 and len(ok)==2 and all(ok[0][ok[1][m]]==m for m in range(5))
    out=dict(midpoint_permutations=120,square_roots=roots,preserving_all_decoders=ok,input_matches=matches,inverse_pair=True,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_root_exchange.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
