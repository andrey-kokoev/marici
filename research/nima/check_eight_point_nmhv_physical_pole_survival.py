#!/usr/bin/env python3
"""Exact census: every physical eight-point NMHV pole has nonzero residue."""
import itertools,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
N=8;terms=tuple((N,i-1,i,j-1,j) for i in range(2,N-1) for j in range(i+2,N))
def canon(q):return tuple(sorted(q))
def denoms(q):return [canon(q[i+1:]+q[:i]) for i in range(5)]
all_den=sorted(set(q for t in terms for q in denoms(t)))
def physical(q):
 S=set(q);adj=[{i,i%N+1} for i in range(1,N+1)]
 return any(a<=S and b<=S and a.isdisjoint(b) for a in adj for b in adj)
physical_poles=[q for q in all_den if physical(q)]
def check(target):
 e=s.Symbol('epsilon');Z={i:s.Matrix([1,t,t*t,t**3]) for i,t in enumerate(map(s.Integer,(1,2,4,7,11,16,22,29)),1)}
 a,b,c,d=target;r=next(i for i in range(1,N+1) if i not in target);Z[d]=Z[a]+2*Z[b]+3*Z[c]+e*Z[r]
 def br(q):return s.factor(s.det(s.Matrix.hstack(*(Z[i] for i in q))))
 def five(q):
  num={q[p]:br(q[p+1:]+q[:p]) for p in range(5)};den=s.prod(br(q[p+1:]+q[:p]) for p in range(5));return num,s.factor(den)
 data={q:five(q) for q in terms};nonzero=0
 for mono in itertools.product(range(1,N+1),repeat=4):
  residue=s.factor(sum((e*s.prod(data[q][0].get(i,0) for i in mono)/data[q][1]).subs(e,0) for q in terms))
  nonzero+=residue!=0
 return {'divisor':'<'+''.join(map(str,target))+'>=0','nonzero_total_residue_components':nonzero,'coefficients_checked':N**4,'passed':nonzero>0}
runs=[check(q) for q in physical_poles]
checks={'twenty_physical_poles':len(physical_poles)==20,'every_physical_pole_survives':all(r['passed'] for r in runs)}
report={'schema':'marici.nima.eight-point-nmhv-physical-pole-survival.v1','benchmark':{'result':'only physical boundaries survive after summing the eight-point NMHV BCFW triangulation','context':'amplituhedron locality from boundary geometry'},'physical_poles':['<'+''.join(map(str,q))+'>' for q in physical_poles],'runs':runs,'total_grassmann_residues_checked':sum(r['coefficients_checked'] for r in runs),'checks':checks,'passed':all(checks.values()),'scope':'Exact transverse nonvanishing-residue test; this does not yet identify each residue with a normalized product of subamplitudes.'}
out=ROOT/'research/nima/results/eight-point-nmhv-physical-pole-survival.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'physical_poles':len(runs),'residues_checked':report['total_grassmann_residues_checked'],'nonzero_components':[r['nonzero_total_residue_components'] for r in runs]},indent=2));raise SystemExit(0 if report['passed'] else 1)
