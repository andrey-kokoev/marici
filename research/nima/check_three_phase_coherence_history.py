#!/usr/bin/env python3
"""Exact connected three-phase coherence-history toy model."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_amplitude import CoherencePhase,CoherenceHistory
from momentum_twistor_super import external_supertwistor,super_five_bracket
xs=[s.Integer(i*i+3*i+1) for i in range(1,12)];Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
labels=((1,2,3,4,5),(4,5,6,7,8),(7,8,9,10,11))
phases=tuple(CoherencePhase(super_five_bracket(tuple(S[i] for i in q)),''.join(map(str,q))) for q in labels)
history=CoherenceHistory(phases)
component_labels=((1,4,7),(2,5,8),(3,6,9),(1,4,7));value=history.component(component_labels)
# Reversing two labels in one SU(4) component must reverse orientation.
reversed_labels=((4,1,7),)+component_labels[1:];reversed_value=history.component(reversed_labels)
checks={'three_degree_four_phases':len(phases)==3 and all(all(len(m)==4 for m in p.weight) for p in phases),'history_degree_twelve':4*len(phases)==12,'connected_overlap_chain':set(labels[0])&set(labels[1])=={4,5} and set(labels[1])&set(labels[2])=={7,8},'generic_component_nonzero':value!=0,'antisymmetric_component_orientation':reversed_value==-value}
out={'schema':'marici.nima.three-phase-coherence-history.v1','formula':'[1,2,3,4,5] then [4,5,6,7,8] then [7,8,9,10,11]','phase_degrees':[4,4,4],'history_degree':12,'shared_coherence_labels':[[4,5],[7,8]],'component_labels':[list(x) for x in component_labels],'component_value':str(value),'assignment_terms':6**4,'checks':checks,'passed':all(checks.values()),'scope':'Exact selected degree-twelve component of a connected three-phase history; a compositional toy invariant, not a sourced full N3MHV amplitude.'}
p=ROOT/'research/nima/results/three-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
