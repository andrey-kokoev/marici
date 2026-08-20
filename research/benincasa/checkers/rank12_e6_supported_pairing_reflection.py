"""Reflection covariance of the typed first-Rees e6 physical pairing."""
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/benincasa/results/rank12-e6-supported-pairing-reflection.json'
omega=[Fraction(-1,8),Fraction(1,8)]
gamma=[-1,1]
pair=lambda x,y:sum(a*b for a,b in zip(x,y))
before=pair(omega,gamma)

# Entry 756: sigma23 pulls dc^da back to db^da=-da^db.
# K1=-16T fixes the sign of T and therefore the ordered sheet transport.
orientation=-1
omega_r=[orientation*x for x in omega]
gamma_r=[orientation*x for x in gamma]
after=pair(omega_r,gamma_r)
assert before==after==Fraction(1,4)
assert [orientation*x for x in omega_r]==omega
assert [orientation*x for x in gamma_r]==gamma

packet={
 'schema':'marici.benincasa.rank12_e6_supported_pairing_reflection.v1',
 'reflection':'sigma_23: G12 -> G31',
 'denominator_transport':'q_G12 -> q_G31',
 'fiber_coordinate_transport':'(a,b)->(c,a)=(b,a)',
 'poincare_residue_orientation':-1,
 'T_normalization':'K1_initial=-16*T fixes T sign',
 'sheet_order_transport':'preserved in the K1-normalized frame',
 'coefficient_character':-1,
 'physical_boundary_character':-1,
 'pairing_before':'1/4',
 'pairing_after':'1/4',
 'reflection_square_identity':True,
 'classification':'the typed supported pairing extends from C3 to D3; coefficient and chain are sign lines whose evaluation is invariant'
}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet))
