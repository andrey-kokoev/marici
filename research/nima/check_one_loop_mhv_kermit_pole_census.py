#!/usr/bin/env python3
"""Exact generic-kinematics pole census for one-loop MHV Kermit sums."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
t=s.symbols('t')
def det4(cols):return s.det(s.Matrix.hstack(*cols))
def run(n,seed):
 # Generic rational external data, not restricted to positivity.
 xs=[s.Integer(i*i+seed*i+1) for i in range(1,n+1)]
 Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
 A=s.Matrix([2+seed,3,5,7]);B0=s.Matrix([11,13+seed,17,19]);V=s.Matrix([23,29,31+seed,37])
 B=B0+t*V
 def ab(i,j):return s.expand(det4((A,B,Z[i],Z[j])))
 def num(a,b):
  return s.expand(det4((A,Z[1],Z[a],Z[a+1]))*det4((B,Z[1],Z[b],Z[b+1]))-det4((B,Z[1],Z[a],Z[a+1]))*det4((A,Z[1],Z[b],Z[b+1])))
 terms=[]
 for a in range(2,n-1):
  for b in range(a+1,n):
   ds=(ab(1,a),ab(a,a+1),ab(a+1,1),ab(1,b),ab(b,b+1),ab(b+1,1))
   terms.append((a,b,s.cancel(num(a,b)**2/s.prod(ds)),ds))
 def residue(i,j):
  p=ab(i,j);root=s.solve(p,t)[0];total=s.Integer(0);individuals=[]
  for a,b,f,ds in terms:
   multiplicity=sum(s.factor(q-p)==0 or s.factor(q+p)==0 for q in ds)
   if multiplicity:
    individual=s.factor(s.limit((t-root)*f,t,root))
    if individual!=0:individuals.append((a,b,individual))
    total += individual
  return individuals,s.factor(total)
 def opposite_pairing(values):
  unused=list(values);pairs=[]
  while unused:
   a,b,r=unused.pop(0);hit=next((q for q,x in enumerate(unused) if s.factor(x[2]+r)==0),None)
   if hit is None:return False,pairs
   c,d,q=unused.pop(hit);pairs.append(((a,b),(c,d)))
  return True,pairs
 sp=[];ph=[];ok=True
 for k in range(3,n):
  vals,r=residue(1,k);paired,pairs=opposite_pairing(vals)
  expected={tuple(sorted(((min(k-1,q),max(k-1,q)),(min(k,q),max(k,q))))) for q in range(2,n) if q not in (k-1,k)}
  observed={tuple(sorted(pair)) for pair in pairs};involution=paired and observed==expected
  good=r==0 and involution;ok &= good;sp.append({'pole':f'<AB1{k}>','singular_terms':len(vals),'residue':str(r),'cancelled':r==0,'pairwise_opposite':paired,'expected_involution':involution,'pairs':pairs})
 for i,j in [(1,2)]+[(k,k+1) for k in range(2,n)]+[(n,1)]:
  vals,r=residue(i,j);incidence=len(vals)==n-3;good=incidence and r!=0;ok &= good;ph.append({'pole':f'<AB{i}{j}>','singular_terms':len(vals),'expected_incidence_n_minus_3':incidence,'residue_nonzero':r!=0,'survives':good})
 return {'n':n,'seed':seed,'terms':len(terms),'spurious':sp,'physical':ph,'passed':ok}
rows=[run(n,seed) for n,seed in ((5,1),(6,2),(7,3),(8,4))]
out={'schema':'marici.nima.one-loop-mhv-kermit-pole-census.v1','fixtures':'exact rational generic momentum twistors and affine loop-line pencils','results':rows,'checks':{'all_anchor_spurious_residues_cancel':all(x['cancelled'] for r in rows for x in r['spurious']),'all_spurious_residues_follow_expected_involution':all(x['expected_involution'] for r in rows for x in r['spurious']),'all_physical_residues_have_incidence_n_minus_3':all(x['expected_incidence_n_minus_3'] for r in rows for x in r['physical']),'all_physical_residues_survive':all(x['survives'] for r in rows for x in r['physical'])},'passed':all(r['passed'] for r in rows),'scope':'Exact generic one-parameter residues through eight points; finite evidence, not an arbitrary-n proof.'}
p=ROOT/'research/nima/results/one-loop-mhv-kermit-pole-census.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'rows':[{'n':r['n'],'terms':r['terms'],'spurious':[(x['pole'],x['singular_terms'],x['cancelled'],x['pairwise_opposite']) for x in r['spurious']],'physical_survive':all(x['survives'] for x in r['physical'])} for r in rows]},indent=2));raise SystemExit(0 if out['passed'] else 1)
