"""Blind candidate count on a named predecessor. Score afterwards by subgraph embeddings for every feasible reverse cut-pair/row signature, not just known witness comparisons."""
import json,gzip
from itertools import combinations,islice
from collections import Counter
from ramsey_cube_retention_floor import CAT,D,decode,G,induced

def ends(e):return (1<<e[0])|(1<<e[1])
def audit():
    record=262402;z=0
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,record,None)).strip())
    vs=[i for i in range(27) if i!=z];blue=[(i,j) for i,j in combinations(vs,2) if not a[i]>>j&1];marks=[(i,j) for i,j in blue if (a[i]&a[j]).bit_count()==1];choices=lambda rows:{(e,f) for e,f in combinations(rows,2) if not ends(e)&ends(f)};pred=choices(marks);total=len(choices(blue));direct={k for k in pred if all((a[i]&a[j])==(1<<z) for i,j in k)}
    # From here on, use the target solely as a scoring oracle. Every way to reach it has a reverse signature among the 48 complete successes.
    truth,ct,visits=score(a,z)
    rep=json.loads((D.parent/'ramsey_cube_two_cut_forward.json').read_text());known=tuple(sorted(tuple(sorted(e)) for e in rep['add']));assert known in truth
    out=dict(record=record,deleted=z,blue_links=len(blue),marked_links=len(marks),all_disjoint_pairs=total,predicted_pairs=len(pred),true_pairs=sorted(truth),hits=len(pred&truth),false_candidates=len(pred-truth),missed=len(truth-pred),both_centered_on_deleted=dict(calls=len(direct),hits=len(direct&truth)),embeddings=ct['embeddings'],search_nodes=visits);print(out);(D.parent/'ramsey_forward_link_filter.json').write_text(json.dumps(out,indent=2)+'\n')

def score(a,z,solutions=None):
    vs=[i for i in range(len(a)) if i!=z]
    core=induced(G,json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels']);rows=json.loads((D.parent/'ramsey_cube_cut_location.json').read_text())['cases'];truth=set();ct=Counter();V=sum(1<<i for i in vs);b=[v&V for v in a];visits=0
    for r in rows:
        if len(r['row'])!=a[z].bit_count():continue
        s=set(r['row']);required=core[:];ban=[0]*26
        for i,j in r['cuts']:required[i]^=1<<j;required[j]^=1<<i;ban[i]|=1<<j;ban[j]|=1<<i
        dom=[sum(1<<j for j in vs if (i in s)==bool(a[z]>>j&1) and b[j].bit_count()>=required[i].bit_count()) for i in range(26)];f=[-1]*26
        def dfs(ds,remaining):
            nonlocal visits
            visits+=1
            if not remaining:
                key=tuple(sorted(tuple(sorted((f[i],f[j]))) for i,j in r['cuts']));truth.add(key);ct['embeddings']+=1
                if solutions is not None and key not in solutions:solutions[key]=f[:]
                return
            i=min(remaining,key=lambda i:(ds[i].bit_count(),-required[i].bit_count()));rest=remaining-{i};opts=ds[i]
            while opts:
                bit=opts&-opts;opts-=bit;j=bit.bit_length()-1;dd=ds[:];f[i]=j
                for h in rest:
                    d=ds[h]&~bit
                    if required[i]>>h&1:d&=b[j]
                    if ban[i]>>h&1:d&=~b[j]
                    if not d:break
                    dd[h]=d
                else:dfs(dd,rest)
        dfs(dom,set(range(26)))
    return truth,ct,visits
if __name__=='__main__':audit()
