#!/usr/bin/env python3
"""Exact twenty-phase scalability test of the coherence-chain family."""
import json,math,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
from coherence_chain_toy import connected_chain
k=20;build_start=time.perf_counter();history,labels,component_labels=connected_chain(k);build_seconds=time.perf_counter()-build_start
start=time.perf_counter();value=history.component(component_labels);elapsed=time.perf_counter()-start
reversed_labels=((component_labels[0][1],component_labels[0][0],*component_labels[0][2:]),)+component_labels[1:];reversed_value=history.component(reversed_labels);overlaps=[sorted(set(labels[i])&set(labels[i+1])) for i in range(k-1)];expected=[[4+3*i,5+3*i] for i in range(k-1)]
checks={'twenty_degree_four_phases':len(history.phases)==k,'history_degree_eighty':4*k==80,'connected_overlap_chain':overlaps==expected,'generic_component_nonzero':value!=0,'antisymmetric_component_orientation':reversed_value==-value,'determinant_evaluation_scales':elapsed<10}
out={'schema':'marici.nima.twenty-phase-coherence-history.v1','family':'connected_chain(k)','phase_count':k,'external_labels':3*k+2,'history_degree':4*k,'overlap_count':len(overlaps),'component_value':str(value),'component_numerator_digits':len(str(abs(value.p))),'component_denominator_digits':len(str(value.q)),'implicit_assignment_terms':math.factorial(k)**4,'build_seconds':build_seconds,'evaluation_seconds':elapsed,'evaluation':'product of four 20x20 determinants','checks':checks,'passed':all(checks.values()),'scope':'Exact selected degree-eighty component and scalability test of the connected twenty-phase toy; not a sourced full N20MHV amplitude.'}
p=ROOT/'research/nima/results/twenty-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'component_value':'<stored in result; omitted from console>'},indent=2));raise SystemExit(0 if out['passed'] else 1)
