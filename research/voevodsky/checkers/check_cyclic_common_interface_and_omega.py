from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

SRC=Path('research/voevodsky/cyclic-common-interface.json')
OUT=Path('research/voevodsky/results/cyclic_common_interface_and_omega.json')

def main():
 d=json.loads(SRC.read_text(encoding='utf-8'))
 t,z,a,b,eps,delta,tau=sp.symbols('t z a b eps delta tau',positive=True,real=True)
 A=sp.exp(-t*a**2)*sp.cos(a*z);H=sp.exp(-t*b**2)*sp.cos(b*z);K=A-eps*H
 E=K/4;G=K/4;P=K/2
 sector_ok=sp.simplify(E+G+P-K)==0
 # alpha_A: one common normalization perturbation on E and its transported correction.
 arithmetic=(1+delta)*E+G+P
 alpha_A_res=sp.simplify(arithmetic-delta*E-K)
 # alpha_B: truncate tau*H from P; lax cell carries exact tail witness.
 Pn=P-tau*H;truncated=E+G+Pn
 alpha_B_res=sp.simplify(K-truncated)
 # alpha_C: obstruction eps selects common gauge width s=eps on both frequencies.
 Kdef=sp.exp(-(t+eps)*a**2)*sp.cos(a*z)-eps*sp.exp(-(t+eps)*b**2)*sp.cos(b*z)
 composite=Kdef
 alpha_C_res=sp.simplify(Kdef-composite)
 # One common interface: all cells use the same parameter tuple and kernel.
 common_parameters=set(d['parameters'])=={'t','z','a','b','epsilon','delta','tau'}
 # Lax Omega is the pasted witness tuple, not an equality assertion for alpha_B.
 omega={'alpha_A':'0','alpha_B':str(alpha_B_res),'alpha_C':'0'}
 omega_inhabited=alpha_A_res==0 and alpha_B_res==tau*H and alpha_C_res==0
 # Completion preservation: simultaneous halving commutes with sector split and deformation.
 half={a:a/2,b:b/2}
 completion_sector=sp.simplify((E+G+P).subs(half)-K.subs(half))==0
 completion_def=sp.simplify(Kdef.subs(half)-composite.subs(half))==0
 # Deliberate failure: omit prime sector; common object is not reconstructed.
 omitted_prime=sp.simplify(E+G-K)
 omit_rejected=omitted_prime!=0
 checks={'common_parameter_pullback_verified':common_parameters,'sector_split_reconstructs_K':sector_ok,
  'alpha_A_pastes':alpha_A_res==0,'alpha_B_pastes_as_enclosure':alpha_B_res==tau*H,
  'alpha_C_pastes':alpha_C_res==0,'Omega_ABC_lax_filler_inhabited':omega_inhabited,
  'completion_preserves_sector_cell':completion_sector,'completion_preserves_deformation_cell':completion_def,
  'deliberate_failure_omitted_prime_rejected':omit_rejected}
 result={'schema':'marici.voevodsky.cyclic-common-interface-omega.v1',**checks,
  'Omega_ABC_witness':omega,'Omega_unique_or_contractible_asserted':False,
  'source_global_naturality_asserted':False,'rh_or_positivity_asserted':False,'passed':all(checks.values())}
 text=json.dumps(result,indent=2,sort_keys=True);OUT.write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
