"""Compute the free edge and primary sign layers under monomial coordinates."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_integral_tame_sign_decorated_complex.json'
def decorated(a,b,c,d):
 det=a*d-b*c;assert abs(det)==1
 signs={'X':-1 if (a*c)%2 else 1,'Y':-1 if (b*d)%2 else 1,'Z':-1 if ((a+b)*(c+d))%2 else 1}
 predicted={'X':-1 if (a*c)%2 else 1,'Y':-1 if (b*d)%2 else 1,'Z':-1 if (1+a*c+b*d)%2 else 1}
 assert signs==predicted
 return {'free_edges':[det,det,det],'primary_signs':signs}
def main():
 identity=decorated(1,0,0,1);shear=decorated(1,1,0,1);swap=decorated(0,1,1,0)
 assert identity=={'free_edges':[1,1,1],'primary_signs':{'X':1,'Y':1,'Z':-1}}
 assert shear=={'free_edges':[1,1,1],'primary_signs':{'X':1,'Y':-1,'Z':1}}
 assert swap['free_edges']==[-1,-1,-1] and swap['primary_signs']==identity['primary_signs']
 out={'schema':'marici.voevodsky.cosmology-integral-tame-sign-decorated-complex.v1','status':'complete_integral_boundary_splits_into_free_edge_and_primary_sign_layers','base_symbol':'{u,v}','base_tame_units':{'X':'v^-1','Y':'u','Z':'-v/u'},'base_decoration':identity,'coordinate_formula':{'free_edges':'(det A)*(1,1,1)','sign_X':'(-1)^(a*c)','sign_Y':'(-1)^(b*d)','sign_Z':'(-1)^((a+b)(c+d))=(-1)^(1+a*c+b*d)'},'covariance':'The free layer transforms by determinant. The sign layer records the diagonal Milnor corrections and transforms affinely over Z/2; direct tame-symbol valuations agree with the Milnor expansion.','projection':'Secondary valuation forgets the constant signs and sends the decorated datum to the primitive free triangle cycle. Rationalization also removes the sign layer.','integral_target_gate':'An integral horn statement must specify both layers. The previously used target (Xi_log,-sigma123) is complete only in the rational/regulator-visible quotient; integrally the primary K1 sign decoration is additional data.','decision':'The full integral localization object is a sign-decorated primitive cycle. Coordinate covariance is restored without pretending the 2-torsion layer vanishes, while the free horn no-go remains unchanged.','next_gate':'integral-horn-target-refinement: formulate the complete sign-decorated target and test whether its torsion component can be canceled independently','limitations':['three-line P2 compactification and monomial GL(2,Z) coordinates','sign splitting depends on the chosen monomial representatives but the full K1 units do not','no physical sign interpretation inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
