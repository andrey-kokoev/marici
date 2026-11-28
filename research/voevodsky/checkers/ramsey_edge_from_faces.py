"""Injective 12-edge selection from six face contacts, with a min-cost relaxation."""
from itertools import combinations,product
from collections import Counter
from ramsey_seven_role_coexist import roots_and_lines,pairings,decode,D
import json


def assignment(cost):
    # Rectangular Hungarian algorithm (rows <= columns), integer potentials.
    n=len(cost);m=len(cost[0]);u=[0]*(n+1);v=[0]*(m+1);p=[0]*(m+1);way=[0]*(m+1)
    for i in range(1,n+1):
        p[0]=i;j=0;dist=[999]*(m+1);used={0}
        while True:
            cur=p[j];delta=999;nxt=0
            for k in range(1,m+1):
                if k in used:continue
                d=cost[cur-1][k-1]-u[cur]-v[k]
                if d<dist[k]:dist[k]=d;way[k]=j
                if dist[k]<delta:delta=dist[k];nxt=k
            for k in range(m+1):
                if k in used:u[p[k]]+=delta;v[k]-=delta
                else:dist[k]-=delta
            j=nxt;used.add(j)
            if not p[j]:break
        while j:
            k=way[j];p[j]=p[k];j=k
    out=sorted((r-1,k-1) for k,r in enumerate(p) if k and r);assert len(out)==n and sum(cost[i][j] for i,j in out)==-v[0];return -v[0],out


def audit():
    roots,lines=roots_and_lines();hist=[Counter() for _ in range(4)];example=None;single=Counter();total=0
    for idx,v in roots:
        a=decode(lines[idx-1].decode());ns=[i for i in range(27) if a[v]>>i&1];sup={a[i]&a[v] for i in range(27) if i!=v and i not in ns}
        for six in combinations(ns,6):
            for ps in pairings(list(six)):
                if sum(sum(1<<i for i in q) in sup for q in product(*ps))!=7:continue
                f=[t for p in ps for t in p];verts=sorted(set(range(27))-set(f));ms=[sum(1<<k for k,x in enumerate(f) if a[y]>>x&1) for y in verts];edges=[(i,j) for i,j in combinations(range(6),2) if i//2!=j//2];costs=[[] for _ in range(4)]
                for i,j in edges:
                    b=(1<<i)|(1<<j);d=[min((m^(1<<(i^1))).bit_count(),(m^(1<<(j^1))).bit_count()) for m in ms];costs[0].append([int(m&b!=b) for m in ms]);costs[1].append([int(m!=b) for m in ms]);costs[2].append([int(x>0) for x in d]);costs[3].append(d)
                vals=[assignment(c) for c in costs];scores=[12-k if i<3 else k for i,(k,_) in enumerate(vals)];total+=1
                for h,x in zip(hist,scores):h[x]+=1
                single[sum(m.bit_count()==1 for m in ms)]+=1
                if example is None:example=dict(record=idx,root=v,pairs=ps,scores=scores,best_repair=[dict(faces=[f[k] for k in edges[i]],old_vertex=verts[j],old_face_contacts=[f[k] for k in range(6) if ms[j]>>k&1],cost=costs[3][i][j]) for i,j in vals[3][1]])
    assert total==161;out=dict(histograms=dict(zip(('match_both','match_exact_pair','retain_wedge','minimum_face_link_changes'),hist)),singleton_candidates=single,example=example);print(out);(D.parent/'ramsey_edge_from_faces.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
