"""Necessary compatibility on the OLD 16 sites only. Each future pair gets two independent hitting masks. Distinct new vertices with masks U,V cannot be red if U&V and cannot be blue if some old independent five misses both. Build pairwise compatibility graph (including repeat choices). Strengthen by red triangles or blue sevens using three or four new vertices when cross-edge colors are forced. No learned witness choices in filter. Positive controls: all eight-pair induced hosts retaining the seed in the previously generated 11-pair witness."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement
from functools import lru_cache
import json
H=Path(__file__).parent;trace=json.loads((H/'ramsey_aligned_blind.json').read_text());swap=lambda x:((x&0x5555)<<1)|((x&0xaaaa)>>1)
def screen(edges):
    N=[0]*16
    for a,b in edges:N[a]|=1<<b;N[b]|=1<<a
    A=[0]
    for i,n in enumerate(N):A += [s|1<<i for s in A if not s&n]
    five=[s for s in A if s.bit_count()==5];six=[s for s in A if s.bit_count()==6]
    @lru_cache(None)
    def allowed(u,v):return (1 if not u&v else 0)|(2 if all(s&(u|v) for s in five) else 0)
    types=[(s,swap(s),c) for s in A if s<=swap(s) and all(s&f for f in six) for c in (1,2) if allowed(s,swap(s))&c];adj=[set() for _ in types];weak=[set() for _ in types];co=0;exact2=0
    def feasible(i,j):
        a,b,c=types[i];u,v,d=types[j];return allowed(a,u) and allowed(a,v)
    def actual2(i,j):
        a,b,c=types[i];u,v,d=types[j];S=[a,b,u,v]
        for e in (1,2):
            if not allowed(a,u)&e:continue
            for f in (1,2):
                if not allowed(a,v)&f:continue
                cols=[c,e,f,f,e,d];P=list(combinations(range(4),2));red={p for p,k in zip(P,cols) if k==1}
                valid=True
                for k in (3,4):
                    for T in combinations(range(4),k):
                        pairs=set(combinations(T,2));miss=0
                        for h in T:miss|=S[h]
                        if k==3 and pairs<=red or (not pairs&red and any(x.bit_count()==7-k and not x&miss for x in A)):valid=False;break
                    if not valid:break
                if valid:return True
        return False
    for i,j in combinations_with_replacement(range(len(types)),2):
        if feasible(i,j):
            co+=1;weak[i].add(j);weak[j].add(i)
            if actual2(i,j):adj[i].add(j);adj[j].add(i);exact2+=1
    tri=any(adj[i]&adj[j] for i in range(len(types)) for j in adj[i]);return dict(types=len(types),compatible_old_only=co,three_old_only=any(weak[i]&weak[j] for i in range(len(types)) for j in weak[i]),compatible_two_pairs=exact2,three_pairwise_compatible=tri)
old=screen(trace[7]['edges']);assert trace[7]['n']==16;last=trace[-1]['edges'];controls=[]
for kept in combinations(range(1,11),7):
    verts=[2*i+d for i in (0,*kept) for d in (0,1)];inv={v:i for i,v in enumerate(verts)};s=screen([(inv[a],inv[b]) for a,b in last if a in inv and b in inv]);assert s['three_pairwise_compatible'];controls.append(dict(kept=kept,**s))
print(old,len(controls),{k:(min(x[k] for x in controls),max(x[k] for x in controls)) for k in old});(H/'ramsey_aligned_future_reservation.json').write_text(json.dumps(dict(dead=old,controls=controls),indent=2)+'\n')
