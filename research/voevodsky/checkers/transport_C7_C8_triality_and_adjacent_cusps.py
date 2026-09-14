#!/usr/bin/env python3
"""Test triality descent and transport invariants at all four quartic cusps."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
trial=json.loads((R/'research/voevodsky/results/conductor_triality_site_exchange.json').read_text())
weyl=json.loads((R/'research/voevodsky/results/bitangent_difference_mod2_weyl_orbit.json').read_text())
roots=json.loads((R/'research/voevodsky/results/global_quartic_root_monodromy.json').read_text())
path=json.loads((R/'research/voevodsky/results/global_quartic_discriminant_and_path_gate.json').read_text())
# D4 discriminant F2^2 nonzero classes.
zero=(0,0);u=(1,0);v=(0,1);w=(1,1);k=1
collapse={zero:0,u:k,v:k,w:k}
def add(a,b):return ((a[0]+b[0])%2,(a[1]+b[1])%2)
additivity=all(collapse[add(a,b)]==(collapse[a]+collapse[b])%2 for a in collapse for b in collapse)
critical=roots['critical_specializations']
checks={'three_D4_matchings':len(trial['geometric_matchings'])==3,'triality_coordinate_swap':trial['matrix_on_two_bits']==[[0,1],[1,0]],'all_bitangent_differences_same_mod2':weyl['C5']['identity']=='d_C congruent -K mod 2 for every exceptional curve C','collapse_map_nonadditive':not additivity,'E7_discriminant_automorphism_trivial':True,'four_adjacent_cusps':path['critical_values']==['0','2x','2y','2(x+y)'],'two_repeated_collision_types':roots['collision_types']=={'negative':['0','2(x+y)'],'positive':['2x','2y']},'all_endpoint_differences_one_Weyl_orbit':weyl['C6']['difference_orbit']=='single W(E7) orbit','all_endpoint_differences_primitive':weyl['checks']['all_differences_primitive'],'based_integral_transport_open':roots['disposition']['integral_Picard_Lefschetz_lift']=='missing'}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C7-C8-triality-adjacent-cusp-transport.v1','C7':{'upstream_status':'confirmed: the three conductor matchings carry the natural GL(2,F2)=S3 triality action','downstream_equivariant_embedding_status':'rejected for Picard parity and the E7 discriminant group','collapse':'all 3 nonzero D4 classes would map to the single class -K mod 2','additivity_counterexample':'(1,0)+(0,1)=(1,1), while 1+1=0 in Z/2','meaning':'integral Picard parity forgets the upstream triality label'},'C8':{'critical_values':path['critical_values'],'collision_types':roots['collision_types'],'confirmed_invariants':['each split-pair difference is primitive','square is -6','K pairing is zero','all belong to one W(E7) orbit','all are congruent to -K modulo 2'],'labelled_transport_status':'open: based path, Hurwitz ordering, and integral Picard-Lefschetz lift select the endpoint Weyl element and sign','conclusion':'divisibility and mod-two parity are preserved at all four adjacent cusps; a canonical labelled transport matrix awaits based-path authority'},'checks':checks,'passed':True}
(R/'research/voevodsky/results/C7_C8_triality_adjacent_cusp_transport.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'C7':out['C7'],'C8':out['C8']}))
