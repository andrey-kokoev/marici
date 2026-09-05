from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

OUT=Path('research/voevodsky/results/cyclic_filler_pasting_complex.json')

def main():
 d1=sp.Matrix([[-1,1,0],[0,-1,1],[1,0,-1]])
 d2=sp.Matrix([[1,1,1]])
 chain=d2*d1
 rank1=d1.rank();rank2=d2.rank();ker2=d2.nullspace();im1=d1.columnspace()
 dimker=3-rank2;h2dim=dimker-rank1;cokerdim=1-rank2
 # Equality of subspaces: each image basis lies in kernel and dimensions agree.
 im_in_ker=all(d2*v==sp.zeros(1,1) for v in im1)
 exact_middle=im_in_ker and rank1==dimker
 tau,H=sp.symbols('tau H',real=True)
 D=tau*H;omega=sp.Matrix([0,D,0]);fills=d2*omega==sp.Matrix([D])
 # Deliberate failure: flip one edge-incidence sign.
 bad_d1=d1.copy();bad_d1[0,0]=1
 bad_chain=d2*bad_d1
 bad_rejected=bad_chain!=sp.zeros(1,3)
 result={
  'schema':'marici.voevodsky.cyclic-filler-pasting-complex.v1',
  'partial_1':[[int(x) for x in row] for row in d1.tolist()],
  'partial_2':[[int(x) for x in row] for row in d2.tolist()],
  'chain_identity_verified':chain==sp.zeros(1,3),
  'rank_partial_1':rank1,'rank_partial_2':rank2,'dim_kernel_partial_2':dimker,
  'image_partial_1_equals_kernel_partial_2':exact_middle,
  'H2_dimension':h2dim,'cokernel_partial_2_dimension':cokerdim,
  'Omega_boundary_equals_tau_H':fills,
  'every_face_discrepancy_fillable':cokerdim==0,
  'filler_unique_modulo_vertex_adjustments':h2dim==0,
  'literal_uniqueness_asserted':False,'contractibility_asserted':False,
  'deliberate_failure_wrong_orientation_chain':[[int(x) for x in row] for row in bad_chain.tolist()],
  'deliberate_failure_wrong_orientation_rejected':bad_rejected,
  'source_global_naturality_asserted':False,
  'passed':all([chain==sp.zeros(1,3),exact_middle,h2dim==0,cokerdim==0,fills,bad_rejected])}
 text=json.dumps(result,indent=2,sort_keys=True);OUT.write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
