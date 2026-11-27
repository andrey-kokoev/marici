"""Does the induced spreadsheet half-turn select a verified core coloring?"""
from itertools import permutations,product,combinations
from collections import Counter
from pathlib import Path
import runpy,json
from ramsey_table_cube_differences import analyze
D=Path(__file__).resolve().parent

def run():
    r=analyze(9);assert len(r['leftover'])==11 and [len(c['new']) for c in r['pieces']]==[8,4,4,4]
    g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));C=g['cells'];E=frozenset((i,j) for i,j in combinations(range(26),2) if g['G'][i]>>j&1);assert len(E)==76
    def perm(p,b):return tuple(C.index(''.join('*' if s[j]=='*' else str(int(s[j])^k) for j,k in zip(p,b))) for s in C)
    def act(h,es):return frozenset(tuple(sorted((h[i],h[j]))) for i,j in es)
    orbit={act(perm(p,b),E) for p in permutations(range(3)) for b in product(range(2),repeat=3)};M=perm((2,1,0),(1,1,1));assert len(orbit)==8 and all(M[M[i]]==i for i in range(26));dist=Counter(len(es^act(M,es)) for es in orbit);out=dict(verified_orbit=len(orbit),fixed=sum(es==act(M,es) for es in orbit),symmetric_difference_histogram=dict(dist),intersection_edges=len(set.intersection(*(set(es) for es in orbit))),mirror_is_involution=True);print(out);dest=D.parent/'results/ramsey_excel_mirror_core.json';s=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
if __name__=='__main__':run()
