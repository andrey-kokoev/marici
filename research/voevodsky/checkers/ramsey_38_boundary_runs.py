"""Sufficient static certificate. Assign each edge of the blue first boundary to the highest-priority compatible unused vertex. Require one nonempty circular run per terminal vertex. The resulting fans glue at run endpoints. No zipper search for the second strip in the selector; independently verify hits."""
from ramsey_38_joint_annuli import D,load,red,zipone,boundaries,bits
from itertools import permutations
import json
from collections import Counter

def rule(M,U):
    m=len(M);assert not any(bits(M));near={u:[red(x,u) for x in M] for u in U};n=len(U)
    for O in permutations(U):
        if O[0]!=min(U) or O[-1]<O[1]:continue
        b=bits(O)
        if b is None:continue
        for c in (0,1):
            masks={u:sum(1<<i for i in range(m) if near[u][i]==near[u][(i+1)%m]==c^q) for u,q in zip(O,b)}
            if any(not v for v in masks.values()):continue
            for pri in permutations(U):
                free=(1<<m)-1;owner=[None]*m
                for u in pri:
                    new=masks[u]&free
                    if not new:break
                    for i in range(m):
                        if new>>i&1:owner[i]=u
                    free^=new
                if free:continue
                runs=[v for i,v in enumerate(owner) if v!=owner[i-1]]
                if len(runs)!=n or set(runs)!=set(U):continue
                k=runs.index(O[0]);seq=runs[k:]+runs[:k]
                if seq==list(O) or seq==[O[0],*O[:0:-1]]:return dict(last=O,priority=pri,owner=owner)

out=[];rows=load('ramsey_38_correction_continuation');olds=load('ramsey_38_second_annulus')
for idx,(r,old) in enumerate(zip(rows,olds)):
    def check(M):
        U=sorted(set(r['W'])-set(M));hit=rule(M,U)
        if hit and zipone(r['ring'],M):
            assert zipone(M,hit['last']);return dict(first=M,**hit)
    oldhit=check(old['inner']);hit=oldhit;tries=0
    if not hit:
        for M in boundaries(r['Z'],r['W']):
            tries+=1;hit=check(M)
            if hit:break
    out.append(dict(index=idx,old_pass=bool(oldhit),tried=tries,certificate=hit));print(idx,bool(hit),tries,flush=True)
print('coverage',sum(bool(x['certificate']) for x in out),sum(x['old_pass'] for x in out));(D/'ramsey_38_boundary_runs.json').write_text(json.dumps(out,indent=2)+'\n')
