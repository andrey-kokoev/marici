"""SymPy producer; the separate verifier has its own rational matrix engine."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
problem={'name':'commuting-dual-number-fixture-v1','field':'Q',
 'algebra':'Q[t]/(t^2), commuting left and right actions',
 'depth_ideal':'J=(t_left,t_right) in the enveloping algebra',
 'dimensions':{'E':5,'O':2,'A':3,'B':1,'G':2},
 'source_maps':'fixed i:B->A, q:A->G; identity source comparisons',
 'scope':'finite structural fixture, not a physical observer identification'}
l=s.zeros(5);r=s.zeros(5);l[1,0]=l[3,2]=1;r[2,0]=r[3,1]=r[3,4]=1
pi=s.eye(5)[:2,:];ol=s.Matrix([[0,0],[1,0]]);orr=s.zeros(2)
e=s.eye(5);i=s.Matrix([[0],[0],[1]])
D1=s.diag(1,1,2,3,5);D2=s.diag(2,3,5,7,11)
C1=s.eye(2);C2=s.diag(13,17)
gains={'00':(s.eye(5),s.eye(2)),'10':(D1,C1),'01':(D2,C2),'11':(D2*D1,C2*C1)}
def enc(m):return [[str(x) for x in row] for row in m.tolist()]
nodes={}
for name,(D,C) in gains.items():
    f=D*e[:,[3]]
    mats={'D':D,'C':C,'left':D*l*D.inv(),'right':D*r*D.inv(),
      'lower_left':C*ol*C.inv(),'lower_right':C*orr*C.inv(),'pi':C*pi*D.inv(),
      'K':D*e[:,[2,3,4]],'M':D*e[:,[1,2,3]],'N':D*e[:,[2,3]],'L':f,
      'f':f,'H':D*e[:,[4,2,3]],'private':s.Matrix([[0,0,0,1,0]])*D.inv(),
      'graph':f.col_join(-i)}
    nodes[name]={key:enc(m) for key,m in mats.items()}
edges={}
for a,b in [('00','10'),('00','01'),('10','11'),('01','11')]:
    D,C=gains[a];DD,CC=gains[b];U=DD*D.inv();V=CC*C.inv()
    edges[a+'-'+b]={'upper':enc(U),'lower':enc(V),'pushout':enc(s.diag(U,s.eye(3)))}
bundle={'schema':'structural-gain-square-v1','problem':problem,
 'problem_sha256':hashlib.sha256(json.dumps(problem,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'nodes':nodes,'edges':edges}
out=ROOT/'research/voevodsky/results/structural-gain-square.json'
out.write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')
print(str(out))
