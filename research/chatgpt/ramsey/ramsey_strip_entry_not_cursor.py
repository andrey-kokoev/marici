"""Recover entry from the unbased alternating boundary cycle, then test whether mark=column B and seam=entry can give a distinguishing endpoint mark reader. No pole/color output used."""
from pathlib import Path
import json
from itertools import combinations,permutations
from ramsey_seed_affine_witness import P,T,r,adj
D=Path(__file__).parent;edges=list(combinations(range(4),2));rows=('BRNN','BNRN')
def run():
    cycle=[0,16]
    while True:
        j,=adj[cycle[-1]]-{cycle[-2]}
        if j==cycle[0]:break
        cycle.append(j)
    assert len(set(cycle))==len(adj)==10
    checks=0;firsts=set();recovered=set()
    for seq in [cycle,cycle[::-1]]:
        for h in range(10):
            view=seq[h:]+seq[:h];fixed=[v for v in view if r[v]==v];entry,=[v for v in fixed if v<15];exit,=[v for v in fixed if v>=15];assert (entry,exit)==(0,29)
            a,b=(set(edges[i]) for i in P[entry]);apex,=a&b;assert all(w[apex]=='B' for w in rows);firsts.add(view[0]);recovered.add(apex);checks+=1
    # Exit is all three opposite edge pairs. Stabilizer of the literal exit partition and even of ONE selected exit duad: no distinguished column.
    st=[]
    for selected in (None,P[7],P[4]):
        ps=[]
        for p in permutations(range(4)):
            act=lambda d:tuple(sorted(edges.index(tuple(sorted((p[a],p[b])))) for a,b in (edges[i] for i in d)))
            if set(map(act,T[29-15]))!=set(T[29-15]) or selected is not None and act(selected)!=selected:continue
            ps.append(p)
        st.append(dict(size=len(ps),possible_images_of_column_1=sorted({p[0]+1 for p in ps})))
    return dict(cycle=cycle,displays=checks,distinct_first_visits=len(firsts),fixed_entry=0,fixed_exit=29,common_entry_column_one_based=sorted(v+1 for v in recovered),exit_stabilizers=st)
if __name__=='__main__':
    res=run();print(res);(D/'ramsey_strip_entry_not_cursor.json').write_text(json.dumps(res)+'\n')
