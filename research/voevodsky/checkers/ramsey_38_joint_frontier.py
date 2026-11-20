"""Synthesize an alternating middle cycle from the original ring and unordered candidate pools. Do not import known middle cycles, terminal cycles, priority orders or certificates. Search prefixes with a joint inward zipper cursor and outward nonempty-run cursor. Verify both resulting strips independently."""
from itertools import combinations, permutations
from functools import lru_cache
from ramsey_38_joint_annuli import D,load,red,bits,zipone
import json

def construct(I,Z,W):
    m=len(I);a=bits(I);s=min(Z);K=len(Z)*2;states=0
    for U in combinations(W,len(W)-len(Z)):
        H=set(Z)|(set(W)-set(U)); adj={u:sorted(v for v in H if (u in Z)!=(v in Z) and not red(u,v)) for u in H};mask=sum(1<<v for v in H)- (1<<s)
        if min(map(len,adj.values()))<2:continue
        for tail in permutations(U[1:]):
            O=(U[0],)+tail;b=bits(O);n=len(O)
            if b is None:continue
            for c in (0,1):
                allowed=[{x for x in H if red(x,y)==(c^v)} for y,v in zip(O,b)]
                edges=[{x:[v for v in adj[x] if v in h] for x in h} for h in allowed];
                if any(not any(e.values()) for e in edges) or any(sum(len(e.get(x,[])) for e in edges)<2 for x in H):continue
                for orient in (0,1):
                    ok={u:[red(x,u)==(z^orient) for x,z in zip(I,a)] for u in H}
                    for k in range(m):
                        if not ok[s][k]:continue
                        for start in range(n):
                            if not edges[start].get(s):continue
                            @lru_cache(None)
                            def dfs(x,free,i,j):
                                nonlocal states
                                states+=1;e=(start+j)%n
                                if j>n or n-j>free.bit_count()+1:return None
                                for v in edges[e].get(x,[]):
                                    if not ((free>>v)&1 or (not free and v==s)):continue
                                    for h in range(i,min(i+m-1,m)+1):
                                        if not ok[x][(k+h)%m]:break
                                        if not ok[v][(k+h)%m]:continue
                                        if not free:
                                            if h==m and n-j in (0,1):return ((x,O[e]),)
                                        else:
                                            for dj in (1,0):
                                                if j+dj<=n:
                                                    ans=dfs(v,free^(1<<v),h,j+dj)
                                                    if ans:return ((x,O[e]),)+ans
                                return None
                            hit=dfs(s,mask,0,0);dfs.cache_clear()
                            if hit:
                                M=[v for v,y in hit];owners=[y for v,y in hit];assert len(set(M))==K and set(owners)==set(O) and sum(y!=owners[t-1] for t,y in enumerate(owners))==n
                                F=zipone(I,M);G=zipone(M,O);assert F and G
                                return dict(middle=M,last=O,owners=owners,states=states,inner_strip=F,outer_strip=G)
    return dict(states=states)

out=[]
for r in load('ramsey_38_correction_continuation'):
    result=construct(r['ring'],r['Z'],r['W']);out.append(dict(ring=r['ring'],poles=r['poles'],**result));print(len(out),result['states'],'found' if 'middle' in result else 'failed',flush=True)
(D/'ramsey_38_joint_frontier.json').write_text(json.dumps(out,indent=2)+'\n')
