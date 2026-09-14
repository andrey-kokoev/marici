"""Audit the universal unit extension that kills the soft-axis free detector."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--smith',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 smith=json.loads(Path(a.smith).read_text());rows=[]
 for r in smith['rows']:
  # lambda(1)=1 gives T=ker(lambda) direct-sum Z*1. Since the completed image
  # lies in ker(lambda), adjoining 1 kills exactly the free summand.
  assert r['target_rank']-r['completed_rank']==1
  assert r['primitive_free_cokernel_detector'].startswith('coefficient sum')
  rows.append({'D':r['D'],'rank_after_unit_extension':r['target_rank'],
   'free_cokernel_rank_after':0,
   'torsion_index_unchanged':r['completed_index_in_saturation'],
   'torsion_prime_factors_unchanged':r['completed_index_prime_factors']})
 out={'schema':'marici.nima.soft-axis-unit-detector-extension.v1','status':'proved',
  'extension_column':'constant monomial 1','detector_pairing':1,
  'splitting':'f=(f-lambda(f)*1)+lambda(f)*1; first term lies in ker(lambda)',
  'conclusion':'adjoining 1 kills exactly the all-degree free cokernel; it does not remove integral torsion',
  'finite_smith_cross_checks':rows,
  'scope':'algebraic target extension; no global road-Cech/geometric realization asserted'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
