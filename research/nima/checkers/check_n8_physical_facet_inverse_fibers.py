#!/usr/bin/env python3
"""Exact inverse-fiber tests for all eleven physical orbit representatives."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
ori=json.loads((R/'research/nima/results/n8-physical-residue-orientations.json').read_text());matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byh={x['history_index']:x for x in matches};n=8;u=s.symbols('u1:9')
def chart(key,start,v,zero):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];C=s.zeros(2,n);idx=0;dirs=[s.Matrix([1,0])];t=0
 for gi in range(1,len(groups)-1):d=0 if idx==zero else v[idx];idx+=1;t+=d;dirs.append(s.Matrix([1,t]))
 dirs.append(s.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   fixed=qi==0 and gi in (0,len(groups)-1);scale=1 if fixed else (0 if idx==zero else v[idx]);idx+=not fixed;C[:,label-1]=(-1 if label<start else 1)*scale*dirs[gi]
 return C
def F(f,j):q,r=divmod(j-1,n);return f[r]+q*n
def facet_key(f):
 neck=[]
 for a in range(1,n+1):
  vals=[]
  for b in range(a-n,a):
   v=F(f,b)
   if v>=a:vals.append((v-1)%n+1)
  neck.append(tuple(sorted(vals,key=lambda x:(x-a)%n)))
 B=set()
 for i in range(1,n+1):
  for j in range(i+1,n+1):
   ok=True
   for a,I in enumerate(neck,1):
    pos=lambda x:(x-a)%n
    if any(x<y for x,y in zip(sorted(map(pos,(i,j))),sorted(map(pos,I)))):ok=False;break
   if ok:B.add((i,j))
 zero=[i for i in range(1,n+1) if not any(i in b for b in B)];left=[i for i in range(1,n+1) if i not in zero];groups=[]
 while left:
  i=left.pop(0);g=[i];rest=[]
  for j in left:
   if tuple(sorted((i,j))) not in B:g.append(j)
   else:rest.append(j)
  left=rest;groups.append(g)
 return {'zero_columns':zero,'parallel_classes':groups}
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);Z0=Z[:6,:];L=s.zeros(6,8);L[:,:6]=Z0.inv();null=Z.T.nullspace();K=s.Matrix.vstack(*[v.T for v in null]);assert L*Z==s.eye(6) and K*Z==s.zeros(2,6);vals={x:s.Integer(p) for x,p in zip(u,[2,3,5,7,11,13,17,19])};x=s.symbols('x1:5');X=s.Matrix(2,2,x);orbits=[]
for rep in ori['representatives']:
 base=rep['source_facets'][0];Cb=chart(byh[base['history_index']]['cell_key'],base['exposing_chart']['cyclic_start'],u,base['exposing_chart']['coordinate']-1).subs(vals);Y=Cb*Z;C=Y*L+X*K;rows=[]
 for f in rep['source_facets']:
  key=facet_key(tuple(f['boundary_permutation']));eq=[]
  for j in key['zero_columns']:eq.extend(C[:,j-1])
  for g in key['parallel_classes']:
   for j in g[1:]:eq.append(s.det(C[:,[g[0]-1,j-1]]))
  eq=[s.factor(z) for z in eq if z!=0];sol=s.solve(eq,x,dict=True,simplify=False);complete=[q for q in sol if all(v in q for v in x)];positive=[]
  branch=[]
  for q in complete:
   Cv=C.subs(q);mins={(i+1,j+1):s.factor(s.det(Cv[:,[i,j]])) for i in range(8) for j in range(i+1,8)}
   if all(z>=0 for z in mins.values()):positive.append(q)
   az=[i for i in range(1,9) if Cv[:,i-1]==s.zeros(2,1)];ap=[];left=[i for i in range(1,9) if i not in az]
   while left:
    i=left.pop(0);g=[i];rest=[]
    for j in left:
     if mins[tuple(sorted((i,j)))]==0:g.append(j)
     else:rest.append(j)
    left=rest;ap.append(g)
   branch.append({'variables':{str(v):str(s.factor(q[v])) for v in x},'positive':q in positive,'actual_key':{'zero_columns':az,'parallel_classes':ap},'exact_open_facet_matroid':az==key['zero_columns'] and ap==key['parallel_classes']})
  rows.append({'history_index':f['history_index'],'boundary_permutation':f['boundary_permutation'],'boundary_key':key,'constraint_count':len(eq),'solution_count':len(sol),'complete_solution_count':len(complete),'open_facet_solution_count':sum(z['exact_open_facet_matroid'] for z in branch),'positive_solution_count':len(positive),'fiber_solutions':branch});print(rep['physical_bracket'],f['history_index'],len(eq),len(sol),len(complete),sum(z['exact_open_facet_matroid'] for z in branch),len(positive),flush=True)
 bracket=rep['physical_bracket'];on=s.det(s.Matrix.vstack(Y,*[Z[i-1,:] for i in bracket]))==0;orbits.append({'physical_bracket':bracket,'target_sample':[[str(z) for z in Y.row(i)] for i in range(2)],'sample_on_bracket':on,'facets':rows})
flat=[f for q in orbits for f in q['facets']];checks={'three_orbits':len(orbits)==3,'eleven_facets':len(flat)==11,'all_samples_on_claimed_brackets':all(q['sample_on_bracket'] for q in orbits),'every_facet_has_open_matroid_inverse':all(f['open_facet_solution_count']>=1 for f in flat),'all_open_facet_maps_degree_one_at_samples':all(f['open_facet_solution_count']==1 for f in flat),'one_extra_degenerate_algebraic_solution':sum(f['complete_solution_count']-f['open_facet_solution_count'] for f in flat)==1,'exactly_one_positive_tile_over_each_sample':all(sum(f['positive_solution_count'] for f in q['facets'])==1 for q in orbits),'kernel_dimension_two':K.shape==(2,8)};out={'schema':'marici.nima.n8-physical-facet-inverse-fibers.v2','kernel_basis':[[str(z) for z in K.row(i)] for i in range(2)],'orbits':orbits,'checks':checks,'passed':all(checks.values()),'claim_boundary':'At each exact positive target sample exactly one source facet has a positive inverse, as expected for a boundary triangulation. Every open facet has exactly one inverse at its sample. The raw history-2 equations also have one extra algebraic solution, which is classified separately by its actual matroid and is not counted unless it lies in the open facet.'};p=R/'research/nima/results/n8-physical-facet-inverse-fibers.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
