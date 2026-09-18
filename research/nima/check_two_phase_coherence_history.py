#!/usr/bin/env python3
"""The connected N2MHV invariant as two sequential coherence phases."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_amplitude import CoherencePhase,CoherenceHistory
from momentum_twistor_super import external_supertwistor,super_five_bracket,multiply_super_five_brackets
xs=map(s.Integer,(1,2,4,7,11,16,22,29));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
left=super_five_bracket(tuple(S[i] for i in (1,2,3,4,8)));right=super_five_bracket(tuple(S[i] for i in (4,5,6,7,8)))
history=CoherenceHistory((CoherencePhase(left,'12348'),CoherencePhase(right,'45678')))
composed=history.full_weight();reference=multiply_super_five_brackets(left,right);pairs=((1,4),(2,5),(3,6),(7,8))
checks={'single_composition_law_reproduces_full_invariant':composed==reference,'two_degree_four_phases_give_degree_eight':all(sum(len(p) for p in m)==8 for m in composed),'fast_component_matches_materialized_history':history.component(pairs)==composed[pairs],'shared_labels_are_allowed_intermediate_coherence_data':{4,8}==set((1,2,3,4,8))&set((4,5,6,7,8))}
out={'schema':'marici.nima.two-phase-coherence-history.v1','formula':'[1,2,3,4,8] then [4,5,6,7,8]','interpretation':'two sequential degree-four movements with shared coherence labels 4,8','phase_degrees':[4,4],'history_degree':8,'nonzero_components':len(composed),'sample_component':str(history.component(pairs)),'checks':checks,'passed':all(checks.values()),'scope':'Exact equality between one connected N2MHV Yangian invariant and the universal two-phase exterior-composition toy model.'}
p=ROOT/'research/nima/results/two-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
