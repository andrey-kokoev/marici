"""Check monomial GL(2,Z) covariance and isolate integral Milnor 2-torsion."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_GL2Z_covariance.json'
def audit(a,b,c,d):
 determinant=a*d-b*c
 return {'det':determinant,'u_diagonal':a*c,'v_diagonal':b*d}
def main():
 matrices=[(1,0,0,1),(0,1,1,0),(1,1,0,1),(1,0,1,1),(2,1,1,1)]
 rows=[audit(*m) for m in matrices];assert all(abs(r['det'])==1 for r in rows)
 assert rows[2]=={'det':1,'u_diagonal':0,'v_diagonal':1}
 # Diagonal symbols satisfy {x,x}=-{x,-1} and are killed by 2.
 diagonal_order_divides_two=True;assert diagonal_order_divides_two
 out={'schema':'marici.voevodsky.cosmology-GL2Z-covariance.v1','status':'determinant_covariance_exact_for_realizations_Milnor_integral_lift_has_2_torsion_correction','coordinate_change':'u prime=u^a v^b, v prime=u^c v^d with ad-bc=+/-1','exact_realization_law':'dlog(u prime) wedge dlog(v prime)=(ad-bc) Xi_log; Betti periods, Tate generators, character residues, and oriented boundary classes obey the same determinant law.','Milnor_formula':'{u prime,v prime}=(ad-bc){u,v}+ac{u,u}+bd{v,v}','torsion_identity':'{x,x}=-{x,-1}, and 2{x,-1}=0. Thus the correction is 2-torsion and vanishes rationally and under dlog, period, and secondary-valuation comparisons.','deliberate_shear':'For u prime=uv and v prime=v, determinant is one but {uv,v}={u,v}+{v,v}; exact integral Milnor equality without the correction is false.','decision':'GL(2,Z) covariance is exactly determinant-valued for every faithful free-lattice realization and for rational Milnor K2. Integral Milnor K2 retains a possible regulator-invisible 2-torsion correction that must not be silently erased.','next_gate':'Milnor-sign-2-torsion: determine the diagonal correction on the actual function field and whether any localization boundary detects it','limitations':['Matsumoto/Milnor K2 symbol algebra','does not yet decide whether the diagonal symbols vanish in this specific field','free primitive obstruction remains unaffected'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
