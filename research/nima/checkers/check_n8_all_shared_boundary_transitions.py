#!/usr/bin/env python3
"""Exact transition and orientation audit for every coarse-shared n=8 alpha-zero boundary pair."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
matches=json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byhi={x['history_index']:x for x in matches};a=s.symbols('a1:9');b=s.symbols('b1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])}
def emb(q,X):
 e=q['embedding'];sup=list(range(1,9)) if isinstance(e,int) else e['support'];rot=e if isinstance(e,int) else e['rotation'];O=s.zeros(2,8)
 for j in range(X.cols):O[:,sup[(j+rot)%len(sup)]-1]=(-1 if j+rot>=len(sup) else 1)*X[:,j]
 return O
def key(X):
 cols=[X[:,j] for j in range(8)];zero=[j for j,c in enumerate(cols) if c==s.zeros(2,1)];nz=[j for j in range(8) if j not in zero];groups=[]
 while nz:
  i=nz.pop(0);g=[i];rest=[]
  for j in nz:(g if s.det(s.Matrix.hstack(cols[i],cols[j]))==0 else rest).append(j)
  nz=rest;groups.append(g)
 return (tuple(map(tuple,groups)),tuple(zero))
vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])}
def positive_orthant_sign(expr,variables):
 num,den=map(s.expand,s.fraction(s.cancel(expr)))
 def psign(poly):
  cs=s.Poly(poly,*variables).coeffs()
  if cs and all(c>0 for c in cs):return 1
  if cs and all(c<0 for c in cs):return -1
  return 0
 sn,sd=psign(num),psign(den);return sn*sd if sn and sd else 0
records=[]
for q in matches:
 C=emb(q,M[q['seed_type']])
 for e,x in enumerate(a,1):records.append((key(C.subs(vals|{x:0})),q['history_index'],q['seed_type'],e))
groups={}
for r in records:groups.setdefault(r[0],[]).append(r)
pairs=[g for g in groups.values() if len({r[1] for r in g})>1];assert len(pairs)==28
rows=[]
for n,g in enumerate(pairs):
 assert len(g)==2;_,h1,s1,e1=g[0];_,h2,s2,e2=g[1];q1,q2=byhi[h1],byhi[h2];C1=emb(q1,M[s1]).subs(a[e1-1],0);C2=emb(q2,M[s2].xreplace(dict(zip(a,b)))).subs(b[e2-1],0);piv=next((i,j) for i in range(8) for j in range(i+1,8) if s.det(C1[:,[i,j]])!=0 and s.det(C2[:,[i,j]])!=0);N1=s.simplify(C1[:,list(piv)].inv()*C1);N2=s.simplify(C2[:,list(piv)].inv()*C2);eq=[s.factor(N1[i,j]-N2[i,j]) for i in range(2) for j in range(8) if s.factor(N1[i,j]-N2[i,j])!=0];source=[x for i,x in enumerate(a,1) if i!=e1];target=[x for i,x in enumerate(b,1) if i!=e2];bvals={y:vals[x] for x,y in zip(a,b)};c1=[N1[i,j] for i in range(2) for j in range(8) if j not in piv];c2=[N2[i,j] for i in range(2) for j in range(8) if j not in piv];rank1=s.Matrix(c1).jacobian(source).subs(vals).rank();rank2=s.Matrix(c2).jacobian(target).subs(bvals).rank();sol=s.solve(eq,target,dict=True,simplify=False);row={'pair_index':n,'left':{'history':h1,'seed':s1,'alpha':e1,'boundary_chart_rank':rank1},'right':{'history':h2,'seed':s2,'alpha':e2,'boundary_chart_rank':rank2},'pivot':[piv[0]+1,piv[1]+1],'equations':len(eq),'solution_count':len(sol),'raw_solutions':[{str(k):str(s.factor(v)) for k,v in z.items()} for z in sol]}
 if len(sol)==1 and all(x in sol[0] for x in target):
  T=[s.factor(sol[0][x]) for x in target];J=s.Matrix([[s.factor(source[j]/T[i]*s.diff(T[i],source[j])) for j in range(7)] for i in range(7)]);det=s.factor(J.det());tv=[s.factor(z.subs(vals)) for z in T];signs=[positive_orthant_sign(z,source) for z in T];classification='positive_to_positive' if all(z==1 for z in signs) else ('positive_chambers_disjoint' if any(z==-1 for z in signs) else 'sign_unresolved');row.update({'transition':{str(x):str(z) for x,z in zip(target,T)},'target_coordinate_global_signs':signs,'positive_orthant_classification':classification,'log_jacobian':str(det),'positive_at_exact_sample':all(z>0 for z in tv),'sample_target':[str(z) for z in tv]})
 rows.append(row);print(n,h1,e1,h2,e2,row.get('solution_count'),row.get('log_jacobian'),flush=True)
complete=[r for r in rows if 'log_jacobian' in r];positive=[r for r in complete if r['positive_orthant_classification']=='positive_to_positive'];negative=[r for r in complete if r['positive_orthant_classification']=='positive_chambers_disjoint'];unknown=[r for r in complete if r['positive_orthant_classification']=='sign_unresolved'];incomplete=[r for r in rows if 'log_jacobian' not in r]
rank6overlap=[r for r in incomplete if r['solution_count']==1 and r['left']['boundary_chart_rank']==r['right']['boundary_chart_rank']==6];rank6disjoint=[r for r in incomplete if r['solution_count']==0 and r['left']['boundary_chart_rank']==r['right']['boundary_chart_rank']==6]
checks={'all_28_pairs_audited':len(rows)==28,'twentythree_complete_symbolic_transitions':len(complete)==23,'twentythree_globally_positive_rank7_transitions':len(positive)==23,'no_globally_disjoint_rank7_positive_chambers':len(negative)==0,'no_complete_transition_sign_unresolved':not unknown,'four_rank6_positive_overlaps':len(rank6overlap)==4 and all('a4 - b4' in str(r['raw_solutions']) for r in rank6overlap),'one_rank6_false_collision':len(rank6disjoint)==1,'all_complete_jacobians_nonzero':all(r['log_jacobian']!='0' for r in complete)}
out={'schema':'marici.nima.n8-all-shared-boundary-transitions.v4','pairs':rows,'summary':{'rank7_positive_internal_pairs':len(positive),'rank7_positive_disjoint_pairs':len(negative),'rank6_positive_overlap_pairs':len(rank6overlap),'rank6_false_collision_pairs':len(rank6disjoint),'complete_sign_unresolved':len(unknown)},'checks':checks,'passed':all(checks.values()),'conclusion':'After twisted cyclic embedding, all 23 complete rank-seven transitions are positive. Four further rank-six image overlaps are positive, and one rank-six coarse collision has no generic transition. Thus 27 coarse pairs are genuine positive incidences, but the previously named 7/11 exception was an artifact of omitting the k=2 cyclic wrap sign.','claim_boundary':'The 23 complete transition sign classifications are certified by coefficient signs on the positive orthant. The four rank-six overlaps admit positive choices 0<b4<a4. The remaining rank-six pair has no generic symbolic transition in the chosen normalized charts.'};p=ROOT/'research/nima/results/n8-all-shared-boundary-transitions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
