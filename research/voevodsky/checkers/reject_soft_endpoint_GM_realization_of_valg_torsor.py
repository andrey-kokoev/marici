#!/usr/bin/env python3
"""Compare the pushed-forward physical endpoint singularities with the v_alg torsor."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3];B=R/'research/benincasa'
push=json.loads((B/'soft-endpoint-pushed-forward-pointing.json').read_text())
tube=json.loads((B/'soft-endpoint-leray-tube-pairing.json').read_text())
soft=json.loads((B/'results/soft_logarithmic_ext_line.json').read_text())
cyc=json.loads((B/'soft-endpoint-pointing-cyclic-naturality.json').read_text())
checks={'pushforward_passes':push['status']=='pass','physical_form_polar_at_t0':'L/t' in push['endpoint_asymptotics']['t=0'],'physical_form_regular_at_t2':'finite' in push['endpoint_asymptotics']['t=2'],'target_has_opposite_residues':soft['integral_residue_generator']==[1,-1,0],'tube_detects_only_t0_residue':tube['tube_pairing']=='integral_{|t|=epsilon} I(t)dt = 2*pi*i*L','cyclic_transition_units_one':all(t['transition_unit']==1 for t in cyc['transitions']),'all_three_charts_same_endpoint_pattern':all(c['marked_endpoint']==0 and c['pointing_endpoint']==2 for c in cyc['charts'])}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.soft-endpoint-GM-v-alg-torsor-no-go.v1','physical_pushforward':{'base_coordinate':'t=xi+1','singular_support':['t=0'],'residue_vector_ordered_t0_t2':['L',0],'t2_behavior':'regular; moving a-cycle collapses'},'target_logarithmic_line':{'generator':'dlog(t/(t-2))','residue_vector_ordered_t0_t2':[1,-1]},'comparison':'No nonzero scalar multiple of (L,0) equals (1,-1). Adding a holomorphic Gauss-Manin transport term or changing the primitive basepoint cannot create a t=2 residue.','cyclic_scope':'The C3 transitions have unit normal Jacobian and preserve marked endpoint 0 and pointing endpoint 2, so the same support mismatch holds in all three occurrence charts.','status':'rejected for the complete cyclic soft-endpoint family','consequence':'The physical Leray tube canonically measures L, but L belongs to a one-supported logarithmic germ, not the degree-zero two-soft torsor carrying the algebraic v_alg extension coordinate.','remaining_possibilities':['a distinct physical family marked at both base-soft endpoints','a source-authorized operation on another discriminant with opposite residues'],'checks':checks,'passed':True}
d=R/'research/voevodsky/results/soft_endpoint_GM_valg_torsor_no_go.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'status':out['status'],'physical':['L',0],'target':[1,-1]}))
