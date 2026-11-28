"""Erase all Q/T-to-exterior edges on one positive marking. Keep the labeled H, pocket and four face neighborhoods. Enumerate, join by exterior degree, check full graph; canonical incidence via singleton/pair/triple masks up to corner permutations."""
from collections import Counter,defaultdict
from itertools import combinations,permutations
import json
from ramsey_cube_construct35 import G,cells,corner
from ramsey_retention_slice import D,check
from ramsey_face_pair_obstruction import bits

def audit():
    z=cells.index('0**');root=34;F=(1<<35)-1;face=G[root]&G[z];q=G[root]&~face;t=G[z]&~face;H=F&~(G[root]|G[z]|1<<root|1<<z);R=H&~__import__('functools').reduce(int.__or__,(G[h] for h in bits(face)));X=H^R;assert (H.bit_count(),R.bit_count(),X.bit_count())==(21,5,16);I=[0]
    for i in bits(H):I.extend([s|1<<i for s in I if not s&G[i]])
    Is=set(I);trip=[s for s in I if not s&~X and s.bit_count()==3];qs={k:[s for s in I if s.bit_count()==k] for k in (4,5,6)};assert max(map(int.bit_count,I))==6
    stage_counts={}
    def panels(group):
        cs=[[s|(G[v]&R) for s in trip if s|(G[v]&R) in Is] for v in bits(group)];miss={s:{k:sum(1<<j for j,a in enumerate(qs[k]) if not s&a) for k in qs} for c in cs for s in c};out=[]
        stages=Counter();stage_counts[str(bits(group))]=stages
        def dfs(rows):
            if len(rows)==4:
                stages['six']+=1
                if any(__import__('functools').reduce(int.__and__,(miss[v][5] for v in sub)) for sub in combinations(rows,3)):return
                stages['five']+=1
                if __import__('functools').reduce(int.__and__,(miss[v][4] for v in rows)):return
                out.append(tuple(s&X for s in rows));return
            for s in cs[len(rows)]:
                if any(miss[s][6]&miss[v][6] for v in rows):continue
                dfs(rows+[s])
        dfs([]);assert tuple(G[v]&X for v in bits(group)) in out;return out
    Q,T=panels(q),panels(t);base=G[:];vs=bits(q)+bits(t);xs=bits(X)
    for v in vs:base[v]&=~X
    for i in xs:base[i]&=~(q|t)
    need=tuple(8-base[i].bit_count() for i in xs);quota=lambda rows:tuple(sum(s>>i&1 for s in rows) for i in xs);bucket=defaultdict(list)
    for rows in T:bucket[quota(rows)].append(rows)
    def incidence(g):return sorted(sum(1<<k for k,j in enumerate(bits(G[root])) if g[i]>>j&1) for i in range(26))
    cube=incidence(G);orb=set()
    def is_cube(m):
        if not orb:
            for p in permutations(range(8)):
                orb.add(tuple(sorted(sum(1<<p[i] for i in bits(s)) for s in cube)))
        return tuple(m) in orb
    count=Counter();ex=None
    for a in Q:
        for b in bucket[tuple(n-c for n,c in zip(need,quota(a)))]:
            count['degree']+=1;g=base[:]
            for v,s in zip(vs,a+b):
                g[v]|=s
                for i in bits(s):g[i]|=1<<v
            assert all(n.bit_count()==8 for n in g)
            if any(g[i]&g[j] for i in range(35) for j in bits(g[i])):continue
            count['triangle_free']+=1
            if not check(g,F,3,9):continue
            count['legal']+=1;count['original']+=g==G;cube_yes=is_cube(incidence(g));count['cube_incidence']+=cube_yes
            if not cube_yes and ex is None:ex=g
    assert count['original']==1;out=dict(z=z,face=bits(face),q=bits(q),t=bits(t),R=bits(R),H=bits(H),first=len(Q),second=len(T),by_clique_size=stage_counts,separate_pairs=len(Q)*len(T),counts=count,noncube=ex);print(out);(D.parent/'ramsey_face_cube_mark_joint.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
