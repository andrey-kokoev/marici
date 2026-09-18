#!/usr/bin/env python3
"""Exact hundred-phase scalability test of the coherence-chain family."""
import hashlib,json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
from coherence_chain_toy import connected_chain
k=100;build_start=time.perf_counter();history,labels,component_labels=connected_chain(k);build_seconds=time.perf_counter()-build_start
start=time.perf_counter();value=history.component(component_labels);elapsed=time.perf_counter()-start
reversed_labels=((component_labels[0][1],component_labels[0][0],*component_labels[0][2:]),)+component_labels[1:];reversed_value=history.component(reversed_labels);overlaps=[sorted(set(labels[i])&set(labels[i+1])) for i in range(k-1)];expected=[[4+3*i,5+3*i] for i in range(k-1)]
num=str(abs(value.p));den=str(value.q);digest=hashlib.sha256((str(value.p)+'/'+den).encode()).hexdigest()
checks={'hundred_degree_four_phases':len(history.phases)==k,'history_degree_four_hundred':4*k==400,'connected_overlap_chain':overlaps==expected,'generic_component_nonzero':value!=0,'antisymmetric_component_orientation':reversed_value==-value,'determinant_evaluation_scales':elapsed<30}
out={'schema':'marici.nima.hundred-phase-coherence-history.v1','family':'connected_chain(k)','phase_count':k,'external_labels':3*k+2,'history_degree':4*k,'overlap_count':len(overlaps),'component_numerator_digits':len(num),'component_denominator_digits':len(den),'component_sha256':digest,'implicit_assignment_decimal_digits':len(str(math.factorial(k)**4)),'build_seconds':build_seconds,'evaluation_seconds':elapsed,'evaluation':'product of four 100x100 exact determinants','checks':checks,'passed':all(checks.values()),'scope':'Exact selected degree-400 component and scalability test of the connected hundred-phase toy; digest records the exact rational compactly; not a sourced full N100MHV amplitude.'}
p=ROOT/'research/nima/results/hundred-phase-coherence-history.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
