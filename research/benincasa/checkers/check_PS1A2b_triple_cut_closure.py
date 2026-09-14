#!/usr/bin/env python3
"""PS1A2b: evaluate the Cech triple coboundary of the admitted pair packet."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
pairs=json.loads((ROOT/'research/benincasa/results/PS1A2a_pair_overlap_currents.json').read_text());local=json.loads((ROOT/'research/benincasa/results/PS1A2_global_marked_cut_Cech_gluing.json').read_text())
e=dict(zip(local['edge_order'],local['integral_edge_coefficients']))
# Vertex order c,a,b and edge order ca,cb,ab: delta(e)=e_ab-e_cb+e_ca.
triple=e['ab']-e['cb']+e['ca']
v=local['local_vector'];true_coboundary={'ca':v[1]-v[0],'cb':v[2]-v[0],'ab':v[2]-v[1]};true_triple=true_coboundary['ab']-true_coboundary['cb']+true_coboundary['ca']
checks={'pair_packet_passed':pairs['resolution']=='++','admitted_coefficients_match':list(e.values())==[z['cochain_coefficient'] for z in pairs['pair_currents']],'admitted_triple_nonzero':triple!=0,'actual_vertex_coboundary_closes':true_triple==0,'chain_boundary_was_mistyped_as_Cech_coboundary':e!=true_coboundary}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.PS1A2b-triple-cut-closure.v1','prospective_action':'PS1A2b_triple_cut_closure','outcome_contract':{'++':'weighted pair packet has zero alternating restriction at the triple cut','+-':'triple residual is exact with a materialized source triple homotopy','-+':'admitted pair coefficients have a nonzero triple residual','--':'triple restriction cannot be typed'},'edge_orientation':'delta(e)=e_ab-e_cb+e_ca','admitted_edge_coefficients':e,'triple_residual':triple,'resolution':'-+','diagnosis':'PS1A2 solved the simplicial chain equation partial(edge)=vertex deviation, then used that edge chain as though it were a Cech 1-cochain. These are dual incidence maps and cannot be identified.','repair_edge_coefficients':true_coboundary,'repair_triple_residual':true_triple,'branch_status':'PS1A remains unresolved because the correctly typed vertex Cech coboundary is integral and closes identically; the admitted pair packet must be replaced before inference.','next':'PS1A2c replace pair weights by delta(v) and re-evaluate their source-oriented double-Leray currents.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/PS1A2b_triple_cut_closure.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'-+','triple_residual':triple,'repair':true_coboundary,'repair_residual':0,'next':'PS1A2c_correct_Cech_pair_weights'}))
