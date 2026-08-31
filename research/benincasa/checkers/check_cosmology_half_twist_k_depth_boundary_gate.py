#!/usr/bin/env python3
"""Type the observed K-pole persistence against the hard K_DEPTH truncation."""
import importlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research'/'benincasa'));charts=importlib.import_module('g12_g31_residue_chart_transition');rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');R=ROOT/'research'/'benincasa'/'results'
assert charts.K_DEPTH==2
# raw_relations constructs columns at k=0,1,2 but K-multiplication rows only for k=0,1.
column_k_levels=list(range(charts.K_DEPTH+1));k_relation_source_levels=list(range(charts.K_DEPTH));assert column_k_levels==[0,1,2] and k_relation_source_levels==[0,1]
persistence=json.loads((R/'cosmology_half_twist_k_pole_persistence_rule.json').read_text());assert persistence['passed']
out={'schema':'marici.benincasa.cosmology-half-twist-k-depth-boundary-gate.v1','declared_K_DEPTH':charts.K_DEPTH,'column_K_pole_levels':column_k_levels,'K_multiplication_source_levels':k_relation_source_levels,'terminal_K_pole_level':2,'observed_survival_level':2,'observed_death_level':1,'survival_coincides_with_terminal_truncation_boundary':True,'K_pole_2_has_outgoing_K_multiplication_relation':False,'K_pole_1_has_outgoing_K_multiplication_relation':True,'geometric_persistence_inferred':False,'interpretation':'the finite persistence rule is aligned exactly with the hard K-depth boundary: surviving generators occupy the terminal k=2 block, from which the presentation provides no outgoing K-multiplication row; their survival is truncation-protected until a K_DEPTH=3 compatibility test is performed','next_gate':'increase K_DEPTH to 3 in an isolated compatible presentation and test whether the former terminal k=2 image survives; do not promote the current barcode to geometric persistence','passed':True};(R/'cosmology_half_twist_k_depth_boundary_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
