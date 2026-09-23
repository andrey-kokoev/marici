"""Exact one-parameter CZ fibres on all triple-parallel n=7 compiled cells."""
import json,itertools
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima';cells=json.loads((N/'results/seven-point-positroid-compiler.json').read_text())['cells']
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)]);kernel=Z.T.nullspace()[0];assert list(kernel)==[1,-6,15,-20,15,-6,1]
def minor(C,i,j):return s.det(C[:,[i,j]])
scenarios=[(1,[0,1,1,1,2,3,4],[1]*7,(2,3,4)),
 (3,[0,0,1,2,3,4,0],[1,1,1,1,1,1,-1],(7,1,2)),
 (5,[0,1,2,3,3,3,4],[1]*7,(4,5,6))]
rows=[]
for index,t,w,labels in scenarios:
 C=s.Matrix([[x for x in w],[w[i]*t[i] for i in range(7)]])
 d=C[:,labels[0]-1];assert all(minor(C,labels[0]-1,j-1)==0 for j in labels[1:])
 h=s.symbols('h');D=C+h*d*kernel.T
 assert D*Z==C*Z and D!=C
 assert all(s.factor(minor(D,i-1,j-1))==0 for i,j in itertools.combinations(labels,2))
 base=[(i+1,j+1) for i,j in itertools.combinations(range(7),2) if minor(C,i,j)==0]
 assert all(minor(C,i,j)>0 for i,j in itertools.combinations(range(7),2) if (i+1,j+1) not in base)
 witness=D.subs(h,s.Rational(1,10000))
 assert all(minor(witness,i,j)>0 for i,j in itertools.combinations(range(7),2) if (i+1,j+1) not in base)
 assert {p for p in itertools.combinations(range(1,8),2) if minor(witness,p[0]-1,p[1]-1)==0}==set(base)
 claimed=[int(x.split('(')[1].split(',')[0]) for x in cells[index]['vanishing_cyclic_minors']]
 assert all((i,(i%7)+1) in base or ((i%7)+1,i) in base for i in claimed)
 rows.append({'history_index':index,'parallel_triple':list(labels),'zero_ordered_minors':list(map(list,base)),
  'source_matrices_distinct':True,'same_CZ':True,'positive_fibre_perturbation':'1/10000',
  'interior_source_positivity_retained':True,'fibre_direction':[[str((d*kernel.T)[i,j]) for j in range(7)] for i in range(2)]})
report={'schema':'marici.nima.seven-point-triple-fibre-obstruction.v1','rows':rows,
 'theorem':'If three source columns are parallel and the external data have a nonzero left-kernel vector k, adding h*d*k^T with d their common column direction preserves their parallelism and CZ. At an interior cell point small nonzero h preserves every strictly positive minor. Thus CZ has a nontrivial fibre on each triple-parallel cell, so its differential rank is at most 7 wherever that fibre persists; it cannot be a locally invertible 8-dimensional positive geometry chart.',
 'claim_boundary':'This refutes identifying these three compiled rank tables as individually full-dimensional image charts for the fixed positive Z; it does not refute the independently checked rational-kinematics history/superamplitude matches.'}
(N/'results/seven-point-triple-fibre-obstruction.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'triple_cells':[r['history_index'] for r in rows]},indent=2))
