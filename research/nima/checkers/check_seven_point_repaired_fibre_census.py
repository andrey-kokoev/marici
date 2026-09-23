"""Exact membership census for six repaired n=7 image cells at positive top-cell targets."""
import itertools,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
original=json.loads((N/'results/seven-point-positroid-compiler.json').read_text())['cells'];repair=json.loads((N/'results/seven-point-zero-column-repair.json').read_text())
assert [r['history_index'] for r in repair['rows']]==[1,3,5]
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)]);R=(Z.T*Z).inv()*Z.T;k=Z.T.nullspace()[0];a,b=s.symbols('a b')
def delta(M,i,j):return s.det(M[:,[i,j]])
def signs(D):
 values={(i+1,j+1):delta(D,i,j) for i,j in itertools.combinations(range(7),2)}
 return {'negative':[list(p) for p,x in values.items() if x<0], 'zero':[list(p) for p,x in values.items() if x==0],
         'positive':sum(1 for x in values.values() if x>0)}
def member(Y,index):
 if index in (1,3,5):
  deleted={1:3,3:1,5:5}[index]-1;kept=[j for j in range(7) if j!=deleted];Q=Y*Z.extract(kept,list(range(6))).inv();D=s.zeros(2,7)
  for r,j in enumerate(kept):D[:,j]=Q[:,r]
 else:
  D0=Y*R;D=D0+s.Matrix([[a*x for x in k],[b*x for x in k]])
  edges=[int(x.split('(')[1].split(',')[0])-1 for x in original[index]['vanishing_cyclic_minors']]
  eq=[delta(D,j,(j+1)%7) for j in edges];L=s.Matrix([[s.diff(e,z) for z in (a,b)] for e in eq]);assert L.det()!=0
  rhs=-s.Matrix([e.subs({a:0,b:0}) for e in eq]);solution=L.inv()*rhs;D=D.subs({a:solution[0],b:solution[1]})
 assert D*Z==Y
 info=signs(D)
 expected={tuple(p) for p in info['zero']}
 if index in (1,3,5):
  deleted={1:3,3:1,5:5}[index];goodzeros={(i,deleted) if i<deleted else (deleted,i) for i in range(1,8) if i!=deleted}
 else:
  edge={tuple(sorted((j+1,(j+1)%7+1))) for j in edges};goodzeros=edge
 return {'history_index':index,'inside':not info['negative'] and expected==goodzeros,
         'negative_minors':len(info['negative']),'zero_minors':len(expected)}
seeds=[([1]*7,list(range(7))),([1,2,3,2,1,3,2],[0,1,3,4,7,9,12]),([2,1,2,3,1,2,4],[0,2,4,5,8,11,15])]
rows=[]
for w,t in seeds:
 C=s.Matrix([w,[w[i]*t[i] for i in range(7)]])
 assert all(delta(C,i,j)>0 for i,j in itertools.combinations(range(7),2))
 Y=C*Z;members=[member(Y,i) for i in range(6)];rows.append({'source_weights':w,'source_slopes':t,'members':members,
  'positive_image_count':sum(1 for x in members if x['inside'])})
# Also probe the six candidate image interiors rather than only the sector
# selected by three generic monotone top-cell sources.
cellrows=[]
for index in range(6):
 if index in (1,3,5):
  deleted={1:3,3:1,5:5}[index]-1;C=s.zeros(2,7)
  for rank,j in enumerate(q for q in range(7) if q!=deleted):C[:,j]=s.Matrix([1,rank])
 else:
  slopes={0:[0,1,1,2,3,3,4],2:[4,0,1,1,2,3,4],4:[4,0,1,2,3,3,4]}[index]
  C=s.Matrix([[(-1 if j==0 and index in (2,4) else 1) for j in range(7)],
    [slopes[j]*(-1 if j==0 and index in (2,4) else 1) for j in range(7)]])
 assert not signs(C)['negative']
 Y=C*Z;members=[member(Y,i) for i in range(6)]
 assert members[index]['inside']
 cellrows.append({'seed_cell':index,'members':members,'positive_image_count':sum(1 for x in members if x['inside'])})
report={'schema':'marici.nima.seven-point-repaired-fibre-census.v1','rows':rows,'cell_seed_rows':cellrows,
 'scope':'Three exact interior target samples from positive top-cell sources. Counts are neither a coverage proof nor a form comparison. An interior count zero or greater than one would falsify naive single-sheet triangulation at that sample.'}
(N/'results/seven-point-repaired-fibre-census.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'top_source_counts':[r['positive_image_count'] for r in rows],
 'candidate_source_counts':[r['positive_image_count'] for r in cellrows],
 'candidate_source_members':[[x['history_index'] for x in r['members'] if x['inside']] for r in cellrows]},indent=2))
