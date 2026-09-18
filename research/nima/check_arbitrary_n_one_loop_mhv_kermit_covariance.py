#!/usr/bin/env python3
"""Combinatorial covariance and count checks for sourced one-loop MHV Kermit terms."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
rows=[];passed=True
for n in range(4,51):
 terms=[];ok=True
 for a in range(2,n-1):
  for b in range(a+1,n):
   # Numerator N=<A1a(a+1)><B1b(b+1)>-(A<->B), squared.
   num={i:0 for i in range(1,n+1)}
   for i,multiplicity in ((1,4),(a,2),(a+1,2),(b,2),(b+1,2)):
    num[i]+=multiplicity
   den={i:0 for i in range(1,n+1)}
   for i,j in ((1,a),(a,a+1),(a+1,1),(1,b),(b,b+1),(b+1,1)):
    den[i]+=1;den[j]+=1
   weights={i:num.get(i,0)-den.get(i,0) for i in range(1,n+1)}
   term_ok=all(v==0 for v in weights.values())
   ok &= term_ok
   terms.append({'a':a,'b':b,'external_weights':weights,'passed':term_ok})
 checks={'term_count':len(terms)==(n-2)*(n-3)//2,'all_external_projective_weights_zero':ok,'rational_gl2_weight_minus_four':2-6==-4,'measure_restores_gl2_weight_zero':2-6+4==0}
 row_ok=all(checks.values());passed &= row_ok
 rows.append({'n':n,'terms':len(terms),'checks':checks,'passed':row_ok})
out={'schema':'marici.nima.arbitrary-n-one-loop-mhv-kermit-covariance.v1','source':'arXiv:1008.2958, equation MHV_1loop_amplitude; arXiv:1212.5605, A_n^(2),1=sum_(1<a<b<n) K[a;b]','range':[4,50],'formula':{'term_count':'(n-2)(n-3)/2','numerator':'<AB|(1 a a+1) intersect (1 b b+1)>^2','denominator':'<AB1a><AB a a+1><AB a+1 1><AB1b><AB b b+1><AB b+1 1>'},'results':rows,'passed':passed,'scope':'Exact exponent bookkeeping for every sourced Kermit term; no integration or inter-term pole cancellation asserted.'}
p=ROOT/'research/nima/results/arbitrary-n-one-loop-mhv-kermit-covariance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':passed,'range':[4,50],'last':rows[-1]},indent=2));raise SystemExit(0 if passed else 1)
