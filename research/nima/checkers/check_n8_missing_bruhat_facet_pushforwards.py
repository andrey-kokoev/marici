#!/usr/bin/env python3
"""Push forward the 25 external Bruhat facets omitted by alpha-zero charts."""
from pathlib import Path
import json,itertools,collections,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
bru=json.loads((ROOT/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());cov=json.loads((ROOT/'research/nima/results/n8-coordinate-to-bruhat-boundary-coverage.json').read_text());n=8
inc=collections.defaultdict(list)
for c in bru['cells']:
 for f in c['bruhat_facets']:inc[tuple(f)].append(c['history_index'])
missing={tuple(x['boundary_permutation']):x for x in cov['missing_facet_incidences']};external=[(f,hs[0]) for f,hs in inc.items() if len(hs)==1 and f in missing];assert len(external)==41
def F(f,j):q,r=divmod(j-1,n);return f[r]+q*n
def necklace(f):
 out=[]
 for a in range(1,n+1):
  vals=[]
  for b in range(a-n,a):
   v=F(f,b)
   if v>=a:vals.append((v-1)%n+1)
  out.append(tuple(sorted(vals,key=lambda x:(x-a)%n)))
 return out
def bases(f):
 neck=necklace(f);out=set()
 for B in itertools.combinations(range(1,n+1),2):
  ok=True
  for a,I in enumerate(neck,1):
   order=lambda x:(x-a)%n
   if any(x<y for x,y in zip(sorted(map(order,B)),sorted(map(order,I)))):ok=False;break
  if ok:out.add(B)
 return out
def classes(B):
 zero=[i for i in range(1,n+1) if not any(i in b for b in B)];left=[i for i in range(1,n+1) if i not in zero];groups=[]
 while left:
  i=left.pop(0);g=[i];rest=[]
  for j in left:
   if tuple(sorted((i,j))) not in B:g.append(j)
   else:rest.append(j)
  left=rest;groups.append(g)
 return zero,groups
def chart(f):
 B=bases(f);zero,groups=classes(B);assert len(groups)>=2;params=s.symbols('u1:20');k=0;C=s.zeros(2,n)
 # Fix one representative in first two projective groups to e1,e2.
 for gi,g in enumerate(groups):
  if gi==0:direction=s.Matrix([1,0])
  elif gi==1:direction=s.Matrix([0,1])
  else:direction=s.Matrix([1,params[k]]);k+=1
  for q,label in enumerate(g):
   if q==0 and gi<2:scale=s.Integer(1)
   else:scale=params[k];k+=1
   C[:,label-1]=scale*direction
 return C,list(params[:k]),zero,groups
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);quads=list(itertools.combinations(range(8),4));edges=[(i,(i+1)%8) for i in range(8)];standard={tuple(sorted(x+y)) for z,x in enumerate(edges) for y in edges[z+1:] if len(set(x+y))==4};rows=[]
for f,h in external:
 C,p,zero,groups=chart(f);assert len(p)==7,(f,len(p),zero,groups);Y=C*Z;v1={x:s.Integer(i+2) for i,x in enumerate(p)};v2={x:s.Integer(2*i+3) for i,x in enumerate(p)};piv=next((i,j) for i in range(6) for j in range(i+1,6) if s.det(Y[:,[i,j]]).subs(v1)!=0);N=s.simplify(Y[:,list(piv)].inv()*Y);coords=[N[i,j] for i in range(2) for j in range(6) if j not in piv];rank=s.Matrix(coords).jacobian(p).subs(v1).rank();labels=[]
 for q in quads:
  fixed=tuple(Z[i,:] for i in q)
  if s.det(s.Matrix.vstack(Y.subs(v1),*fixed))==0 and s.det(s.Matrix.vstack(Y.subs(v2),*fixed))==0:labels.append(tuple(i+1 for i in q))
 rows.append({'history_index':h,'boundary_permutation':list(f),'zero_columns':zero,'parallel_classes':groups,'target_rank':rank,'target_brackets':[list(x) for x in labels],'standard_brackets':[list(x) for x in labels if tuple(i-1 for i in x) in standard],'nonstandard_brackets':[list(x) for x in labels if tuple(i-1 for i in x) not in standard]})
checks={'fortyone_missing_external_facets':len(rows)==41,'all_charts_dimension_seven':True,'all_target_ranks_at_most_seven':all(r['target_rank']<=7 for r in rows),'at_most_one_bracket_per_rank7':all(len(r['target_brackets'])<=1 for r in rows if r['target_rank']==7)}
out={'schema':'marici.nima.n8-missing-bruhat-facet-pushforwards.v1','rank_distribution':{str(k):sum(r['target_rank']==k for r in rows) for k in sorted({r['target_rank'] for r in rows})},'standard_labelled_rank7':sum(r['target_rank']==7 and bool(r['standard_brackets']) for r in rows),'nonstandard_labelled_rank7':sum(r['target_rank']==7 and bool(r['nonstandard_brackets']) for r in rows),'unlabelled_rank7':sum(r['target_rank']==7 and not r['target_brackets'] for r in rows),'details':rows,'checks':checks,'passed':all(checks.values()),'claim_boundary':'Rank and bracket labels use exact fixed moment-curve Z and two exact generic chart points. Nonlinear unlabelled images require implicitization.'};p=ROOT/'research/nima/results/n8-missing-bruhat-facet-pushforwards.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='details'},indent=2));raise SystemExit(0 if out['passed'] else 1)
