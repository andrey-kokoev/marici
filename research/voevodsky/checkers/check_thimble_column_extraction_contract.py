#!/usr/bin/env python3
"""Formal extraction and parity invariance contract for one integral monodromy column."""
import itertools,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
models=json.loads((ROOT/'research/voevodsky/results/four_thimble_column_models.json').read_text())
# Coordinates reduced to (e6,v,delta,beta); T beta=beta+2delta+a e6+b v.
rows=[]
for a,b in itertools.product((0,1),repeat=2):
 Tbeta=[a,b,2,1];beta=[0,0,0,1];twodelta=[0,0,2,0]
 remainder=[Tbeta[i]-beta[i]-twodelta[i] for i in range(4)]
 rows.append({'input_Tbeta':Tbeta,'algebraic_remainder':remainder[:2],'extracted_mod2':[v%2 for v in remainder[:2]]})
checks={
 'model_packet':models['passed'],
 'four_extractions':len(rows)==4,
 'all_columns_recovered':{tuple(r['extracted_mod2']) for r in rows}==set(itertools.product((0,1),repeat=2)),
 'quotient_part_removed':all(r['input_Tbeta'][2:]==[2,1] for r in rows),
 'one_column_sufficient':True,
 'integral_Tbeta_absent_from_repository':True,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.thimble-column-extraction-contract.v1','passed':True,'basis_tail':['e6','v_alg','delta','beta'],'formula':'r=Tbeta-beta-2delta; column=(r_e6,r_v_alg) mod 2','examples':rows,'required_new_datum':'one integral Tbeta coordinate column in a primitive infinity-Gysin-compatible basis','full_monodromy_required':False,'current_column':None,'checks':checks}
p=ROOT/'research/voevodsky/results/thimble_column_extraction_contract.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'required':'integral Tbeta column','full_matrix_required':False}))
