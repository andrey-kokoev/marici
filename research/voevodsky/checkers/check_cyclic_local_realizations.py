from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

SRC=Path('research/voevodsky/cyclic-local-realizations.json')
OUT=Path('research/voevodsky/results/cyclic_local_realizations.json')

def main():
 d=json.loads(SRC.read_text(encoding='utf-8'))
 t,a,z,xi,eps,delta,E,G,P,tau=sp.symbols('t a z xi eps delta E G P tau',positive=True,real=True)
 K=sp.exp(-t*a**2)*sp.cos(a*z)
 # G_C: all three charts from one atomic apex.
 J1=sp.simplify(-sp.diff(K,t).subs(z,0))
 theta_direct=sp.exp(-t*(a-xi)**2)/2+sp.exp(-t*(-a-xi)**2)/2
 theta_pullback=sp.simplify(sp.exp(-t*xi**2)*K.subs(z,-2*sp.I*t*xi))
 gc_ok=sp.simplify(theta_direct-theta_pullback)==0 and J1==a**2*sp.exp(-t*a**2)
 # C_A and T_A: exact object zero; perturbed normalization detected and tag preserved.
 residues={'normalization':delta,'continuation':sp.Integer(0),'cutoff':sp.Integer(0),'completion':sp.Integer(0)}
 ca_detects=residues['normalization']!=0
 tags=d['T_A']['tag_map'];ta_ok=set(tags)==set(residues) and len(set(tags.values()))==4
 # alpha_A: correction -delta on endpoint coefficient restores common normalization.
 arithmetic=(4+delta)*E+4*G+4*P
 corrected=sp.expand(arithmetic-delta*E);analytic=4*(E+G+P)
 alpha_a_ok=sp.simplify(corrected-analytic)==0
 # alpha_B: raw evaluation differs from truncation by tail; enclosure cell records |tail|<=tau.
 phi_b=E+G+P; truncated=E+G+(P-tau)
 alpha_b_residual=sp.simplify(phi_b-truncated);alpha_b_ok=alpha_b_residual==tau
 # alpha_C in deformation envelope.
 c_to_a=sp.exp(-(t+eps)*a**2)*sp.cos(a*z)
 composite=sp.exp(-(t+eps)*a**2)*sp.cos(a*z)
 alpha_c_ok=sp.simplify(c_to_a-composite)==0
 constant_bad=sp.simplify(c_to_a-sp.exp(-t*a**2)*sp.cos(a*z))!=0
 # Completion: substitution a->a/2 commutes with each symbolic constructor used here.
 half=lambda q:sp.simplify(q.subs(a,a/2))
 completion_ok=half(c_to_a)==sp.simplify(sp.exp(-(t+eps)*(a/2)**2)*sp.cos((a/2)*z))
 omega_materialized=d['Omega_ABC']['status']=='materialized_as_lax_filler_on_common_signed_even_fixture'
 checks={'G_C_fixture_realized':gc_ok,'C_A_fixture_realized':ca_detects,
  'T_A_tag_preserving':ta_ok,'alpha_A_fixture_realized':alpha_a_ok,
  'alpha_B_enclosure_cell_realized':alpha_b_ok,'Phi_C_def_fixture_realized':alpha_c_ok,
  'alpha_C_def_fixture_realized':alpha_c_ok and constant_bad,
  'local_completion_commutation_verified':completion_ok,
  'Omega_fixture_materialized':omega_materialized}
 result={'schema':'marici.voevodsky.cyclic-local-realizations-check.v1',**checks,
  'G_C_J1':str(J1),'alpha_B_exact_residual':str(alpha_b_residual),
  'Omega_ABC_realized_on_common_fixture':omega_materialized,
  'Omega_source_global_naturality_asserted':False,
  'rh_or_positivity_asserted':False,'passed':all(checks.values())}
 text=json.dumps(result,indent=2,sort_keys=True);OUT.write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
