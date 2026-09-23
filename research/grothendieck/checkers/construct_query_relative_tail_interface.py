"""Compile a query-relative interface from the owning ternary tail carrier."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,subprocess,sys
import query_relative_tail_geometry as g
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subprocess.run([sys.executable,str(HERE/'verify_ternary_tail_budget_dpc.py')],check=True)
source_path=R/'ternary-tail-budget-dpc.json';source=load(source_path)
caps=list(map(Q,source['atom_capacity_upper']));budget=list(map(Q,source['prefix_budget_upper']));c=[Q(w['lower']) for w in source['weights']]
# Freeze the language and representation before constructing the quotient.
contract={'schema':'query-relative-tail-interface.v1','source_sha256':sha(source_path),'observables':['S=x1+x2+x3','F=sum c_i*x_i, with c_i the owning rational lower kernel bounds'],'future_language':'arbitrary finite sequences of rational closed halfspaces a*S+b*F<=d; observe feasibility and linear extremal values in (S,F)','representation':'exact convex polygon with rational source lifts at vertices; retained size may grow with queries','excluded_queries':['individual-bin predicates not factoring through (S,F)','marked historical cuts','actual-source selection'],'query_scenarios':['compatible-refinement','separately-feasible-inconsistent-chain'],'scope':'Owning Chebyshev moment relaxation; no new actual-prime or midpoint verdict.'}
cp=R/'query-relative-tail-interface-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
A=[];b=[]
for i in range(3):A.append([Q(-int(i==j)) for j in range(3)]);b.append(Q(0))
for i in range(3):A.append([Q(int(i==j)) for j in range(3)]);b.append(caps[i])
for i in range(3):A.append([Q(int(j<=i)) for j in range(3)]);b.append(budget[i])
poly=g.project(A,b,c);assert len(poly)>=3
halfspaces=g.facets(poly)
def pack(poly):return [{'observable':list(map(str,z)),'source_lift':list(map(str,x))} for z,x in poly]
def query(row,bound):return {'coefficients':list(map(str,row)),'upper':str(bound)}
B=budget[-1];v=Q(source['full_LP']['value'])
sequences={'compatible-refinement':[((Q(-1),Q(0)),-B/2),((Q(0),Q(1)),v/2),((Q(1),Q(0)),3*B/4)],'separately-feasible-inconsistent-chain':[((Q(1),Q(0)),B/4),((Q(-1),Q(0)),-B/2)]}
traces={}
for name,frames in sequences.items():
 current=poly;AA=list(A);bb=list(b);trace=[]
 for row,bound in frames:
  current=g.clip(current,row,bound)
  AA.append([row[0]+row[1]*w for w in c]);bb.append(bound)
  direct=g.project(AA,bb,c)
  assert [z for z,_ in current]==[z for z,_ in direct]
  trace.append({'frame':query(row,bound),'polygon':pack(current),'direct_source_vertices':len(g.vertices(AA,bb))})
 traces[name]=trace
assert traces['compatible-refinement'][-1]['polygon']
assert not traces['separately-feasible-inconsistent-chain'][-1]['polygon']
assert all(g.clip(poly,*frame) for frame in sequences['separately-feasible-inconsistent-chain'])
# Every facet has a private violating point satisfying all remaining facets.
# The singleton query at this point separates the full and facet-forgetting
# representations; rational equality is encoded by opposing halfspaces.
facet_witnesses=[]
for i,((normal,bound),(p,_),(q,_)) in enumerate(zip(halfspaces,poly,poly[1:]+poly[:1])):
 mid=tuple((a+b)/2 for a,b in zip(p,q));direction=normal
 eps=Q(1)
 for j,(n,d) in enumerate(halfspaces):
  if j==i:continue
  slack=d-sum(a*z for a,z in zip(n,mid));slope=sum(a*z for a,z in zip(n,direction));assert slack>0
  if slope>0:eps=min(eps,slack/(2*slope))
 witness=tuple(z+eps*a for z,a in zip(mid,direction))
 assert sum(a*z for a,z in zip(normal,witness))>bound
 assert all(sum(a*z for a,z in zip(n,witness))<=d for j,(n,d) in enumerate(halfspaces) if i!=j)
 facet_witnesses.append(list(map(str,witness)))
# Rectangular marginal ranges fabricate a joint observable point.
rectangle_false=(Q(0),v)
assert all(min(z[j] for z,_ in poly)<=rectangle_false[j]<=max(z[j] for z,_ in poly) for j in (0,1))
assert any(sum(a*z for a,z in zip(n,rectangle_false))>d for n,d in halfspaces)
# New bin-level queries require a lift: same S,F can hide different x1.
ker=(c[1]-c[2],c[2]-c[0],c[0]-c[1]);assert ker[0]!=0
scale=Q(100)/max(map(abs,ker));delta=tuple(scale*a for a in ker)
p=tuple(Q(1000)+d for d in delta);q=tuple(Q(1000)-d for d in delta)
assert g.image(p,c)==g.image(q,c)
assert all(sum(a*z for a,z in zip(row,w))<=d for w in (p,q) for row,d in zip(A,b))
assert (p[0]<=1000)!=(q[0]<=1000)
out={'schema':'query-relative-tail-interface-result.v1','contract_sha256':sha(cp),'source_constraints':{'A':[[str(v) for v in row] for row in A],'b':list(map(str,b))},'objective_coefficients':list(map(str,c)),'initial_polygon':pack(poly),'facets':[query(n,d) for n,d in halfspaces],'facet_omission_witnesses':facet_witnesses,'traces':traces,'rectangle_false_point':list(map(str,rectangle_false)),'out_of_language_collision':{'left':list(map(str,p)),'right':list(map(str,q)),'forgotten_query':'x1<=1000'},'budget_control':{'representation':'irredundant original-space linear inequalities','necessary_initial_facets':len(halfspaces),'refuse_budget':len(halfspaces)-1,'sufficient_initial_facets':len(halfspaces)},'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'query_relative_tail_geometry.py',cp,source_path)}}
(R/'query-relative-tail-interface.json').write_text(json.dumps(out,indent=2)+'\n')
print('Constructed exact query-relative polygon:',len(poly),'vertices/facets; coherent refinement and omission witnesses passed.')
