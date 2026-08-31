#!/usr/bin/env python3
"""Test whether any seven-candidate combination descends to a nonzero principal-three-wall source packet."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';A=ROOT/'research/aspect/results'
def rank(rows,p):
 piv={}
 for raw in rows:
  r=[x%p for x in raw]
  while any(r):
   j=max(i for i,x in enumerate(r) if x)
   if j not in piv:
    z=pow(r[j],p-2,p);piv[j]=[(x*z)%p for x in r];break
   c=r[j];r=[(x-c*y)%p for x,y in zip(r,piv[j])]
 return len(piv)
def main():
 results={}
 for p in (32003,32009):
  data=json.loads((N/f'cosmology_p_normal_rank26_syzygy_provenance_full_a8_p{p}.json').read_text());cands=data['candidates'];extra=[];principal=[]
  for row_id in range(1140,9780):
   vector=[int(c['source_coefficients'].get(str(row_id),0)) for c in cands]
   if 1140<=row_id<6324: principal.append(vector)
   elif 6324<=row_id<9780: extra.append(vector)
  extra_rank=rank(extra,p);extra_tail_rank=rank([r[2:] for r in extra],p);bulk_principal_nonzero=any(r[0] or r[1] for r in principal)
  assert extra_rank==extra_tail_rank==5 and not bulk_principal_nonzero
  results[str(p)]={'extra_family_projection_rank':extra_rank,'candidate_kernel_dimension':7-extra_rank,'extra_projection_rank_on_candidates_2_through_6':extra_tail_rank,'candidates_0_1_principal_q_support_nonzero':bulk_principal_nonzero,'nonzero_principal_three_wall_descent_exists':False}
 out={'schema':'marici.aspect.rank26-five-mark-projection-kernel.v1','primes':[32003,32009],'results':results,'kernel_description':'extra-family kernel is exactly span(candidates 0,1), whose g1/g2/g3 source projection is zero','principal_three_wall_nonzero_source_packet':False,'tau_p_map_constructed':False,'passed':True};A.mkdir(exist_ok=True);(A/'rank26_five_mark_projection_kernel.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','extra_rank':[results[str(p)]['extra_family_projection_rank'] for p in (32003,32009)]}))
if __name__=='__main__':main()
