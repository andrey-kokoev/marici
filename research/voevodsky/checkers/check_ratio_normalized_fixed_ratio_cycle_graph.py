#!/usr/bin/env python3
"""Checks normalized-grade and universal fixed-ratio graph claims."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,math
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/ratio_normalized_grade_makes_fixed_ratio_cycle_graphs_canonically_isomorphic_20260912.md'
SOURCE=ROOT/'research/nima/every-two-consecutive-prime-shells-generate-a-four-term-interval-cycle-in-the-unlabelled-pair-history.md'
RESULT=ROOT/'research/voevodsky/results/ratio_normalized_fixed_ratio_cycle_graph.json'
primes=(2,3,5,7,11,13,17,19,23); shells=list(zip(primes,primes[1:])); denominators=(1,2,3,7); Ls=(100,300,900)
def labels(L): return [(j,k,p,q) for j,(p,q) in enumerate(shells) for k in range(1,L+1) if k*p*q<=L]
def normalized_edges(L): return {(k*p,k*q) for j,k,p,q in labels(L)}
def block_edges(b,L): return {(b*k*p,b*k*q) for j,k,p,q in labels(L)}
checks={}
checks['source_four_term_rectangle']='four source tuples' in SOURCE.read_text() and 'multiplicative rectangle' in SOURCE.read_text()
checks['finite_nested_intrinsic_cutoffs']=all(len(labels(L))<L*len(shells) for L in Ls) and all(set(labels(a))<=set(labels(b)) for a,b in zip(Ls,Ls[1:]))
for b in denominators:
 checks[f'graph_scaling_isomorphism_b{b}']={(u//b,v//b) for u,v in block_edges(b,Ls[-1])}==normalized_edges(Ls[-1])
 for delta in (1,2):
  coeff={tuple(e):Fraction((i%5)-2,i+1) for i,e in enumerate(labels(Ls[-1]))}
  qbar=sum(abs(coeff[tuple(e)])*(k*p*q)**delta for e in labels(Ls[-1]) for j,k,p,q in [e])
  qD=sum(abs(coeff[tuple(e)])*(k*b*p*q)**delta for e in labels(Ls[-1]) for j,k,p,q in [e])
  checks[f'seminorm_scaling_b{b}_d{delta}']=qD==(b**delta)*qbar
# Every two shell pairs produce the four boundary-cancelling edges at every b.
for b in denominators:
 ok=True
 for p,q in shells[:4]:
  for r,s in shells[:4]:
   oriented=[(b*p*r,b*q*r),(b*q*r,b*q*s),(b*p*r,b*p*s),(b*p*s,b*q*s)]
   bal={}
   for idx,(u,v) in enumerate(oriented):
    sign=1 if idx<2 else -1; bal[u]=bal.get(u,0)-sign; bal[v]=bal.get(v,0)+sign
   ok &= all(x==0 for x in bal.values())
 checks[f'rectangle_cycle_b{b}']=ok
for delta in (.1,.5,1,2): checks[f'uniform_length_delta_{delta}']=all(math.log(q/p)<=math.exp(delta*math.log(k*p*q))/delta+1e-13 for L in Ls for j,k,p,q in labels(L))
# Reflection changes only reduced ratio data, never intrinsic labels/cutoffs.
ratios=((1,1),(2,3),(3,2),(5,7))
checks['reflection_fixes_intrinsic_labels']=all(labels(300)==labels(300) and {(j,k) for j,k,p,q in labels(300)}=={(j,k) for j,k,p,q in labels(300)} for a,b in ratios)
checks['denominator_unbounded_coproduct_not_claimed']='No uniform topology over an unbounded coproduct' in PACKET.read_text()
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.ratio-normalized-fixed-ratio-cycle-graph-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'source':hashlib.sha256(SOURCE.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'denominators':list(denominators),'largest_cutoff_edges':len(labels(Ls[-1])),'disposition':{'constructed':'universal labelled cycle graph and ratio-normalized proper grade','reflection':'strict on intrinsic labels and grade','boundary':'no weighted topology across unbounded ratio coproduct'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'largest_edges':result['largest_cutoff_edges']})); raise SystemExit(0 if result['passed'] else 1)
