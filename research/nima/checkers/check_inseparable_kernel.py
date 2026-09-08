"""Prime-field points versus nilpotent rescaling; exact modular coefficients."""
from math import comb,gcd
from pathlib import Path
import json
records=[]
for n,p in [(6,3),(9,3),(12,3),(5,2),(7,2),(8,3)]:
    m=n-3;r=m;e=0
    while r%p==0:r//=p;e+=1
    coefficients=[comb(m,j)%p for j in range(m+1)]
    first=next(j for j in range(1,m+1) if coefficients[j])
    assert first==p**e
    roots=[a for a in range(1,p) if pow(a,m,p)==1]
    assert len(roots)==gcd(r,p-1)
    # (1+epsilon)^m=1 modulo epsilon^2 precisely when p divides m.
    assert (coefficients[1]==0)==(e>0)
    if e>0:
        assert all(coefficients[j]==0 for j in range(1,p**e))
        assert coefficients[p**e]!=0 # fails at the next truncation order
    fibers={b:[a for a in range(1,p) if pow(a,m,p)==b] for b in range(1,p)}
    records.append({'n':n,'p':p,'prime_to_p_part':r,'inseparable_multiplicity':p**e,'field_kernel_points':roots,'dual_number_kernel':e>0,'first_nonzero_nilpotent_degree':first,'power_map_fibers':fibers})
assert records[0]['field_kernel_points']==[1] and records[0]['dual_number_kernel']
assert not records[-1]['dual_number_kernel']
result={'status':'passed','records':records,'scope':'Prime-field power maps and formal binomial coefficients; generic channel reduction uses crossing connectivity.'}
Path('research/nima/results/inseparable_kernel.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
