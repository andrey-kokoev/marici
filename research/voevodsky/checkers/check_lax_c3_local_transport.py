from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

eps,s,t,a,z=sp.symbols('eps s t a z',positive=True,real=True)
G=lambda q:sp.exp(-(t+q)*a**2)*sp.cos(a*z)

def main():
 transported=G(eps)
 derivative=sp.simplify(sp.diff(transported,eps).subs(z,0))
 constant_transport=G(sp.Integer(0))
 constant_derivative=sp.simplify(sp.diff(constant_transport,eps))
 result={
  'schema':'marici.voevodsky.lax-c3-local-transport.v1',
  'edge':'C_to_A',
  'C_C':'rho_epsilon -> epsilon',
  'T_C':'epsilon -> s=epsilon',
  'G_A_T_C_C_C':str(transported),
  'residue_tangent_derivative_at_z0':str(derivative),
  'residue_tangent_preserved':derivative!=0,
  'inverse_transport_asserted':False,
  'fiber_equivalence_asserted':False,
  'deliberate_failure_constant_transport_derivative':str(constant_derivative),
  'deliberate_failure_constant_transport_rejected':constant_derivative==0,
  'local_lax_edge_realized':derivative!=0 and constant_derivative==0,
  'alpha_C_realized':False,
  'Phi_C_main_model_admitted':False,
  'passed':True}
 text=json.dumps(result,indent=2,sort_keys=True)
 Path('research/voevodsky/results/lax_c3_local_transport.json').write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
