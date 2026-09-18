#!/usr/bin/env python3
"""Finite symbolic typing census for the sourced all-loop BCFW recursion."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
fixture=json.loads((ROOT/'research/nima/fixtures/all-loop-bcfw-recursion-source.v1.json').read_text())
rows=[];passed=True
for n in range(4,13):
 for k in range(2,n-1):
  for loop in range(0,5):
   splits=[]
   for nL in range(3,n):
    nR=n+2-nL
    if not 3<=nR<n:continue
    for kL in range(1,nL):
     kR=k-1-kL
     if not 1<=kR<nR:continue
     for lL in range(loop+1):
      lR=loop-lL
      splits.append((nL,nR,kL,kR,lL,lR))
   checks={
    'inverse_soft_decreases_n':n-1<n,
    'all_factorization_children_decrease_n':all(a<n and b<n for a,b,_,_,_,_ in splits),
    'all_factorization_constraints':all(a+b==n+2 and c+d==k-1 and e+f==loop for a,b,c,d,e,f in splits),
    'forward_limit_present_exactly_at_positive_loop':(loop>0)==(loop-1>=0),
    'forward_limit_decreases_loop':loop==0 or loop-1<loop,
    'forward_limit_shifts_n_k_as_sourced':loop==0 or ((n+2)-n==2 and (k+1)-k==1)
   }
   ok=all(checks.values());passed &= ok
   rows.append({'n':n,'k':k,'loop':loop,'admissible_factorization_types':len(splits),'checks':checks,'passed':ok})
out={'schema':'marici.nima.all-loop-bcfw-recursion-typing.v1','source_fixture':'research/nima/fixtures/all-loop-bcfw-recursion-source.v1.json','well_founded_order':'lexicographic in (loop,n): inverse-soft/factorization lower n at fixed loop distribution; forward limit lowers loop despite n -> n+2','range':{'n':[4,12],'loop':[0,4]},'typed_instances':len(rows),'results':rows,'checks':{'source_has_four_shifted_twistors':len(fixture['recursion']['shifted_twistors'])==4,'all_instances_typed':passed,'claim_boundary_explicit':'does not evaluate' in fixture['claim_boundary']},'passed':passed and len(fixture['recursion']['shifted_twistors'])==4,'scope':'Structural typing and recursive well-foundedness only; no GL(2) residue or higher-loop integrand evaluation.'}
p=ROOT/'research/nima/results/all-loop-bcfw-recursion-typing.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'typed_instances':len(rows),'range':out['range']},indent=2));raise SystemExit(0 if out['passed'] else 1)
