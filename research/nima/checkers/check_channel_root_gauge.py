"""Integer exponent witness embedding uniform channel roots in triangle gauge."""
from itertools import combinations
from pathlib import Path
import json
records=[]
for n in range(4,13):
    def s(i,j):return int(j-i>1 and (i,j)!=(0,n-1))
    h={(i,j,k):s(i,j)+s(j,k) for i,j,k in combinations(range(n),3)}
    u={(i,j):0 if i==0 else h[0,i,j] for i,j in combinations(range(n),2)}
    for i,j,k in h:assert u[j,k]-u[i,k]+u[i,j]==h[i,j,k]
    hol=sum(u[i,i+1] for i in range(n-1))-u[0,n-1]
    assert hol==n-3
    # A primitive (n-2)nd root fails: the holonomy exponent is nonzero modulo n-2.
    assert hol%(n-2)!=0
    records.append({'n':n,'triangle_identities':len(h),'boundary_holonomy_exponent':hol,'wrong_root_residue':hol%(n-2)})
result={'status':'passed','records':records,'witness':'u_0i=1; u_ij=zeta^(s_0i+s_ij) for 0<i<j', 'scope':'Integer exponent identities n=4..12 plus generic formula; no floating roots used.'}
Path('research/nima/results/channel_root_gauge.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
