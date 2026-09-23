"""Exact fibre test of the six compiled n=7 rank-two charts at one positive Z."""
from pathlib import Path
from fractions import Fraction as Q
import json,itertools
from sympy import Matrix, symbols, solve, Rational
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
cells=json.loads((N/'results/seven-point-positroid-compiler.json').read_text())['cells'];chart=json.loads((N/'results/seven-point-positive-chart.json').read_text());assert chart['history_index']==0
Z=Matrix([[j**k for k in range(6)] for j in range(1,8)]);null=Z.T.nullspace();assert len(null)==1
k=null[0];assert k[0]==1

def minor(C,i,j):return C[0,i]*C[1,j]-C[0,j]*C[1,i]
def constraints(cell):return [int(x.split('(')[1].split(',')[0])-1 for x in cell['vanishing_cyclic_minors']]
def test(weights,u,v):
 t=[0,1,1,2,u,u,v];C=Matrix([[weights[i] for i in range(7)],[weights[i]*t[i] for i in range(7)]])
 assert all(minor(C,i,j)>0 for i in range(7) for j in range(i+1,7) if (i,j) not in ((1,2),(4,5)))
 a,b=symbols('a b');D=C+Matrix([[a*x for x in k],[b*x for x in k]])
 result=[]
 for cell in cells:
  edges=constraints(cell);eq=[minor(D,i,(i+1)%7) for i in edges]
  sol=solve(eq,[a,b],dict=True)
  if len(sol)!=1 or a not in sol[0] or b not in sol[0]:result.append({'history_index':cell['history_index'],'status':'DEGENERATE_SYSTEM'});continue
  E=D.subs(sol[0]);ms=[minor(E,i,j) for i in range(7) for j in range(i+1,7)]
  # Rank-two nonnegative Grassmannian means all ordered minors >=0,
  # irrespective of row gauge; D preserves the orientation of CZ.
  signs={1 if x>0 else -1 for x in ms if x!=0}
  status='POSITIVE_CELL' if len(signs)==1 and {p for p in itertools.combinations(range(7),2) if minor(E,*p)==0}=={(i,(i+1)%7) if i<6 else (0,6) for i in edges} else 'OUTSIDE_POSITIVE_CELL'
  result.append({'history_index':cell['history_index'],'status':status,'kernel_shift':[str(sol[0][a]),str(sol[0][b])],
   'negative_ordered_minors':[[i+1,j+1] for i,j in itertools.combinations(range(7),2) if minor(E,i,j)<0],
   'zero_ordered_minors':[[i+1,j+1] for i,j in itertools.combinations(range(7),2) if minor(E,i,j)==0]})
 return result
samples=[([1]*7,3,4),([1,2,3,2,1,3,2],4,6)]
rows=[]
for w,u,v in samples:
 r=test(w,u,v);assert r[0]['status']=='POSITIVE_CELL';rows.append({'weights':w,'u':u,'v':v,'candidate_fibres':r})
report={'schema':'marici.nima.seven-point-chart-overlap.v1','external_Z':'moment curve j=1..7 powers 0..5',
 'source_fibre_kernel':list(map(str,k)),'samples':rows,
 'scope':'Exact two source fibre tests only. A positive competing-cell lift proves local target overlap; failure at samples does not prove global disjointness.'}
p=N/'results/seven-point-chart-overlap.json';p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'samples':[[{'history':x['history_index'],'status':x['status'],'negative':len(x.get('negative_ordered_minors',[]))} for x in row['candidate_fibres']] for row in rows]},indent=2))
