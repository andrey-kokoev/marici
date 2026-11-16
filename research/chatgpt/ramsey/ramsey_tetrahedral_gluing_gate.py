"""Exact R(3,3) local gluing obstruction in two 4-vertex tetrahedral windows.
All colors of old K5 and monochromatic exclusions are EXTERNAL Ramsey data.
"""
from itertools import combinations, product
import json
N=5
red={(min(i,(i+1)%N),max(i,(i+1)%N)) for i in range(N)}
blue=set(combinations(range(N),2))-red
assert len(red)==len(blue)==5
R,B=1,0

def e(i,j):return tuple(sorted((i,j)))
def allowed_on(base):
    base=tuple(sorted(base))
    out=[]
    for x in product((0,1),repeat=len(base)):
        c=dict(zip(base,x))
        valid=all(not(c[i]==c[j]==(R if e(i,j) in red else B))
                  for i,j in combinations(base,2))
        if valid:out.append(c)
    return out
window1=(0,1,2)
window2=(1,3,4)
a=allowed_on(window1)
b=allowed_on(window2)
assert len(a)==3 and len(b)==3
assert {x[1] for x in a}=={B}
assert {x[1] for x in b}=={R}
assert not any(x[1]==y[1] for x in a for y in b)
assert allowed_on(range(N))==[]
clause_names=[('R',i,(i+1)%N) for i in range(N)]+[('B',i,(i+2)%N) for i in range(N)]
def sat(clause_indices):
  for assignment in product((B,R),repeat=N):
    if all(not(assignment[clause_names[i][1]]==assignment[clause_names[i][2]]==(R if clause_names[i][0]=='R' else B)) for i in clause_indices):return True
  return False
assert not sat(range(10))
minsize=next(k for k in range(1,11) if any(not sat(xs) for xs in combinations(range(10),k)))
min_cores=[ix for ix in combinations(range(10),minsize) if not sat(ix)]
assert minsize==6 and len(min_cores)==5
horn1={('R',0,1),('R',1,2),('B',0,2)}
horn2={('B',1,3),('B',4,1),('R',3,4)}
def nrm(c):return(c[0],*e(c[1],c[2]))
assert frozenset(nrm(x) for x in horn1|horn2) in {
  frozenset(nrm(clause_names[i]) for i in core) for core in min_cores}
# The two filled tetrahedra share an edge, have acyclic reduced simplicial homology.
vertices=list(range(6)) # base old=0..4, new=5
T1=set([0,1,2,5]);T2=set([1,3,4,5]);
faces={k:sorted({q for tetra in [T1,T2] for r in combinations(sorted(tetra),k+1) for q in [r]}) for k in range(4)}
# Union of two tetrahedra along their common edge is collapsible; compute matrix ranks over Q.
import sympy as s
rank=[]; nullity=[]
for k in range(1,4):
  row={f:i for i,f in enumerate(faces[k-1])};D=s.zeros(len(faces[k-1]),len(faces[k]))
  for j,f in enumerate(faces[k]):
    for i in range(len(f)):
      sub=f[:i]+f[i+1:];D[row[sub],j]+=(-1)**i
  rank.append(D.rank());nullity.append(len(faces[k])-D.rank())
assert len(faces[0])==6 and [len(faces[k]) for k in (1,2,3)]==[11,8,2]
assert rank==[5,6,2]
assert len(faces[1])-rank[0]-rank[1]==0
assert len(faces[2])-rank[1]-rank[2]==0
result={
 'old_red_edges':sorted(list(red)),'old_blue_edges':sorted(list(blue)),
 'two_tetrahedral_windows':[[0,1,2,5],[1,3,4,5]],'intersection_edge':[1,5],
 'per_window_admissible_colorings': [len(a),len(b)],
 'first_window_possible_color_new_to_1':['blue'],
 'second_window_possible_color_new_to_1':['red'],
 'joint_completion_count':0,
 'minimal_unsat_clause_count':minsize,
 'number_smallest_unsat_cores':len(min_cores),
 'topological_simplex_union_face_counts':[len(faces[k]) for k in range(4)],
 'boundary_ranks':[0]+rank,
 'union_homology':{'H0':'Z','H1':'0','H2':'0','H3':'0'},
 'limitation':'Constraints originate in externally supplied two-color Ramsey triangle exclusions, not in Marici native composition.'
}
with open('/mnt/data/ramsey_tetrahedral_gluing_gate_results.json','w') as f:json.dump(result,f,indent=2)
print('PASS: two 4-vertex windows allow 3 assignments each but incompatible on shared edge')
print('PASS: C5 critical extension unsatisfiable, five 6-clause smallest cores')
print('PASS: two tetrahedra along an edge have reduced homology zero')
print(result)
