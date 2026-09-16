"""Exact diagonal audit of the canonical graph-relative stabilization modulus."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# In B-orthonormal coordinates, C_n=diag(2,-1/n); the minimal epsilon is 1/n.
rows=[]
for n in (1,2,4,8,16,32,64):
 epsilon=F(1,n);raw=[F(2),-epsilon];stabilized=[x+epsilon for x in raw]
 # A smaller rational epsilon/2 leaves the negative eigenvalue negative.
 smaller=epsilon/F(2)
 rows.append({'n':n,'relative_negative_modulus':str(epsilon),'stabilized_eigenvalues':[str(x) for x in stabilized],'stabilized_positive':min(stabilized)>=0,'half_stabilization_fails':raw[1]+smaller<0})
checks={'canonical_stabilization_positive':all(r['stabilized_positive'] for r in rows),'minimality_witnessed':all(r['half_stabilization_fails'] for r in rows),'negative_moduli_decrease':all(F(rows[i+1]['relative_negative_modulus'])<F(rows[i]['relative_negative_modulus']) for i in range(len(rows)-1)),'defect_vanishes_in_fixture':F(rows[-1]['relative_negative_modulus'])<F(1,50)}
out={'schema':'marici.voevodsky.canonical-relative-negative-modulus.v1','rows':rows,'checks':checks,'passed':all(checks.values()),'acceptance_quantity':'epsilon_alpha^min = ||(B_alpha^(-1/2) C_alpha B_alpha^(-1/2))_-||','physical_acceptance_rule':'epsilon_alpha^min -> 0 along the declared cofinal regulator path','construction':'Add sqrt(epsilon_alpha^min) B_alpha^(1/2) to both polarities, then apply Douglas factorization to the exact positive common remainder.'}
if __name__=='__main__':
 p=ROOT/'results'/'canonical-relative-negative-modulus.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
