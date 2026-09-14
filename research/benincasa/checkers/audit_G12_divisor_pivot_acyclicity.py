#!/usr/bin/env python3
"""Exhaust normal-coordinate pivots for an acyclic G12 IBP dependency order."""
import itertools,json
from pathlib import Path
# Linear coefficient supports in (a,b,c).
support={'B12':{'c'},'g1':{'b','c'},'g2':{'a','c'},'g3':{'a','b'},'s23':{'b','c'},'s31':{'a','c'}}
# Analyze each preconditioned G12 branch: g1 and s23 never coexist in branch 23;
# g2 and s31 never coexist in branch 31.
branches=[{'name':'23_g1','walls':{'B12','g1','g2','g3'}},{'name':'23_s23','walls':{'B12','s23','g2','g3'}},{'name':'31_g2','walls':{'B12','g1','g2','g3'}},{'name':'31_s31','walls':{'B12','g1','g3','s31'}}]
def edges(walls,piv):return {(q,r) for q in walls for r in walls if q!=r and piv[q] in support[r]}
def cyclic(vertices,E):
 indeg={v:0 for v in vertices}
 for u,v in E:indeg[v]+=1
 todo=[v for v in vertices if indeg[v]==0];seen=0
 while todo:
  u=todo.pop();seen+=1
  for a,b in E:
   if a==u:
    indeg[b]-=1
    if indeg[b]==0:todo.append(b)
 return seen<len(vertices)
keys=list(support);assignments=[]
for choices in itertools.product(*(sorted(support[k]) for k in keys)):
 p=dict(zip(keys,choices));bad=[]
 for br in branches:
  E=edges(br['walls'],p)
  if cyclic(br['walls'],E):bad.append(br['name'])
 assignments.append({'pivots':p,'cyclic_branches':bad,'all_acyclic':not bad})
valid=[x for x in assignments if x['all_acyclic']]
# Exhibit the unavoidable core in branch containing B12,g1,g2,g3.
checks={'all_pivots_exhausted':len(assignments)==1*2*2*2*2*2,'no_acyclic_assignment':not valid,'every_assignment_has_cycle':all(x['cyclic_branches'] for x in assignments),'preconditioned_branches_covered':len(branches)==4}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-divisor-pivot-acyclicity.v1','divisor_variable_support':{k:sorted(v) for k,v in support.items()},'preconditioned_branches':[{'name':b['name'],'walls':sorted(b['walls'])} for b in branches],'pivot_assignments_tested':len(assignments),'acyclic_assignments':len(valid),'result':'No choice of coordinate normal for the linear G12 walls makes every post-partial-fraction dependency graph acyclic. Coordinate-by-coordinate IBP therefore admits no strict divisor-weight order.','structural_core':'The branch containing B12,g1,g2,g3 forces a cycle: choosing the g3 pivot a couples back to g2, while choosing b couples back to g1; alternative c-pivots couple to B12.','consequence':'VA0 requires a simultaneous multivariate syzygy/Griffiths-Dwork reduction, not sequential one-wall homotopies.','next_constructor':'Solve A_a*d_a(D)+A_b*d_b(D)+A_c*d_c(D)=target leading numerator modulo D for the coupled divisor D=B12*g1*g2*g3*K0, with exchange-equivariant coefficients, then use that vector field as the global lowering homotopy.','checks':checks,'passed':True}
d=Path(__file__).resolve().parents[1]/'results'/'G12_divisor_pivot_acyclicity.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'tested':len(assignments),'acyclic':0,'consequence':out['consequence']}))
