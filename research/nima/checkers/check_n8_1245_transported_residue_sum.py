#!/usr/bin/env python3
"""Exact local transported-residue sum over the three <Y1245> source facets."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
ori=json.loads((R/'research/nima/results/n8-physical-residue-orientations.json').read_text());fib=json.loads((R/'research/nima/results/n8-physical-facet-inverse-fibers.json').read_text());matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byh={x['history_index']:x for x in matches};rep=next(x for x in ori['representatives'] if x['physical_bracket']==[1,2,4,5]);fo=next(x for x in fib['orbits'] if x['physical_bracket']==[1,2,4,5]);u=s.symbols('u1:9');n=8
def chart(key,start,v,zero):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];C=s.zeros(2,n);idx=0;dirs=[s.Matrix([1,0])];t=0
 for gi in range(1,len(groups)-1):d=0 if idx==zero else v[idx];idx+=1;t+=d;dirs.append(s.Matrix([1,t]))
 dirs.append(s.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   fixed=qi==0 and gi in (0,len(groups)-1);scale=1 if fixed else (0 if idx==zero else v[idx]);idx+=not fixed;C[:,label-1]=(-1 if label<start else 1)*scale*dirs[gi]
 return C
def extract(key,start,C):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];r0=groups[0][0];rl=groups[-1][0];sf=-1 if r0<start else 1;sl=-1 if rl<start else 1;D=s.Matrix([[sf,0],[0,sl]])*C[:,[r0-1,rl-1]].inv()*C;out=[];prev=s.Integer(0)
 for gi in range(1,len(groups)-1):
  label=next(x for x in groups[gi] if D[:,x-1]!=s.zeros(2,1));t=s.factor(D[1,label-1]/D[0,label-1]);out.append(s.factor(t-prev));prev=t
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   if qi==0 and gi in (0,len(groups)-1):continue
   sign=-1 if label<start else 1;out.append(s.factor((D[1,label-1] if gi==len(groups)-1 else D[0,label-1])/sign))
 assert len(out)==8;return out
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);Ysample=s.Matrix([[s.Rational(z) for z in row] for row in fo['target_sample']]);Z0=Z[:6,:];L=s.zeros(6,8);L[:,:6]=Z0.inv();K=s.Matrix.vstack(*[v.T for v in Z.T.nullspace()]);x=s.symbols('x1:5');X=s.Matrix(2,2,x);piv=next((i,j) for i in range(6) for j in range(i+1,6) if s.det(Ysample[:,[i,j]])!=0);target_rows=[(i,j) for i in range(2) for j in range(6) if j not in piv];entries=[];baseJ=None;chosen=None
for f in rep['source_facets']:
 C=chart(byh[f['history_index']]['cell_key'],f['exposing_chart']['cyclic_start'],u,f['exposing_chart']['coordinate']-1);Y=C*Z;N=Y[:,list(piv)].inv()*Y;tc=[N[i,j] for i,j in target_rows];free=[z for i,z in enumerate(u) if i!=f['exposing_chart']['coordinate']-1];# recover source coordinates from the pre-solved affine fiber branch
 ff=next(z for z in fo['facets'] if z['history_index']==f['history_index']);q=ff['fiber_solutions'][0]['variables'];xf={z:s.Rational(q[str(z)]) for z in x};Cf=Ysample*L+X.subs(xf)*K;alluv=extract(byh[f['history_index']]['cell_key'],f['exposing_chart']['cyclic_start'],Cf);uv={z:alluv[i] for i,z in enumerate(u) if i!=f['exposing_chart']['coordinate']-1};J=s.Matrix(tc).jacobian(free)*s.diag(*free);Jn=J.subs(uv)
 if chosen is None:
  chosen=[]
  for q in range(8):
   if s.Matrix([Jn[i,:] for i in chosen+[q]]).rank()>len(chosen):chosen.append(q)
   if len(chosen)==7:break
 det=s.factor(s.Matrix([Jn[i,:] for i in chosen]).det());coef=s.factor(s.Integer(f['seed_oriented_residue_sign'])/det);entries.append({'history_index':f['history_index'],'source_parameters':{str(x):str(s.factor(uv[x])) for x in free},'target_log_jacobian':str(det),'orientation_sign':f['seed_oriented_residue_sign'],'transported_coefficient':str(coef)});print(f['history_index'],det,coef,flush=True)
total=s.factor(sum(s.sympify(x['transported_coefficient']) for x in entries));checks={'three_branches':len(entries)==3,'common_target_chart_rank_seven':len(chosen)==7,'nonzero_jacobians':all(x['target_log_jacobian']!='0' for x in entries),'nonzero_total':total!=0};out={'schema':'marici.nima.n8-1245-transported-residue-sum.v1','physical_bracket':[1,2,4,5],'target_pivot':[x+1 for x in piv],'target_coordinate_indices':chosen,'target_sample':fo['target_sample'],'contributions':entries,'summed_coefficient':str(total),'checks':checks,'passed':all(checks.values()),'claim_boundary':'This is an exact pointwise evaluation in seven ordinary normalized target coordinates. It is not yet a symbolic identity or comparison with an independent closed-form boundary canonical form.'};p=R/'research/nima/results/n8-1245-transported-residue-sum.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'summed_coefficient':str(total),'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
