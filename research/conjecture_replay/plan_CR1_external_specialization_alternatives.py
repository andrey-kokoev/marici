#!/usr/bin/env python3
"""Refine the missing D03 specialization into genuinely alternative geometric routes."""
import json,sys
from dataclasses import asdict
from itertools import combinations
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from refinement import InterfaceType,Gate,RefinementPlan,ExistentialAggregationRule
parent='CR1A1a1i1a1a2i1a1a2b1a1a1a1a1_construct_external_nearby_cycle_specialization'
base=frozenset(json.loads((R/'research/conjecture_replay/results/CR1_marked_extraordinary_Q_leg_authoritative_graph.json').read_text())['after_snapshot']['interfaces'])
req=frozenset({'formal_D03_cubical_calculus','primitive_D03_first_flip_line','gallery_kernel_zero_Q_obstruction'})
def gate(name,out,cost,elim,tight,falsify,hard=False):
 return Gate(name,req,(InterfaceType(out,'transported_Yoneda_e_F','D03_extraordinary_costalk_unit'),),cost,elim,tight,falsify,hard)
gates=(
 gate('CR1SP1_deformation_to_normal_cone_specialization','D03_DNC_specialization',13,3,5,4,True),
 gate('CR1SP2_nearby_vanishing_cycle_specialization','D03_psi_phi_specialization',21,5,7,6,True),
 gate('CR1SP3_Ext1_Cartier_Gysin_specialization','D03_Ext1_Gysin_specialization',8,4,6,6,True),
 gate('CR1SP4_Cousin_local_cohomology_specialization','D03_Cousin_specialization',10,4,7,5,True),
 gate('CR1SP5_non_gallery_Q_source_specialization','D03_alternate_Q_source_specialization',12,6,8,7,True),
)
plan=RefinementPlan(parent,gates,(),ExistentialAggregationRule('*+'));plan.validate();nxt=plan.next_gate(base)
names=tuple(g.name for g in gates)
pairwise=[{'left':a,'right':b,'common_source':'transported_Yoneda_e_F','common_target':'D03_extraordinary_costalk_unit','required_equation':'sp_'+a+'(e_F) = sp_'+b+'(e_F) = [1]'} for a,b in combinations(names,2)]
coherence={'activation':'for every pair of branches resolved with terminal +','pairwise_comparisons':pairwise,'layers':[{'name':'source_transport','requires':'same transported e_F and Yoneda normalization'},{'name':'costalk_orientation','requires':'same D03 costalk shift and positive conormal orientation'},{'name':'unit_class','requires':'both maps yield the identical nonzero class [1]'},{'name':'Cousin_boundary','requires':'images agree after the geometric Cousin boundary map'},{'name':'proper_base_change','requires':'mates agree under the ringed proper-base-change square'},{'name':'Theta03_readout','requires':'comparisons assemble at all road vertices and agree with the full Theta03 trace'}],'failure_policy':'a coherence failure does not erase an individually successful branch; it opens a typed comparison gate and blocks use of the branches as interchangeable evidence','ordinary_gallery_excluded':True}
assert len(pairwise)==10 and len(coherence['layers'])==6
out={'schema':'marici.conjecture-replay.CR1-external-specialization-alternatives.v1','parent':parent,'parent_status':'unresolved','aggregation':{'kind':'existential','success':'at least one branch has terminal +','all_terminal_minus':'parent -+'},'shared_contract':{'++':'typed geometric map constructed and sp_G(e_F)=[1] proved','+-':'typed map constructed but unit comparison unresolved','-+':'candidate source is obstructed or maps e_F to zero','--':'candidate geometry is unavailable or ill-typed'},'gates':[{'gate':asdict(g),'score':g.score()} for g in gates],'dependencies':[],'available_interfaces':sorted(base),'negative_constraint':'No branch may identify its map with ordinary galleryToQ followed by qToCostalk; RHCR1GalleryQNoGo excludes that route.','next_rung_coherence':coherence,'recommended_first':nxt.name if nxt else None,'recommendation_reason':'highest hard-gate information/falsification score per estimated cost; it reuses the certified finite-free dual and Cartier residue','passed':nxt is not None};p=R/'research/conjecture_replay/results/CR1_external_specialization_alternatives.json';p.write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':out['passed'],'branches':len(gates),'recommended_first':out['recommended_first'],'score':nxt.score() if nxt else None}))
