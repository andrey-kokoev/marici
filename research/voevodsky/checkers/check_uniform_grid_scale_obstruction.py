"""No fixed numerator/denominator caps cover all positive rational row scales."""
from fractions import Fraction as Q
from pathlib import Path
import json
# Unit-square proof P of target x<=1 uses one x-upper source row.
old=(Q(0),Q(1),Q(0),Q(0))
def image(scale,m):return ((-m[0]+scale*m[1],-m[2]+m[3]),scale*m[1]+m[3])
assert image(Q(1),old)==((Q(1),Q(0)),Q(1))
cases=[]
for cap in (2,3,5,10,20):
 prime=next(n for n in range(cap+1,2*cap+10) if n>1 and all(n%d for d in range(2,int(n**.5)+1)))
 tiny=Q(1,prime);huge=Q(prime)
 assert (Q(1)/tiny)>cap and (Q(1)/huge).denominator>cap
 assert image(tiny,(Q(0),Q(1)/tiny,Q(0),Q(0)))==((Q(1),Q(0)),Q(1))
 assert image(huge,(Q(0),Q(1)/huge,Q(0),Q(0)))==((Q(1),Q(0)),Q(1))
 cases.append({'cap':cap,'small_row_scale':str(tiny),'required_multiplier':str(1/tiny),'large_row_scale':str(huge),'required_denominator':(1/huge).denominator})
report={'passed':True,'finite_cap_cases':cases,'general_argument':'For any finite magnitude cap M choose integer p>M: row scale 1/p sends multiplier 1 to p. For any finite reduced denominator cap D choose prime p>D: row scale p sends multiplier 1 to 1/p. Both preserve row-bound product and target exactly.','local_remedy':'Transport the finite envelope coordinatewise by reciprocal positive scales and retain the row bijection as its provenance.','scope':'Obstruction to a single fixed global bounded raw grid under arbitrary positive rational row scalings, not obstruction to finite witness-relative envelopes, Farkas proof existence, or source authority.'}
out=Path(__file__).resolve().parents[1]/'results/uniform-grid-scale-obstruction.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
