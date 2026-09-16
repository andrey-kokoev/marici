"""Exact shell-summability audit for strong and product sewing majorants."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# Representative polynomial-growth dual: q=2, transition exponent d=3.
q=2;d=3;Mstrong=3;Mproduct=6
assert 2*Mstrong>d+q and Mproduct>d+q
rs=2*Mstrong-d-q;rp=Mproduct-d-q
rows=[]
for N in (4,8,16,32,64):
 # Integral-test bounds: sum_{n>N}(1+n)^(-1-r) <= N^(-r)/r.
 strong_tail=F(1,rs*N**rs);product_tail=F(1,rp*N**rp)
 rows.append({'N':N,'strong_tail_upper':str(strong_tail),'product_tail_upper':str(product_tail)})
checks={'strong_exponent_gate':rs>0,'product_exponent_gate':rp>0,'strong_tails_decrease':all(F(rows[i+1]['strong_tail_upper'])<F(rows[i]['strong_tail_upper']) for i in range(len(rows)-1)),'product_tails_decrease':all(F(rows[i+1]['product_tail_upper'])<F(rows[i]['product_tail_upper']) for i in range(len(rows)-1))}
out={'schema':'marici.voevodsky.two-sewing-angular-majorants.v1','growth_dimension_q':q,'transition_exponent_d':d,'strong_schwartz_order':Mstrong,'product_schwartz_order':Mproduct,'strong_decay_margin':2*Mstrong-d-q,'product_decay_margin':Mproduct-d-q,'rows':rows,'checks':checks,'all_exact':all(checks.values()),'meaning':'Polynomial per-character transition growth plus sufficiently high Schwartz angular order supplies the square-summable strong majorant and summable product majorant.','remaining_gate':'Prove the localized semilocal Hankel estimate and its polynomial character exponent d.'}
if __name__=='__main__':
 p=ROOT/'results'/'two-sewing-angular-majorants.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
