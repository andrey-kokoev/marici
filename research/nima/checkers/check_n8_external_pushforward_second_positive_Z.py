#!/usr/bin/env python3
"""Cross-check all 86 external facets on a second exact totally positive Z."""
from pathlib import Path
import json,itertools,collections,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());base=json.loads((R/'research/nima/results/n8-complete-external-pushforward.json').read_text());n=8
inc=collections.defaultdict(list)
for c in bru['cells']:
 for f in c['bruhat_facets']:inc[tuple(f)].append(c['history_index'])
external=[(f,hs[0]) for f,hs in inc.items() if len(hs)==1];assert len(external)==86
def F(f,j):q,r=divmod(j-1,n);return f[r]+q*n
def bases(f):
 neck=[]
 for a in range(1,n+1):
  vals=[]
  for b in range(a-n,a):
   v=F(f,b)
   if v>=a:vals.append((v-1)%n+1)
  neck.append(tuple(sorted(vals,key=lambda x:(x-a)%n)))
 out=set()
 for B in itertools.combinations(range(1,n+1),2):
  if all(not any(x<y for x,y in zip(sorted((z-a)%n for z in B),sorted((z-a)%n for z in I))) for a,I in enumerate(neck,1)):out.add(B)
 return out
def chart(f):
 B=bases(f);zero=[i for i in range(1,n+1) if not any(i in b for b in B)];left=[i for i in range(1,n+1) if i not in zero];groups=[]
 while left:
  i=left.pop(0);g=[i];rest=[]
  for j in left:
   if tuple(sorted((i,j))) not in B:g.append(j)
   else:rest.append(j)
  left=rest;groups.append(g)
 u=s.symbols('u1:20');q=0;C=s.zeros(2,n)
 for gi,g in enumerate(groups):
  d=s.Matrix([1,0]) if gi==0 else (s.Matrix([0,1]) if gi==1 else s.Matrix([1,u[q]]));q+=gi>=2
  for z,label in enumerate(g):
   scale=1 if z==0 and gi<2 else u[q];q+=not(z==0 and gi<2);C[:,label-1]=scale*d
 assert q==7;return C,list(u[:q])
ts=[1,2,4,7,11,16,22,29];Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in ts]);quads=list(itertools.combinations(range(8),4));standard={tuple(sorted((i,i%8+1,j,j%8+1))) for i in range(1,9) for j in range(i+1,9) if len({i,i%8+1,j,j%8+1})==4};orig={tuple(r['boundary_permutation']):r for r in base['facets']};rows=[]
for ix,(f,h) in enumerate(external):
 C,p=chart(f);Y=C*Z;v1={x:s.Integer(i+2) for i,x in enumerate(p)};v2={x:s.Integer(2*i+3) for i,x in enumerate(p)};piv=next((i,j) for i in range(6) for j in range(i+1,6) if s.det(Y[:,[i,j]]).subs(v1)!=0);N=Y[:,list(piv)].inv()*Y;coords=[N[i,j] for i in range(2) for j in range(6) if j not in piv];rank=s.Matrix(coords).jacobian(p).subs(v1).rank();labels=[]
 for qd in quads:
  fixed=[Z[i,:] for i in qd]
  if s.det(s.Matrix.vstack(Y.subs(v1),*fixed))==0 and s.det(s.Matrix.vstack(Y.subs(v2),*fixed))==0:labels.append(tuple(i+1 for i in qd))
 old=orig[f];rows.append({'history_index':h,'boundary_permutation':list(f),'rank':rank,'brackets':[list(x) for x in labels],'original_rank':old['target_rank'],'original_brackets':old['target_brackets'],'matches_original':rank==old['target_rank'] and {tuple(x) for x in labels}=={tuple(x) for x in old['target_brackets']}});print(ix,h,rank,len(labels),rows[-1]['matches_original'],flush=True)
checks={'eighty_six_external':len(rows)==86,'rank_distribution_80_5_1':collections.Counter(r['rank'] for r in rows)=={7:80,6:5,5:1},'all_rank7_labels_physical':all(len(r['brackets'])==1 and tuple(r['brackets'][0]) in standard for r in rows if r['rank']==7),'facetwise_matches_first_Z':all(r['matches_original'] for r in rows)};out={'schema':'marici.nima.n8-external-pushforward-second-positive-Z.v1','Z_parameters':ts,'facets':rows,'checks':checks,'passed':all(checks.values())};p=R/'research/nima/results/n8-external-pushforward-second-positive-Z.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
