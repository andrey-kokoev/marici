#!/usr/bin/env python3
"""Resolve the prospectively selected VA1 executability gate."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
plan=json.loads((R/'research/conjecture_replay/results/prospective_valg_frontier.json').read_text())
pole=json.loads((R/'research/benincasa/results/relative-shape-pole-depth.json').read_text())
six=json.loads((R/'research/benincasa/results/relative-shape-six-term-jet.json').read_text())
checks={'VA1_was_selected':plan['prospective_policy']['first_action']=='VA1_GM_IBP_simple_residue','jet_has_no_IBP':six['ibp_reduction_applied'] is False,'lowering_homotopy_missing':pole['filtered_lowering_homotopy_constructed'] is False,'simple_residue_matrix_missing':pole['simple_residue_matrix_constructed'] is False,'proper_face_only':pole['scope'].startswith('proper face')}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.VA1-executability-audit.v1','selected_action':'VA1_GM_IBP_simple_residue','resolution':'--','reason':'The planner treated the existing Cech-coherent Gauss-Manin class as if it included a filtered IBP lowering interface. The frozen source explicitly says that the lowering homotopy and simple-residue matrix are absent.','distinction':{'available':'wall-horizontal/contact-weighted Gauss-Manin class modulo exact forms','missing':'global filtered pole-lowering homotopy compatible with K0, wall intersections, and the relative cycle'},'repair':'Split VA1 into VA0_construct_filtered_lowering followed by VA1_apply_lowering_and_project.','protocol_finding':'Action executability requires every declared input interface; an action may not bundle construction of an absent interface into an unpriced application step.','checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/VA1_executability_audit.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'--','repair':out['repair']}))
