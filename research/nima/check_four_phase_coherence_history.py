#!/usr/bin/env python3
"""Exact connected four-phase coherence-history toy model."""
import json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_amplitude import CoherencePhase,CoherenceHistory
from momentum_twistor_super import external_supertwistor,super_five_bracket
xs=[s.Integer(i*i+3*i+1) for i in range(1,15)];Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
labels=((1,2,3,4,5),(4,5,6,7,8),(7,8,9,10,11),(10,11,12,13,14))
phases=tuple(CoherencePhase(super_five_bracket(tuple(S[i] for i in q)),str(q)) for q in labels);history=CoherenceHistory(phases)
component_labels=((1,4,7,10),(2,5,8,11),(3,6,9,12),(1,4,7,10));start=time.perf_counter();value=history.component(component_labels);elapsed=time.perf_counter()-start
reversed_labels=((4,1,7,10),)+component_labels[1:];reversed_value=history.component(reversed_labels)
overlaps=[sorted(set(labels[i])&set(labels[i+1])) for i in range(3)]
checks={'four_degree_four_phases':len(phases)==4 and all(all(len(m)==4 for m in p.weight) for p in phases),'history_degree_sixteen':4*len(phases)==16,'connected_overlap_chain':overlaps==[[4,5],[7,8],[10,11]],'generic_component_nonzero':value!=0,'antisymmetric_component_orientation':reversed_value==-value}
out={'schema':'marici.nima.four-phase-coherence-history.v1','formula':'[12345] then [45678] then [7891011] then [1011121314]','phase_degrees':[4,4,4,4],'history_degree':16,'shared_coherence_labels':overlaps,'component_labels':[list(x) for x in component_labels],'component_value':str(value),'assignment_terms':24**4,'evaluation_seconds':elapsed,'checks':checks,'passed':all(checks.values()),'scope':'Exact selected degree-sixteen component of a connected four-phase history; compositional toy invariant, not a sourced full N4MHV amplitude.'}
p=ROOT/'research/nima/results/four-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
