#!/usr/bin/env python3
"""Integrate the current finite CR programme into a contradiction-safe frontier."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[3]
paths={
'n8_boundary':'research/nima/results/n8-boundary-programme-manifest.json',
'arbitrary_cr':'research/nima/results/arbitrary-m-coherent-resolution.json',
'weighted':'research/nima/results/a3-weighted-local-system-code-audit.json',
'formal_alignment':'research/nima/results/a3-weighted-formal-alignment.json',
'flavor':'research/nima/results/a3-flavor-weighted-integration.json',
'control':'research/nima/results/arbitrary-m-characteristic-inverse.json',
'bcj':'research/nima/results/six-point-cr-bcj-no-go-certificate.json',
'g4':'research/nima/results/independent-g4-interface-population-audit.json',
'rh':'research/nima/results/rh-programme-frontier.json',
'scc':'research/nima/results/n8-exceptional-boundary-transition-refined-scc.json',
'facet_carrier':'research/nima/results/arbitrary-m-facet-cochain-carrier.json',
'lean_carrier':'research/nima/results/lean-polygon-diagonal-alignment.json',
'history_facet_compiler':'research/nima/results/arbitrary-n-history-to-facet-compiler.json',
'codim2_incidence':'research/nima/results/arbitrary-m-codim2-facet-incidence.json',
'mod2_edge_obstruction':'research/nima/results/a3-mod2-transport-obstruction.json'}
docs={k:json.loads((R/v).read_text()) for k,v in paths.items()}
checks={'all_inputs_pass':all(x['passed'] for x in docs.values()),'n8_boundary_closed':docs['n8_boundary']['checks']['all_40_shared_cancel_directly'] and docs['n8_boundary']['checks']['physical_boundary_completion'],'finite_cr_exact':docs['arbitrary_cr']['checks']['all_contracted_to_empty_face_apex'],'flat_weighted_line_trivial':docs['weighted']['disposition']['flat_positive_transport'].startswith('trivial gauge twist'),'formal_scope_bounded':'full arbitrary-m chain-complex theorem' in docs['formal_alignment']['claim_boundary'],'flavor_physical_map_absent':'physical_flavor' in docs['flavor']['separated_obstructions'],'control_static_only':docs['control']['control_disposition'].startswith('This is a static'),'bcj_bridge_obstructed':docs['bcj']['checks']['defect_rank_four'],'g4_constructor_absent':docs['g4']['slot_counts']['independently_populated']==0,'rh_not_claimed':docs['rh']['claim_boundary'].endswith('RH proof or disproof.'),'scc_lanes_separated':docs['scc']['checks']['three_semantic_lanes'],'facet_promotion_bounded':'does not supply arbitrary-m physical densities' in docs['facet_carrier']['claim_boundary'],'lean_carrier_repaired':docs['lean_carrier']['checks']['counts_match_all_tested'],'history_facet_compiler_complete':docs['history_facet_compiler']['checks']['compiler_surjective_to_all_facets'],'codim2_index_complete':docs['codim2_incidence']['checks']['closed_form_counts_match'],'mod2_obstruction_gauge_invariant':docs['mod2_edge_obstruction']['checks']['mutation_graph_connected'] and docs['mod2_edge_obstruction']['edge_counts']['nonunit']==17}
frontier=[
{'branch':'finite n=8 canonical boundary','status':'closed','next':'arbitrary-m residue/descent promotion only'},
{'branch':'arbitrary-n facet compiler','status':'all supported and boundary-completion histories biject onto every A_m facet; all codim2 tests indexed with closed lane counts','next':'canonical-form/positroid representatives and oriented residue cancellation'},
{'branch':'combinatorial CR_m','status':'proved for each finite m','next':'complete Lean strict-chain and cone-homotopy packaging'},
{'branch':'positive coefficient local system','status':'trivial Q gauge twist; 17/21 A3 edge ratios obstruct direct F2 descent invariantly','next':'new integral-unit model required; no code semantics'},
{'branch':'flavor','status':'free presentation only','next':'Carrier-to-weak-basis-Yukawa chain map'},
{'branch':'control','status':'static coordinate isomorphism','next':'source-derived state evolution, actuator, and output maps'},
{'branch':'radiative/double copy','status':'obstructed at rank-4 six-point BCJ chain defect','next':'source-derived Jacobi numerators on CR generators'},
{'branch':'independent G4','status':'blocked with 0/64 slots populated','next':'CR-derived arithmetic J_r functor and G_r,s forms'},
{'branch':'RH unchanged Evans','status':'falsified under tested membership criterion','next':'modified sourced state or independent G4 only'}]
out={'schema':'marici.nima.coherent-resolution-programme-frontier.v1','inputs':paths,'checks':checks,'passed':all(checks.values()),'frontier':frontier,'nonconflation_rules':['Finite exactness does not imply physical descent.','Flat Q transport does not imply a binary code.','A free flavor relabeling does not define Yukawa flavor.','Static reconstruction does not define time evolution.','Evaluated BCJ identities do not imply a CR chain map.','A complete target schema does not supply an independent constructor.','A failed unchanged-Evans state does not decide RH.'],'claim_boundary':'Integrated status manifest only; every scientific claim retains the narrower boundary of its source result.'}
p=R/'research/nima/results/coherent-resolution-programme-frontier.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
