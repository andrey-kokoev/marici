#!/usr/bin/env python3
"""Exact transitions for the 17 hidden facets in genuine cyclic BCFW bridge charts."""
from pathlib import Path
import json,collections,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
atlas=json.loads((R/'research/nima/results/n8-complete-cyclic-bcfw-bridge-atlas.json').read_text());bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());old=json.loads((R/'research/nima/results/n8-all-shared-boundary-transitions.json').read_text());A=s.symbols('a1:9');B=s.symbols('b1:9');n=8
inc=collections.defaultdict(list)
for c in bru['cells']:
 for f in c['bruhat_facets']:inc[tuple(f)].append(c['history_index'])
oldpairs={frozenset((r['left']['history'],r['right']['history'])) for r in old['pairs'] if r.get('positive_orthant_classification')=='positive_to_positive'};hidden=[(f,hs) for f,hs in inc.items() if len(hs)==2 and frozenset(hs) not in oldpairs];assert len(hidden)==17
charts=collections.defaultdict(list)
for c in atlas['charts']:charts[c['history_index']].append(c)
def exposures(h,f):return [(c,e) for c in charts[h] for e in c['exposed_facets'] if tuple(e['boundary_permutation'])==f]
def matrix(c,v,zero):
 D=s.zeros(2,n);p,q=[x-1 for x in c['decorated_identity_sources']];D[0,p]=1;D[1,q]=1
 for i,z in enumerate(c['bridge_word']):D[:,z['destination']-1]+=z['sign']*(0 if i==zero else v[i])*D[:,z['source']-1]
 r=c['cyclic_start']-1;C=s.zeros(2,n)
 for i in range(n):C[:,(i+r)%n]=(-1 if i+r>=n else 1)*D[:,i]
 return C
def psign(expr,vars):
 num,den=map(s.expand,s.fraction(s.cancel(expr)))
 def z(p):
  cs=s.Poly(p,*vars).coeffs();return 1 if cs and all(x>0 for x in cs) else (-1 if cs and all(x<0 for x in cs) else 0)
 x,y=z(num),z(den);return x*y if x and y else 0
rows=[]
for ix,(f,hs) in enumerate(hidden):
 h1,h2=hs;x1,x2=exposures(h1,f),exposures(h2,f);common=sorted({c['cyclic_start'] for c,e in x1}&{c['cyclic_start'] for c,e in x2});c1,e1=x1[0];c2,e2=x2[0]
 if common:
  start=common[0];c1,e1=next((c,e) for c,e in x1 if c['cyclic_start']==start);c2,e2=next((c,e) for c,e in x2 if c['cyclic_start']==start)
 else:start=[c1['cyclic_start'],c2['cyclic_start']]
 z1=e1['coordinate']-1;z2=e2['coordinate']-1;C1=matrix(c1,A,z1);C2=matrix(c2,B,z2);piv=next((i,j) for i in range(n) for j in range(i+1,n) if s.det(C1[:,[i,j]])!=0 and s.det(C2[:,[i,j]])!=0);N1=C1[:,list(piv)].inv()*C1;N2=C2[:,list(piv)].inv()*C2;eq=[s.factor(N1[i,j]-N2[i,j]) for i in range(2) for j in range(n) if s.factor(N1[i,j]-N2[i,j])!=0];src=[x for i,x in enumerate(A) if i!=z1];tgt=[x for i,x in enumerate(B) if i!=z2];sol=s.solve(eq,tgt,dict=True,simplify=False);row={'boundary_permutation':list(f),'left':{'history':h1,'cyclic_start':c1['cyclic_start'],'coordinate':z1+1},'right':{'history':h2,'cyclic_start':c2['cyclic_start'],'coordinate':z2+1},'solution_count':len(sol)}
 if len(sol)==1 and all(x in sol[0] for x in tgt):
  T=[s.factor(sol[0][x]) for x in tgt];J=s.Matrix([[s.factor(src[j]/T[i]*s.diff(T[i],src[j])) for j in range(7)] for i in range(7)]);det=s.factor(J.det());row.update({'transition':{str(x):str(y) for x,y in zip(tgt,T)},'positive_coordinate_signs':[psign(y,src) for y in T],'log_jacobian':str(det),'raw_residue_sum':str(s.factor((-1)**z1+det*(-1)**z2))})
 rows.append(row);print(ix,h1,h2,start,z1+1,z2+1,row.get('log_jacobian'),flush=True)
checks={'seventeen_pairs':len(rows)==17,'all_solved':all(r['solution_count']==1 and 'log_jacobian' in r for r in rows),'all_positive_to_positive':all(all(x==1 for x in r['positive_coordinate_signs']) for r in rows),'all_unit_log_jacobians':all(r['log_jacobian'] in ('1','-1') for r in rows)};out={'schema':'marici.nima.n8-hidden-bcfw-bridge-transitions.v1','pairs':rows,'checks':checks,'passed':all(checks.values()),'claim_boundary':'These are exact transitions between genuine positive colored-bridge charts at a common cyclic start. Top-chart orientation anchors to the original history forms are separate.'};p=R/'research/nima/results/n8-hidden-bcfw-bridge-transitions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
