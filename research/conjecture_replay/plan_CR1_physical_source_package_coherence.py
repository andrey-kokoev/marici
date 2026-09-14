#!/usr/bin/env python3
"""Next coherence rung: local D03 specialization to CR1PhysicalSourcePackage."""
import json,sys
from dataclasses import asdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from refinement import InterfaceType,Gate,RefinementPlan,AggregationRule
I=InterfaceType
def g(n,req,out,d,c=5): return Gate(n,frozenset(req),(I(out,'local_CR1_geometry','global_CR1_physical_data'),),c,4,6,5,True)
gates=(
 g('CR1PK1_assemble_all_Theta03_road_vertices',{'D03_extraordinary_specialization'},'full_Theta03_vertex_residue_system','vertex'),
 g('CR1PK2_check_road_and_adjacent_flip_compatibility',{'full_Theta03_vertex_residue_system'},'road_flip_compatible_residue_system','road'),
 g('CR1PK3_glue_extraordinary_maps_by_Cech_descent',{'road_flip_compatible_residue_system'},'global_Cech_descended_extraordinary_map','cech',8),
 g('CR1PK4_verify_ringed_six_functor_mates',{'global_Cech_descended_extraordinary_map'},'ringed_proper_base_change_mate','six',13),
 g('CR1PK5_verify_rotation_reflection_sheet_coherence',{'road_flip_compatible_residue_system'},'symmetric_CR1_support_map','symmetry',8),
 g('CR1PK6_compare_support_with_distinguished_theta_section',{'ringed_proper_base_change_mate','symmetric_CR1_support_map'},'inhabited_CR1SupportWitness','support',10),
 g('CR1PK7_construct_source_SectionBoundaryReadout',{'source_theta_green_data'},'inhabited_SectionBoundaryReadout','readout',13),
 g('CR1PK8_identify_support_and_analytic_zero_lines',{'inhabited_CR1SupportWitness','inhabited_SectionBoundaryReadout'},'inhabited_CR1PhysicalSourcePackage','zero',5),
)
deps=(
 ('CR1PK1_assemble_all_Theta03_road_vertices','CR1PK2_check_road_and_adjacent_flip_compatibility'),
 ('CR1PK2_check_road_and_adjacent_flip_compatibility','CR1PK3_glue_extraordinary_maps_by_Cech_descent'),
 ('CR1PK3_glue_extraordinary_maps_by_Cech_descent','CR1PK4_verify_ringed_six_functor_mates'),
 ('CR1PK2_check_road_and_adjacent_flip_compatibility','CR1PK5_verify_rotation_reflection_sheet_coherence'),
 ('CR1PK4_verify_ringed_six_functor_mates','CR1PK6_compare_support_with_distinguished_theta_section'),
 ('CR1PK5_verify_rotation_reflection_sheet_coherence','CR1PK6_compare_support_with_distinguished_theta_section'),
 ('CR1PK6_compare_support_with_distinguished_theta_section','CR1PK8_identify_support_and_analytic_zero_lines'),
 ('CR1PK7_construct_source_SectionBoundaryReadout','CR1PK8_identify_support_and_analytic_zero_lines'),
)
plan=RefinementPlan('CR1PhysicalSourcePackage',gates,deps,AggregationRule());plan.validate()
out={'schema':'marici.conjecture-replay.CR1-physical-source-package-coherence.v1','parent':'CR1PhysicalSourcePackage','activation':'after any external-specialization branch constructs D03_extraordinary_specialization','aggregation':'all eight gates must resolve ++','gates':[asdict(x) for x in gates],'dependencies':[list(x) for x in deps],'coherence_diamonds':[{'left':['CR1PK3_glue_extraordinary_maps_by_Cech_descent','CR1PK4_verify_ringed_six_functor_mates'],'right':['CR1PK5_verify_rotation_reflection_sheet_coherence'],'join':'CR1PK6_compare_support_with_distinguished_theta_section','meaning':'descent/base-change and symmetry produce the same support-to-theta comparison'},{'left':['CR1PK6_compare_support_with_distinguished_theta_section'],'right':['CR1PK7_construct_source_SectionBoundaryReadout'],'join':'CR1PK8_identify_support_and_analytic_zero_lines','meaning':'geometric and analytic zero objects agree'}],'terminal_interface':'inhabited_CR1PhysicalSourcePackage','agda_consumers':['physicalSourcePackageGivesPhysicalRealization','physicalSourcePackageGivesBoundaryConservation','physicalSourcePackageThetaZeroImpliesTransverseZero'],'passed':True};p=R/'research/conjecture_replay/results/CR1_physical_source_package_coherence.json';p.write_text(json.dumps(out,indent=2,default=list)+'\n');print(json.dumps({'passed':True,'gates':len(gates),'dependencies':len(deps),'diamonds':len(out['coherence_diamonds']),'terminal':out['terminal_interface']}))
