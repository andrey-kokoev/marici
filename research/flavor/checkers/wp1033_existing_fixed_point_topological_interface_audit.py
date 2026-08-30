import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
eps=sp.Rational(1,20)
ag=(26*eps+4*eps**2)/(57-46*eps-8*eps**2)
ay=12*eps/(57-46*eps-8*eps**2)
assert sp.simplify(ay/ag-6/(13+2*eps))==0
assert ay==sp.Rational(15,1367)

bad_color=-sp.Rational(1747041281,6918678948)
bad_B=-sp.Rational(116978905,2306226316)
assert bad_color<0 and bad_B<0

chiral=sp.Matrix([[1,1,0,1,0,0],[0,1,0,0,1,1],[0,0,1,0,1,1]])
assert chiral.rank()==3 and len(chiral.T.nullspace())==0
assert sp.Rational(34182,5585)>6

gates=["source_fixed_magnitude","single_pole_interface","controlled_source","threshold_survival","physical16_instrument"]
rows={
 "WP738_required_mediators":[False,False,True,False,False],
 "WP802_litim_sannino":[True,False,True,False,False],
 "WP805_chiral_fixed_point":[True,False,False,False,False],
 "WP744_topological_inflow":[True,False,True,False,False]}
assert all(not all(v) for v in rows.values())

result={"schema":"marici.flavor.wp1033.v1","status":"PASS",
 "question":"Does an existing admitted fixed-point or quantized flavor source supply the WP1032 normalization interface?",
 "gates":gates,"candidate_matrix":rows,
 "exact_witnesses":{"WP738_negative_couplings":[str(bad_color),str(bad_B)],
 "WP802_alpha_y_star":str(ay),"WP805_phase_kernel_dimension":0,
 "WP805_uncontrolled_chiral_coordinate":str(sp.Rational(34182,5585)),
 "WP744_type":"quantized parity-odd A5 F wedge F, not CP-even pole mass"},
 "contextual_partition":"each candidate is distinguished by which interface gate first fails; no candidate occupies the all-true class",
 "smallest_exact_falsifier":"WP802 fixes alpha_y*=15/1367 but has no typed map from that normalized coupling to h=1 in m_S^2=17 h f^2",
 "classification":"empty source-authorized interface intersection; neither selector nor new rigidifier for the WP1028 pole",
 "instrument":"no candidate supplies a calibrated physical16 pole/condensate interface after thresholds",
 "remaining_gate":"derive one named map from a controlled source-fixed coupling to the CP-even single-pole mass operator, then prove threshold survival and instrument rank",
 "claim_boundary":"bounded census of WP738, WP744, WP802, and WP805; does not exclude an unstudied source theory",
 "disposition":"negative: the archive contains ingredients in separate frames, not the missing composite arrow"}
(ROOT/"results"/"wp1033_existing_fixed_point_topological_interface_audit.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1033 PASS:",ay,bad_color,bad_B,chiral.rank())
