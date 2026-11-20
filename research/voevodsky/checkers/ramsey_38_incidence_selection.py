"""Two priority tests without ID tie breaks: maximize weakest inward edge support, and, separately on known run certificates, assign least flexible terminal first. Keep all tied boundary maxima and all tied priority orders. The cyclic order and relative potential in the latter test are supplied, not inferred."""
from ramsey_38_joint_annuli import D,load,red,zipone,boundaries,bits
from itertools import permutations,groupby
from collections import Counter
import json

def scarce(M,O,c):
    b=bits(O);m=len(M);n=len(O);A={u:{j for j in range(m) if red(M[j],u)==red(M[(j+1)%m],u)==(b[k]^c)} for k,u in enumerate(O)};goods=total=0
    for p in permutations(O):
        if any(len(A[x])>len(A[y]) for x,y in zip(p,p[1:])):continue
        total+=1;owner=[next((u for u in p if j in A[u]),None) for j in range(m)];runs=[u for j,u in enumerate(owner) if u!=owner[j-1]]
        if len(runs)!=n or set(runs)!=set(O):continue
        i=runs.index(O[0]);seq=runs[i:]+runs[:i];goods+=seq==O or seq==[O[0],*O[:0:-1]]
    return goods,total

def extends(M,U):
    for t in permutations(U[1:]):
        O=[U[0],*t];
        if O[1]<O[-1] and zipone(M,O):return True
    return False

out=[]
for r,cert in zip(load('ramsey_38_correction_continuation'),load('ramsey_38_boundary_runs')):
    I=r['ring'];a=bits(I);V=r['Z']+r['W'];support={(x,y):tuple(sum(red(x,u)==red(y,u)==(k^c) for u,k in zip(I,a)) for c in (0,1)) for x in V for y in V};groups={}
    for M in boundaries(r['Z'],r['W']):
        S=[support[x,y] for x,y in zip(M,M[1:]+M[:1])];score=max(tuple(sorted(v[c] for v in S)) for c in (0,1));groups.setdefault(score,[]).append(M)
    for score in sorted(groups,reverse=True):
        best=[M for M in groups[score] if zipone(I,M)]
        if best:break
    hits=sum(extends(M,sorted(set(r['W'])-set(M))) for M in best);cert=cert['certificate'];M,O=cert['first'],cert['last'];b=bits(O);u=cert['owner'][0];c=red(M[0],u)^b[O.index(u)];good,total=scarce(M,O,c)
    out.append(dict(poles=r['poles'],ring=I,score=score,top_tied=len(best),top_extend=hits,scarce_good=good,scarce_orders=total));
print('boundary groups',Counter('none' if not x['top_extend'] else 'all' if x['top_extend']==x['top_tied'] else 'mixed' for x in out));print('priority groups',Counter('none' if not x['scarce_good'] else 'all' if x['scarce_good']==x['scarce_orders'] else 'mixed' for x in out));print(out[0]);(D/'ramsey_38_incidence_selection.json').write_text(json.dumps(out,indent=2)+'\n')
