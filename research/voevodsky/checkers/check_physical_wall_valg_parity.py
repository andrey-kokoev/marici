#!/usr/bin/env python3
"""Compose literal physical wall orientations with universal v_alg tail units."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
seg=json.loads((ROOT/'research/benincasa/results/rank26-literal-residue-chain-wall-segments.json').read_text())
wall=json.loads((ROOT/'research/voevodsky/results/one_wall_valg_covector.json').read_text())
orient={'g1':-1,'g2':1};tail={'g1':wall['cleared_covector'][0],'g2':wall['cleared_covector'][1]}
terms={k:orient[k]*tail[k] for k in orient};total=sum(terms.values())
checks={
 'segment_packet':seg['passed'],
 'wall_packet':wall['passed'],
 'only_two_real_segments':set(seg['active_wall_segments'])=={'g1','g2'},
 'literal_orientations':seg['active_wall_segments']['g1']['residue_orientation']=='-da' and seg['active_wall_segments']['g2']['residue_orientation']=='+db',
 'one_switch_each':all(v['switch_count']==1 for v in seg['active_wall_segments'].values()),
 'opposite_tail_units':tail=={'g1':-1,'g2':1},
 'oriented_terms_same_sign':terms=={'g1':1,'g2':1},
 'total_two':total==2,
 'mod_two_zero':total%2==0,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.physical-wall-valg-parity.v1','passed':True,'physical_wall_chain':'-w101+w110','oriented_v_alg_terms':terms,'wall_sum_v_alg_coefficient':total,'wall_sum_v_alg_parity':total%2,'conditional_thimble_column_mod2':{'v_alg':0},'remaining':'v_alg parity of common-endpoint and infinity-Gysin sewing correction','claim_boundary':'wall pieces only; not yet the closed integral thimble','checks':checks}
p=ROOT/'research/voevodsky/results/physical_wall_valg_parity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'wall_valg_coefficient':total,'mod2':total%2,'closed_thimble':False}))
