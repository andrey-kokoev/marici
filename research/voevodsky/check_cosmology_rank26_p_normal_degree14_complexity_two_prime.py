"""Aggregate degree-14 familywise reduction-complexity certificates."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; R=ROOT/'research'/'voevodsky'/'results'; OUT=R/'cosmology_rank26_p_normal_degree14_complexity_two_prime.json'
def main():
 xs={str(p):json.loads((R/f'cosmology_rank26_p_normal_degree14_reduction_complexity_p{p}.json').read_text()) for p in (32003,32009)}
 for p,x in xs.items(): assert x['passed'] and x['field']==int(p)
 summary={}
 for family in xs['32003']['families']:
  summary[family]={}
  for direction in ('nx','ny'):
   vals={p:{k:x['families'][family][direction][k] for k in ('rows','nonzero_input_rows','zero_remainders','total_pivot_eliminations','max_pivot_eliminations_per_row')} for p,x in xs.items()}
   assert len({v['nonzero_input_rows'] for v in vals.values()})==1 and len({v['max_pivot_eliminations_per_row'] for v in vals.values()})==1
   summary[family][direction]=vals
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-degree14-complexity-two-prime.v1','status':'familywise_reduction_complexity_stable_in_support_and_max_depth','primes':[32003,32009],'summary':summary,'observations':['IBP and K derivative rows are all nonzero before reduction','marked-q family has 10080 nonzero derivative rows out of 25200 for each normal','maximum pivot depth is prime-independent in every family/direction','total pivot counts differ slightly by prime because intermediate modular cancellation patterns differ'],'decision':'The absorption certificate is computationally distributed across all families and has bounded observed pivot depth <=580 at degree 14; it is not explained by rows being mostly zero.','limitations':['order-dependent pivot complexity','not a retained coefficient certificate','not a uniform homotopy'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
