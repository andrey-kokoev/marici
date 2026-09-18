#!/usr/bin/env python3
"""Exact connected seven-phase coherence-history toy model."""
import json,math,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_amplitude import CoherencePhase,CoherenceHistory
from momentum_twistor_super import external_supertwistor,super_five_bracket
k=7;n=3*k+2
xs=[s.Integer(i*i+3*i+1) for i in range(1,n+1)];Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
labels=tuple(tuple(range(1+3*j,6+3*j)) for j in range(k));phases=tuple(CoherencePhase(super_five_bracket(tuple(S[i] for i in q)),str(q)) for q in labels);history=CoherenceHistory(phases)
component_labels=(tuple(1+3*j for j in range(k)),tuple(2+3*j for j in range(k)),tuple(3+3*j for j in range(k)),tuple(1+3*j for j in range(k)))
start=time.perf_counter();value=history.component(component_labels);elapsed=time.perf_counter()-start
reversed_labels=((component_labels[0][1],component_labels[0][0],*component_labels[0][2:]),)+component_labels[1:];reversed_value=history.component(reversed_labels);overlaps=[sorted(set(labels[i])&set(labels[i+1])) for i in range(k-1)]
expected_overlaps=[[4+3*i,5+3*i] for i in range(k-1)]
checks={'seven_degree_four_phases':len(phases)==k,'history_degree_twenty_eight':4*k==28,'connected_overlap_chain':overlaps==expected_overlaps,'generic_component_nonzero':value!=0,'antisymmetric_component_orientation':reversed_value==-value,'determinant_evaluation_avoids_enumeration':elapsed<5}
out={'schema':'marici.nima.seven-phase-coherence-history.v1','phase_labels':[list(q) for q in labels],'phase_degrees':[4]*k,'history_degree':4*k,'shared_coherence_labels':overlaps,'component_labels':[list(x) for x in component_labels],'component_value':str(value),'implicit_assignment_terms':math.factorial(k)**4,'evaluation_seconds':elapsed,'evaluation':'product of four 7x7 determinants','checks':checks,'passed':all(checks.values()),'scope':'Exact selected degree-twenty-eight component of a connected seven-phase history; compositional toy invariant, not a sourced full N7MHV amplitude.'}
p=ROOT/'research/nima/results/seven-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
