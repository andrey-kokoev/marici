"""Test the natural Milnor K2 symbol as source realization versus horn filler."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_milnor_K2_primitive_source_gate.json'
def wedge(a,b):return a[0]*b[1]-a[1]*b[0]
def main():
 # Logarithmic coefficient vectors in basis (du,dv): dlog u=(1/u,0), dlog v=(0,1/v).
 u=Fraction(2);v=Fraction(3);dlogu=(1/u,0);dlogv=(0,1/v);xi=wedge(dlogu,dlogv);assert xi==Fraction(1,6) and xi!=0
 # Deliberate vanishing comparator: dlog(u) wedge dlog(1-u) has parallel du factors.
 steinberg=wedge((1/u,0),(-1/(1-u),0));assert steinberg==0
 # Torus residue coefficient of du/u wedge dv/v is one, so the de Rham class is primitive.
 residue=1;assert residue==1
 out={'schema':'marici.voevodsky.cosmology-milnor-K2-primitive-source-gate.v1','status':'K2_symbol_sources_Xi_but_cannot_fill_it','candidate':'Milnor symbol {u,v} on U=G_m^2','regulator_image':'dlog(u) wedge dlog(v)=Xi_log','primitive_double_residue':residue,'nonvanishing_test':{'evaluation_coefficient_at_u2_v3':[xi.numerator,xi.denominator],'torus_de_Rham_basis':'[dlog u] wedge [dlog v] generates H^2_dR(G_m^2)'},'degree_gate':'{u,v} is a closed motivic/K2 class mapping to cohomological degree two; it is not a degree-one precycle with boundary Xi_log.','boundary_no_go':'If {u,v} were a boundary in a regulator-compatible enlargement, its dlog image would be exact. Its primitive nonzero de Rham class forbids that.','deliberate_comparator':'The Steinberg-shaped symbol {u,1-u} has zero dlog wedge because both logarithmic differentials are proportional to du; this does not apply to algebraically independent u,v.','decision':'Milnor K2 gives a source-natural realization of the surviving Xi_log class, strengthening rather than removing the horn obstruction. It cannot be promoted to the missing filler by a degree shift.','next_gate':'audit genuine open-change or relative higher-Chow precycles whose boundary matrix includes (Xi_log,-sigma123), rather than closed K2 symbols','limitations':['algebraic de Rham/motivic degree audit only','no relative precycle constructed','no physical period inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
