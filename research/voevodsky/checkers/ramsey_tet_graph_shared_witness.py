"""A degree-preserving incidence switch. Install b0 last with one fixed marked red link."""
import json
from itertools import permutations,combinations
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'

def audit():
    E={tuple(p) for p in json.loads((D/'ramsey_37_root_glue.json').read_text())['witness']['plus_edges']};edge=lambda i,j:tuple(sorted((i,j)))
    # Work on the 17-site core; keep labels. Baselines are induced subgraphs of it or one switch away.
    for n in (17,16,15,14,13):
        V=tuple(range(5,5+n));g={p for p in E if set(p)<=set(V)};N=lambda G,i:{j for j in V if edge(i,j) in G};
        for w,v in combinations(V,2):
            A=N(g,w)-N(g,v)-{v};B=N(g,v)-N(g,w)-{w}
            for r0,b0 in permutations(sorted(A),2):
                for r1,b1 in permutations(sorted(B),2):
                    h=(g-{edge(w,b0),edge(v,b1)})|{edge(v,b0),edge(w,b1)}
                    if edge(r0,b0) in g or N(g,r0)&N(g,b0)!={w} or N(h,r0)&N(h,b0):continue
                    if any(N(h,i)&N(h,j) for i,j in h):continue
                    def independent(G,k):return next((s for s in combinations(V,k) if all(e not in G for e in combinations(s,2))),None)
                    if independent(h,7):continue
                    marked=h|{edge(r0,b0)};assert not independent(g,7) and not independent(marked,7) and all(not N(marked,i)&N(marked,j) for i,j in marked);assert all(len(N(g,i))==len(N(h,i)) for i in V)
                    # Orient as a single common predecessor: remove BOTH blue-side addresses first.
                    base=[e for e in sorted(g) if b0 not in e and b1 not in e];assert base==[e for e in sorted(h) if b0 not in e and b1 not in e];out=dict(vertices=V,common_core_red=base,matched_red=sorted(g),crossed_red=sorted(h),r=[r0,r1],b=[b0,b1],witnesses=[w,v],marked_link=edge(r0,b0),matched_triangle=[r0,w,b0],blue_six_after_mark=independent(marked,6));print({k:x for k,x in out.items() if not k.endswith('red')});(D/'ramsey_tet_graph_shared_witness.json').write_text(json.dumps(out,indent=2)+'\n');return
    raise AssertionError('no matched pair')
if __name__=='__main__':audit()
