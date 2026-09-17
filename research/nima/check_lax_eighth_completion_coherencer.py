#!/usr/bin/env python3
"""Aggregate certificate for the lax eighth completion coherencer."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
R=ROOT/'research/nima/results'
required={
 'H_completion':'rooted-substitution-completion.json',
 'V_completion':'physical-cut-completion.json',
 'C_completion':'forward-comparison-completion.json',
 'LO_domain':'convolution-observation-joint-graph.json',
 'source_pullback':'source-pulled-lo-graph.json',
 'H_graph_stability':'rooted-convolution-lo-graph-stability.json',
 'V_graph_stability':'physical-cut-lo-graph-stability.json',
 'q_graph_leakage':'qdlo-leakage-transport.json',
 'prism_registry':'vertexwise-eighth-completion-prism.json',
 'joint_closability':'arithmetic-joint-closability.json',
}
data={k:json.loads((R/f).read_text()) for k,f in required.items()}
prism=data['prism_registry']
checks={
 'all_dependencies_pass':all(x.get('passed',False) for x in data.values()),
 'components_128':prism['component_count']==128,
 'naturality_squares_448':prism['square_count']==448,
 'six_strict_families_384':prism['square_status_counts']['constructed']==384,
 'one_lax_family_64':prism['square_status_counts']['lax']==64,
 'no_open_or_conditional_pair_faces':prism['square_status_counts']['open']==prism['square_status_counts']['conditional']==0,
 'q_lax_cell_nonzero':data['q_graph_leakage']['checks']['nonzero_lax_cell_retained'],
 'q_shell_modification_coherent':data['q_graph_leakage']['checks']['shell_cocycle_after_multiplier'] and data['q_graph_leakage']['checks']['shell_cocycle_after_observation'],
 'H_and_V_preserve_pulled_graph':data['H_graph_stability']['passed'] and data['V_graph_stability']['passed'],
 'arithmetic_joint_closability_constructed':data['joint_closability']['passed'],
}
out={'schema':'marici.nima.lax-eighth-completion-coherencer.v1','kind':'lax cubical natural transformation R:Q_X=>Q_hat on axes H,V,D,q,L,C,O','components':128,'naturality_2_cells':448,'strict_face_families':['R x H','R x V','R x D','R x L','R x C (forward)','R x O'],'lax_face_family':'R x q','lax_cell':'A_X=P_X F (I-P_X)','modification_law':'A_X=P_X F (P_Y-P_X)+P_X F (I-P_Y), preserved by admitted H,V,L,O transports','dependencies':required,'checks':checks,'strict_eight_cube':False,'conditional_lax_coherencer_assembled':all(checks.values()),'lax_eighth_coherencer_constructed':all(checks.values()),'scope':['projective exponential/Laurent source completion','forward retained-graph comparison','admitted Mellin and Laurent graph multipliers','transverse marked physical cuts','source-pulled QDLO graph'],'nonclaims':['strict finite-cutoff Fourier naturality','bounded inverse to realization comparison','arbitrary completed observers','nontransverse loaded divisors']}
out['passed']=out['lax_eighth_coherencer_constructed']
p=R/'lax-eighth-completion-coherencer.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
