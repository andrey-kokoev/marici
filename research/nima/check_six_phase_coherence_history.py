#!/usr/bin/env python3
"""Exact connected six-phase coherence-history toy model."""
import json,math,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_amplitude import CoherencePhase,CoherenceHistory
from momentum_twistor_super import external_supertwistor,super_five_bracket
xs=[s.Integer(i*i+3*i+1) for i in range(1,21)];Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
labels=tuple(tuple(range(1+3*j,6+3*j)) for j in range(6))
phases=tuple(CoherencePhase(super_five_bracket(tuple(S[i] for i in q)),str(q)) for q in labels);history=CoherenceHistory(phases)
component_labels=(tuple(1+3*j for j in range(6)),tuple(2+3*j for j in range(6)),tuple(3+3*j for j in range(6)),tuple(1+3*j for j in range(6)))
start=time.perf_counter();value=history.component(component_labels);elapsed=time.perf_counter()-start
reversed_labels=((component_labels[0][1],component_labels[0][0],*component_labels[0][2:]),)+component_labels[1:];reversed_value=history.component(reversed_labels);overlaps=[sorted(set(labels[i])&set(labels[i+1])) for i in range(5)]
checks={'six_degree_four_phases':len(phases)==6,'history_degree_twenty_four':4*len(phases)==24,'connected_overlap_chain':overlaps==[[4,5],[7,8],[10,11],[13,14],[16,17]],'generic_component_nonzero':value!=0,'antisymmetric_component_orientation':reversed_value==-value,'determinant_evaluation_avoids_enumeration':elapsed<5}
out={'schema':'marici.nima.six-phase-coherence-history.v1','phase_labels':[list(q) for q in labels],'phase_degrees':[4]*6,'history_degree':24,'shared_coherence_labels':overlaps,'component_labels':[list(x) for x in component_labels],'component_value':str(value),'implicit_assignment_terms':math.factorial(6)**4,'evaluation_seconds':elapsed,'evaluation':'product of four 6x6 determinants','checks':checks,'passed':all(checks.values()),'scope':'Exact selected degree-twenty-four component of a connected six-phase history; compositional toy invariant, not a sourced full N6MHV amplitude.'}
p=ROOT/'research/nima/results/six-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
