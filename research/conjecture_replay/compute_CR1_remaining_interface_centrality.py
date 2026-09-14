#!/usr/bin/env python3
"""Authoritative dependency/Shapley ranking of remaining CR1 interfaces."""
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from interface_centrality import InterfaceAction as A,score_interfaces,shapley_interface_values,closure
current=frozenset({'transported_eF','Kummer_loaded_relative_BM_class','v00_v10_loaded_residues','formal_four_corner_trace','finite_carrier','distinguished_theta_section','green_problem'})
actions=[
 A('form_extraordinary_specialization',frozenset({'alpha_sh_mixed_variance_connector','transported_eF','Kummer_loaded_relative_BM_class'}),frozenset({'spG_eF_equals_unit'}),8),
 A('promote_all_vertex_residues',frozenset({'spG_eF_equals_unit','full_Theta03_vertex_geometry','v00_v10_loaded_residues'}),frozenset({'global_extraordinary_Theta03_map'}),5),
 A('construct_support_witness',frozenset({'global_extraordinary_Theta03_map','ringed_proper_base_change','finite_carrier','distinguished_theta_section'}),frozenset({'CR1SupportWitness'}),8),
 A('construct_readout_witness',frozenset({'SectionBoundaryReadout'}),frozenset({'CR1ReadoutWitness'}),1),
 A('derive_work_mate',frozenset({'CR1SupportWitness','SectionBoundaryReadout','zero_line_agreement'}),frozenset({'CR1WorkMate'}),1),
 A('assemble_physical_source_package',frozenset({'CR1SupportWitness','SectionBoundaryReadout','zero_line_agreement'}),frozenset({'CR1PhysicalSourcePackage'}),1),
 A('realize_physical_recollement',frozenset({'CR1PhysicalSourcePackage'}),frozenset({'PhysicalRecollementRealization'}),1),
 A('derive_boundary_conservation',frozenset({'PhysicalRecollementRealization'}),frozenset({'ThetaBoundaryConservation'}),1),
 A('derive_RH_transverse_zero',frozenset({'ThetaBoundaryConservation'}),frozenset({'RH_transverse_zero'}),1),
]
costs={'alpha_sh_mixed_variance_connector':21,'full_Theta03_vertex_geometry':13,'ringed_proper_base_change':21,'SectionBoundaryReadout':13,'zero_line_agreement':3}
candidates=tuple(costs);scores=score_interfaces(actions,current,'RH_transverse_zero',costs);sh=shapley_interface_values(actions,current,'RH_transverse_zero',candidates)
rank=sorted(candidates,key=lambda x:(sh[x],next(s.score for s in scores if s.interface==x)),reverse=True)
out={'schema':'marici.conjecture-replay.CR1-remaining-interface-centrality.v1','model_scope':'remaining typed CR1 dependency closure from current certified interfaces to RH_transverse_zero','current_interfaces':sorted(current),'actions':[asdict(a) for a in actions],'candidate_costs':costs,'dependency_scores':[asdict(s) for s in scores],'shapley_unlock_values':sh,'shapley_rank':rank,'highest':rank[0],'qualification':'Shapley values measure declared dependency unlock utility, not probability that geometry exists. Costs affect dependency score but not Shapley allocation.','passed':rank[0]=='alpha_sh_mixed_variance_connector'};p=R/'research/conjecture_replay/results/CR1_remaining_interface_centrality.json';p.write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':out['passed'],'rank':rank,'shapley':sh,'cost_adjusted_rank':[s.interface for s in scores]}))
