#!/usr/bin/env python3
"""Exact transition-residue test for corrected n=8 target groups with zero raw coefficient sum."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
groups=[g for g in json.loads((ROOT/'research/nima/results/n8-target-boundary-grouping.json').read_text())['groups'] if g['source_coefficient_sum']==0];matches={x['history_index']:x for x in json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches']};a=s.symbols('a1:9');b=s.symbols('b1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])};Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)])
def embed(q,X):
 e=q['embedding'];sup=list(range(1,9)) if isinstance(e,int) else e['support'];rot=e if isinstance(e,int) else e['rotation'];O=s.zeros(2,8)
 for j in range(X.cols):O[:,sup[(j+rot)%len(sup)]-1]=X[:,j]
 return O
def Yof(branch,vars):
 q=matches[branch['history_index']];X=M[q['seed_type']].xreplace(dict(zip(a,vars))).subs(vars[branch['alpha']-1],0);return embed(q,X)*Z
vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};bvals={y:vals[x] for x,y in zip(a,b)};outgroups=[]
for gi,g in enumerate(groups):
 ref=g['branches'][0];Y1=Yof(ref,a);free1=[x for i,x in enumerate(a,1) if i!=ref['alpha']];trans=[];total=s.Integer(ref['source_coefficient'])
 for branch in g['branches'][1:]:
  Y2=Yof(branch,b);free2=[x for i,x in enumerate(b,1) if i!=branch['alpha']];piv=next((i,j) for i in range(6) for j in range(i+1,6) if s.det(Y1[:,[i,j]]).subs(vals)!=0 and s.det(Y2[:,[i,j]]).subs(bvals)!=0);N1=s.simplify(Y1[:,list(piv)].inv()*Y1);N2=s.simplify(Y2[:,list(piv)].inv()*Y2);eq=[s.factor(N1[i,j]-N2[i,j]) for i in range(2) for j in range(6) if s.factor(N1[i,j]-N2[i,j])!=0];sol=s.solve(eq,free2,dict=True,simplify=False);row={'branch':branch,'solution_count':len(sol),'pivot':[piv[0]+1,piv[1]+1]}
  if len(sol)==1 and all(x in sol[0] for x in free2):
   T=[s.factor(sol[0][x]) for x in free2];J=s.Matrix([[s.factor(free1[j]/T[i]*s.diff(T[i],free1[j])) for j in range(7)] for i in range(7)]);det=s.factor(J.det());row['log_jacobian']=str(det);row['transition']={str(x):str(z) for x,z in zip(free2,T)};total=s.factor(total+s.Integer(branch['source_coefficient'])*det)
  trans.append(row)
 outgroups.append({'target_label':g['target_label'],'kind':g['kind'],'multiplicity':g['multiplicity'],'reference':ref,'transitions':trans,'transported_residue_coefficient':str(total),'cancels':total==0});print(gi,g['target_label'],str(total),flush=True)
checks={'seven_zero_raw_sum_groups':len(groups)==7,'all_transitions_unique_complete':all('log_jacobian' in t for g in outgroups for t in g['transitions']),'all_transported_residues_cancel':all(g['cancels'] for g in outgroups)};out={'schema':'marici.nima.n8-zero-sum-target-group-residues.v1','groups':outgroups,'checks':checks,'passed':all(checks.values()),'claim_boundary':'Transitions are exact rational target-chart equalities for fixed exact moment-curve Z. Cancellation is coefficientwise after logarithmic Jacobian transport to each group reference chart.'};p=ROOT/'research/nima/results/n8-zero-sum-target-group-residues.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
