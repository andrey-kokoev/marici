"""Account for the 7+3 readings on unused reflection orbits. Test also invariant matching structurally: fixed positions must match fixed positions, moving positions must match moving positions. Compute both conditions independently of the count predictor."""
from ramsey_strip_closure_control import out,r,N,fixed,dist,rules
from collections import Counter
from pathlib import Path
import json
counts=Counter();records=[]
for z in out:
    p=z['path'];rem=set(range(30))-set(p)-{r[i] for i in p};bs=z['bridge'][0];flag=lambda x:tuple(int(tuple(dist[x][v] for v in bs) in rule) for rule in rules);orbits=[x for x in range(30) if x<r[x]];assert len(orbits)==12 and all(sum(flag(x)[i] for x in orbits)==4 for i in (0,1));u,v=sorted(rem&set(orbits));assert u<15<=v;ff=rem&fixed;left=sorted(x for x in ff if x<15);right=sorted(ff-set(left));assert len(left)==len(right)==2;assert any(all(y in N[x] for x,y in zip(left,perm)) for perm in (right,right[::-1]));link=bool(N[u]&{v,r[v]});assert link==z['closes'];c=tuple(4-flag(u)[i]-flag(v)[i] for i in (0,1));assert c==tuple(map(len,z['selected']));s=lambda x:''.join(map(str,flag(x)));counts[s(u),s(v),link]+=1
    if not link:
        j=c.index(2);isol=z['isolated'];assert set(isol)=={isol[0],r[isol[0]]} and all(flag(x)[j] and not flag(x)[1-j] for x in isol)
    records.append(dict(half=p,unused_reps=[u,v],flags=[flag(u),flag(v)],adjacent_orbits=link,counts=c))
print(counts);Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
