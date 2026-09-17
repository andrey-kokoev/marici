#!/usr/bin/env python3
"""Exact cancellation of every spurious pole in seven-point NMHV BCFW."""
import itertools,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
N=7; terms=tuple((N,i-1,i,j-1,j) for i in range(2,N-1) for j in range(i+2,N))
def canonical(q):
 # Sorting a four-bracket contributes the permutation sign.
 inv=sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))
 return tuple(sorted(q)),(-1)**inv
def denominator_brackets(q):
 return [canonical(q[i+1:]+q[:i])[0] for i in range(5)]
counts=Counter(d for q in terms for d in denominator_brackets(q))
def physical(q):
 S=set(q);pairs=[{i,i%N+1} for i in range(1,N+1)]
 return any(p<=S and r<=S and p.isdisjoint(r) for p in pairs for r in pairs)
spurious=sorted(q for q,k in counts.items() if k>1 and not physical(q))

def check_divisor(target):
 e=s.Symbol('epsilon');base={i:s.Matrix([1,s.Integer(t),s.Integer(t)**2,s.Integer(t)**3]) for i,t in enumerate((1,2,4,7,11,16,22),1)}
 a,b,c,d=target;r=next(i for i in range(1,N+1) if i not in target);base[d]=base[a]+2*base[b]+3*base[c]+e*base[r]
 def br(q):return s.factor(s.det(s.Matrix.hstack(*(base[i] for i in q))))
 def five(q):
  out={}
  for pos,label in enumerate(q):
   rest=q[pos+1:]+q[:pos];out[label]=br(rest)
  den=s.prod(br(q[i+1:]+q[:i]) for i in range(5));return out,s.factor(den)
 data={q:five(q) for q in terms};bad=[];nonzero=0
 for mono in itertools.product(range(1,N+1),repeat=4):
  residues=[]
  for q in terms:
   num,den=data[q];residues.append(s.factor((e*s.prod(num.get(i,0) for i in mono)/den).subs(e,0)))
  nonzero+=any(v!=0 for v in residues)
  total=s.factor(sum(residues))
  if total!=0:bad.append({'monomial':list(mono),'residue':str(total)})
 return {'divisor':'<'+''.join(map(str,target))+'>=0','occurrences':counts[target],'coefficients_checked':N**4,'nonzero_individual_residues':nonzero,'failure_count':len(bad),'failures':bad[:10],'passed':nonzero>0 and not bad}
runs=[check_divisor(q) for q in spurious]
checks={'shared_spurious_divisors_found':len(spurious)>0,'all_residues_cancel':all(r['passed'] for r in runs)}
report={'schema':'marici.nima.seven-point-nmhv-all-spurious-poles.v1','benchmark':{'result':'complete cancellation of internal BCFW boundaries for the seven-point NMHV tree amplitude','context':'positive Grassmannian/amplituhedron triangulation'},'bcfw_terms':['['+''.join(map(str,q))+']' for q in terms],'runs':runs,'total_grassmann_residues_checked':sum(r['coefficients_checked'] for r in runs),'checks':checks,'passed':all(checks.values()),'scope':'Exact transverse residue checks for every shared nonphysical four-bracket divisor of the seven-point BCFW representation.'}
out=ROOT/'research/nima/results/seven-point-nmhv-all-spurious-poles.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'divisors':[r['divisor'] for r in runs],'residues_checked':report['total_grassmann_residues_checked'],'failures':sum(r['failure_count'] for r in runs)},indent=2));raise SystemExit(0 if report['passed'] else 1)
