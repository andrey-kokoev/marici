#!/usr/bin/env python3
"""Exact dlog transitions for the 17 shared facets hidden by original seed charts."""
from pathlib import Path
import json,collections,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byh={x['history_index']:x for x in matches};bru=json.loads((R/'research/nima/results/n8-positroid-bruhat-boundaries.json').read_text());atlas=json.loads((R/'research/nima/results/n8-rank2-cyclic-positive-atlas.json').read_text());old=json.loads((R/'research/nima/results/n8-all-shared-boundary-transitions.json').read_text());n=8
inc=collections.defaultdict(list)
for c in bru['cells']:
 for f in c['bruhat_facets']:inc[tuple(f)].append(c['history_index'])
oldpairs={frozenset((r['left']['history'],r['right']['history'])) for r in old['pairs'] if r.get('positive_orthant_classification')=='positive_to_positive'};hidden=[(f,hs) for f,hs in inc.items() if len(hs)==2 and frozenset(hs) not in oldpairs];assert len(hidden)==17
A=s.symbols('a1:9');B=s.symbols('b1:9')
def chart(key,start,v,zero):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];C=s.zeros(2,n);idx=0;dirs=[s.Matrix([1,0])];t=s.Integer(0)
 for gi in range(1,len(groups)-1):
  d=0 if idx==zero else v[idx];idx+=1;t+=d;dirs.append(s.Matrix([1,t]))
 dirs.append(s.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   if qi==0 and gi in (0,len(groups)-1):scale=1
   else:scale=0 if idx==zero else v[idx];idx+=1
   C[:,label-1]=(-1 if label<start else 1)*scale*dirs[gi]
 assert idx==8;return C
acells={x['history_index']:x for x in atlas['cells']}
def exposures(h,f):
 return [(c['cyclic_start'],e['coordinate']-1) for c in acells[h]['charts'] for e in c['exposed_facets'] if tuple(e['boundary_permutation'])==f]
def psign(expr,vars):
 num,den=map(s.expand,s.fraction(s.cancel(expr)))
 def z(p):
  cs=s.Poly(p,*vars).coeffs();return 1 if cs and all(x>0 for x in cs) else (-1 if cs and all(x<0 for x in cs) else 0)
 x,y=z(num),z(den);return x*y if x and y else 0
rows=[]
for ix,(f,hs) in enumerate(hidden):
 h1,h2=hs;x1,x2=exposures(h1,f),exposures(h2,f);common=sorted({z[0] for z in x1}&{z[0] for z in x2});assert common;s1=s2=common[0];e1=next(e for q,e in x1 if q==s1);e2=next(e for q,e in x2 if q==s2);C1=chart(byh[h1]['cell_key'],s1,A,e1);C2=chart(byh[h2]['cell_key'],s2,B,e2);piv=next((i,j) for i in range(n) for j in range(i+1,n) if s.det(C1[:,[i,j]])!=0 and s.det(C2[:,[i,j]])!=0);N1=s.simplify(C1[:,list(piv)].inv()*C1);N2=s.simplify(C2[:,list(piv)].inv()*C2);eq=[s.factor(N1[i,j]-N2[i,j]) for i in range(2) for j in range(n) if s.factor(N1[i,j]-N2[i,j])!=0];src=[x for i,x in enumerate(A) if i!=e1];tgt=[x for i,x in enumerate(B) if i!=e2];sol=s.solve(eq,tgt,dict=True,simplify=False);row={'pair_index':ix,'boundary_permutation':list(f),'left':{'history':h1,'cyclic_start':s1,'coordinate':e1+1},'right':{'history':h2,'cyclic_start':s2,'coordinate':e2+1},'pivot':[x+1 for x in piv],'solution_count':len(sol)}
 if len(sol)==1 and all(x in sol[0] for x in tgt):
  T=[s.factor(sol[0][x]) for x in tgt];J=s.Matrix([[s.factor(src[j]/T[i]*s.diff(T[i],src[j])) for j in range(7)] for i in range(7)]);det=s.factor(J.det());signs=[psign(x,src) for x in T];resleft=(-1)**e1;resright=det*(-1)**e2;row.update({'transition':{str(x):str(y) for x,y in zip(tgt,T)},'positive_coordinate_signs':signs,'log_jacobian':str(det),'oriented_residue_sum':str(s.factor(resleft+resright)),'cancels':s.factor(resleft+resright)==0})
 rows.append(row);print(ix,h1,h2,s1,e1+1,s2,e2+1,row.get('log_jacobian'),row.get('cancels'),flush=True)
checks={'seventeen_hidden_pairs':len(rows)==17,'all_transitions_solved':all(r['solution_count']==1 and 'log_jacobian' in r for r in rows),'all_positive_to_positive':all(all(x==1 for x in r['positive_coordinate_signs']) for r in rows),'all_log_jacobians_unit':all(r['log_jacobian'] in ('1','-1') for r in rows),'all_oriented_residues_cancel':all(r['cancels'] for r in rows)};out={'schema':'marici.nima.n8-hidden-polygon-chart-transitions.v1','pairs':rows,'checks':checks,'passed':all(checks.values()),'claim_boundary':'These are independent exact transitions in cyclic rank-two positive polygon charts, equivalent positive coordinates but not claimed to be the source paper’s specific lexicographic bridge charts.'};p=R/'research/nima/results/n8-hidden-polygon-chart-transitions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
