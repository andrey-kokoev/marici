"""Exhaust coordinate changes of the fixed local decision, not automorphisms of the whole graph."""
from itertools import permutations
from collections import Counter
from ramsey38_one_pin_holdout import P,prev,json,faces
from ramsey38_mesh_single_pin import domains,reduce_domains,shelling,attaches,boundary,setup,graph

def run():
    out=[]
    for e in json.loads(P.read_text())['cases']:
        for d in e['requests']:
            if not d.get('pin') or d['pick']:continue
            c=d['commit'];Q,E,B,F=domains(e,c);L,rs,_=setup(graph(e['word']),e['u']);amb=[a for a in L if len(Q[a])>1];results={};meshes={}
            for a in amb:
                for i,s in enumerate(Q[a]):
                    D,_=reduce_domains({**Q,a:[s]});res='abstain'
                    if all(len(ss)==1 for ss in D.values()):
                        M=frozenset.union(*(ss[0] for ss in D.values()));assert shelling(M) and boundary(M)==B and boundary(M|E)==F and any(all(attaches(M|set(o[:j]),t) for j,t in enumerate(o)) for o in permutations(E));res=meshes.setdefault(M,'mesh'+str(len(meshes)))
                    results[a,i]=res
            stats=[Counter(),Counter()];frames=[];marked=[c['first'][0],c['second'][0],d['j'],d['l']];best=None;framesets=0
            for perm in permutations(L):
                tr=dict(zip(L,perm));encode=lambda f:tuple(sorted(tr[w] for w in f));star=lambda s:tuple(sorted(encode(f) for f in s));mask=lambda m:encode([w for j,w in enumerate(L) if m>>j&1]);rowkey=tuple(mask(rs[j]) for j in marked),tuple(sorted(mask(s) for j,s in rs.items() if j not in marked));sig=(rowkey,tr[c['first'][1]],tr[c['second'][1]],tr[c['tip']],star(B),star(F),star(E));
                for idx in (0,1):
                    a=min(amb,key=lambda a:(-len(Q[a]) if idx else 0,tr[a]));i=min(range(len(Q[a])),key=lambda i:star(Q[a][i]));stats[idx][results[a,i]]+=1
                if best is None or sig<best:best=sig;frames=[]
                if sig==best:frames.append((perm,results[a,i]))
            canon=sorted({r for perm,r in frames});assert all(sum(z.values())==5040 for z in stats);z=dict(record=e['record'],root=e['u'],targets=[d['j'],d['l']],smallest=dict(stats[0]),largest=dict(stats[1]),marked_stabilizer=len(frames),canonical_outputs=canon,meshes={n:faces(m) for m,n in meshes.items()});out.append(z);print(e['record'],stats,len(frames),canon)
    assert len(out)==2;prev.save(prev.out/'ramsey38_mesh_equivariance_audit.json',dict(source_sha=prev.sha(P.read_bytes()),cases=out))
if __name__=='__main__':run()
