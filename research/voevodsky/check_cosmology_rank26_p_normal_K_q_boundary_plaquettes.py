"""Verify cutoff-boundary q-lift signatures form even-anchor 2x2 plaquettes plus edge singletons."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_plaquettes.json'
def main():
 prior=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_signature_census.json').read_text()); assert prior['passed']
 lookup={(r['k_pole'],*r['exponent']):r['signature_sha256'] for r in prior['records']}; poles={}
 for kp in (0,1):
  plaquettes=[]; used=set()
  for a in range(0,10,2):
   coords=[(a,8-a),(a,9-a),(a+1,8-a),(a+1,9-a)]; hashes=[lookup[(kp,*c)] for c in coords]; assert len(set(hashes))==1
   used.update(coords); plaquettes.append({'even_anchor':a,'coordinates':[list(c) for c in coords],'signature_sha256':hashes[0]})
  lower=[(x,8-x) for x in range(1,9,2)]; upper=[(x,10-x) for x in range(0,11,2)]; singles=lower+upper
  singleton_hashes=[lookup[(kp,*c)] for c in singles]; plaquette_hashes=[p['signature_sha256'] for p in plaquettes]
  assert len(set(singleton_hashes))==len(singleton_hashes)==10
  assert not (set(singleton_hashes)&set(plaquette_hashes)); assert len(set(plaquette_hashes))==5
  assert used|set(singles)=={(x,d-x) for d in (8,9,10) for x in range(d+1)}
  poles[f'k{kp}']={'plaquettes':plaquettes,'lower_degree8_odd_singletons':[list(c) for c in lower],'upper_degree10_even_singletons':[list(c) for c in upper],'templates':15,'boundary_rows':30}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-plaquettes.v1','status':'boundary_signatures_partition_into_plaquettes_and_edge_singletons','poles':poles,'total_templates':30,'total_boundary_rows':60,'compression':'per pole: five 2x2 plaquette templates cover 20 rows; four lower odd and six upper even edge templates cover 10 singleton rows','decision':'Coordinate distance and parity classify every boundary signature; pole/degree alone does not.','limitations':['presentation-dependent pivot signatures','single prime','degree-14 boundary geometry','classification is not a source-natural homotopy'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
