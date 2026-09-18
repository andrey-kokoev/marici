#!/usr/bin/env python3
"""Exact ten-phase instance of the parameterized coherence-chain family."""
import json,math,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
from coherence_chain_toy import connected_chain
k=10;history,labels,component_labels=connected_chain(k);start=time.perf_counter();value=history.component(component_labels);elapsed=time.perf_counter()-start
reversed_labels=((component_labels[0][1],component_labels[0][0],*component_labels[0][2:]),)+component_labels[1:];reversed_value=history.component(reversed_labels);overlaps=[sorted(set(labels[i])&set(labels[i+1])) for i in range(k-1)];expected=[[4+3*i,5+3*i] for i in range(k-1)]
checks={'ten_degree_four_phases':len(history.phases)==k,'history_degree_forty':4*k==40,'connected_overlap_chain':overlaps==expected,'generic_component_nonzero':value!=0,'antisymmetric_component_orientation':reversed_value==-value,'determinant_evaluation_avoids_enumeration':elapsed<5}
out={'schema':'marici.nima.ten-phase-coherence-history.v1','family':'connected_chain(k)','phase_count':k,'external_labels':3*k+2,'phase_labels':[list(q) for q in labels],'history_degree':4*k,'shared_coherence_labels':overlaps,'component_labels':[list(x) for x in component_labels],'component_value':str(value),'implicit_assignment_terms':math.factorial(k)**4,'evaluation_seconds':elapsed,'evaluation':'product of four 10x10 determinants','checks':checks,'passed':all(checks.values()),'scope':'Exact selected degree-forty component of the parameterized connected ten-phase toy; not a sourced full N10MHV amplitude.'}
p=ROOT/'research/nima/results/ten-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
