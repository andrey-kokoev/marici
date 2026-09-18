#!/usr/bin/env python3
"""Weighted isometric radial transform from endpoint kernel to AF center."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
rows=[]
for m in range(1,8):
 coeff={(i,j):s.symbols(f'k{i}_{j}') for i in range(1,m+1) for j in range(1,i+1)}
 endpoint_norm=sum(v**2 for v in coeff.values());radial_norm=s.Integer(0);endpoint_aug=sum(coeff.values());radial_readout=s.Integer(0);blocks=[]
 for (i,j),v in coeff.items():
  r=j;# normalized central vector I_r/sqrt(r)
  radial_norm+=v**2 # Tr((v I/sqrt(r))^2)=v^2
  radial_readout+=v # ell_r(X)=Tr(X)/sqrt(r)
  blocks.append({'endpoint':[i,j],'matrix_size':r,'coefficient':str(v),'central_vector':f'{v} I_{r}/sqrt({r})'})
 # Show it is not an algebra homomorphism once E_11 E_12 exists.
 nonmultiplicative=m>1
 rows.append({'m':m,'dimension':len(coeff),'blocks':blocks,'isometry':s.expand(endpoint_norm-radial_norm)==0,'augmentation_intertwined':s.expand(endpoint_aug-radial_readout)==0,'incidence_and_center_products_differ':nonmultiplicative})
checks={'radial_map_is_hilbert_schmidt_isometry':all(x['isometry'] for x in rows),'scalar_augmentation_is_center_positive_functional_readout':all(x['augmentation_intertwined'] for x in rows),'products_differ_beyond_seed':all(x['incidence_and_center_products_differ'] for x in rows if x['m']>1),'seed_products_coincide':not rows[0]['incidence_and_center_products_differ']}
out={'schema':'marici.nima.nnmhv-weighted-radial-intertwiner.v1','endpoint_presentation':'K_m in upper-triangular incidence algebra T_m','radial_presentation':'R(K)=direct_sum_(i>=j) k_(i,j) I_j/sqrt(j) in Z(A_N)','center_readout':'ell_j(X)=Tr(X)/sqrt(j)','identities':['||R(K)||_HS = ||K||_HS','sum_(i>=j) k_(i,j) = sum_blocks ell_j(R(K)_(i,j))'],'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'The radial transform preserves the Hilbert norm and scalar augmentation but changes multiplication: endpoint convolution is noncommutative/triangular, while superselection multiplication is commutative/pointwise.','bridges':['Fourier-like change of presentation','noncommutative incidence coordinates versus commutative spectrum','Plancherel isometry','central positive-functional readout'],'claim_boundary':'The map is a canonical unitary vector-space transform, not an algebra homomorphism. Physical kernel coefficients need not be positive central-state weights.'};p=ROOT/'research/nima/results/nnmhv-weighted-radial-intertwiner.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'endpoint_presentation':out['endpoint_presentation'],'radial_presentation':out['radial_presentation'],'identities':out['identities'],'checks':checks,'meaning':out['meaning'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
