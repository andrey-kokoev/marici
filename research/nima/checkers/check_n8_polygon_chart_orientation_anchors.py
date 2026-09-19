#!/usr/bin/env python3
"""Anchor hidden-facet polygon-chart orientations to the original seed dlog forms."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
trans=json.loads((R/'research/nima/results/n8-hidden-polygon-chart-transitions.json').read_text());bridge_trans=json.loads((R/'research/nima/results/n8-hidden-bcfw-bridge-transitions.json').read_text());bridge_physical=json.loads((R/'research/nima/results/n8-physical-bcfw-residue-representatives.json').read_text());physical=json.loads((R/'research/nima/results/n8-physical-residue-orbit-representatives.json').read_text());matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byh={x['history_index']:x for x in matches};a=s.symbols('a1:9');u=s.symbols('u1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])}
def emb(q,X):
 e=q['embedding'];sup=list(range(1,9)) if isinstance(e,int) else e['support'];rot=e if isinstance(e,int) else e['rotation'];O=s.zeros(2,8)
 for j in range(X.cols):O[:,sup[(j+rot)%len(sup)]-1]=(-1 if j+rot>=len(sup) else 1)*X[:,j]
 return O
def poly(key,start,v):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%8;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];C=s.zeros(2,8);idx=0;dirs=[s.Matrix([1,0])];t=s.Integer(0)
 for gi in range(1,len(groups)-1):t+=v[idx];idx+=1;dirs.append(s.Matrix([1,t]))
 dirs.append(s.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   fixed=qi==0 and gi in (0,len(groups)-1);scale=1 if fixed else v[idx];idx+=not fixed
   C[:,label-1]=(-1 if label<start else 1)*scale*dirs[gi]
 assert idx==8;return C
vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};uvguess={x:s.Integer(p) for x,p in zip(u,[2,3,5,7,11,13,17,19])};needed_hidden={(side['history'],side['cyclic_start']) for r in trans['pairs'] for side in (r['left'],r['right'])};needed_physical={(f['history_index'],f['exposing_chart']['cyclic_start']) for q in physical['representatives'] for f in q['source_facets']};needed_bridge={(side['history'],side['cyclic_start']) for r in bridge_trans['pairs'] for side in (r['left'],r['right'])};needed_bridge_physical={(f['history_index'],f['exposing_bridge_chart']['cyclic_start']) for q in bridge_physical['representatives'] for f in q['source_facets']};needed=sorted(needed_hidden|needed_physical|needed_bridge|needed_bridge_physical);cachep=R/'research/nima/results/.n8-polygon-orientation-anchor-cache.json';cached=json.loads(cachep.read_text()) if cachep.exists() else {};anchors={(int(v['history']),int(v['cyclic_start'])):v for v in cached.values()}
for h,start in needed:
 if (h,start) in anchors:continue
 q=byh[h];Cs=emb(q,M[q['seed_type']]);Cp=poly(q['cell_key'],start,u);piv=next((i,j) for i in range(8) for j in range(i+1,8) if s.det(Cp[:,[i,j]])!=0 and s.det(Cs[:,[i,j]])!=0);Ns=s.simplify(Cs[:,list(piv)].inv()*Cs);Np=s.simplify(Cp[:,list(piv)].inv()*Cp);components=[(i,j) for i in range(2) for j in range(8) if j not in piv];eq=[s.factor(Np[i,j]-Ns[i,j].subs(vals)) for i,j in components];sol=s.solve(eq,u,dict=True,simplify=False);assert len(sol)==1 and all(x in sol[0] for x in u),(h,start,len(sol));uv={x:s.factor(sol[0][x]) for x in u};# select eight independent intrinsic coordinates using polygon Jacobian
 xp=[Np[i,j] for i,j in components];xs=[Ns[i,j] for i,j in components];Jall=s.Matrix(xp).jacobian(u).subs(uv);chosen=[]
 for r in range(len(xp)):
  if s.Matrix([Jall[i,:] for i in chosen+[r]]).rank()>len(chosen):chosen.append(r)
  if len(chosen)==8:break
 Jp=s.Matrix([xp[i] for i in chosen]).jacobian(u);Js=s.Matrix([xs[i] for i in chosen]).jacobian(a);Lp=s.diag(*u);Ls=s.diag(*a);dp=s.factor((Jp*Lp).det().subs(uv));ds=s.factor((Js*Ls).det().subs(vals));ratio=s.factor(dp/ds);sgn=s.signsimp(s.sign(ratio));assert sgn in (-1,1),(h,start,ratio);anchors[(h,start)]={'history':h,'cyclic_start':start,'pivot':[x+1 for x in piv],'polygon_parameters':{str(x):str(uv[x]) for x in u},'dlog_jacobian_sign':int(sgn),'dlog_jacobian_at_sample':str(ratio)};cachep.write_text(json.dumps({f'{x[0]}:{x[1]}':v for x,v in anchors.items()},indent=2)+'\n');print(h,start,sgn,flush=True)
rows=[]
for r in trans['pairs']:
 L,Rr=r['left'],r['right'];ol=anchors[(L['history'],L['cyclic_start'])]['dlog_jacobian_sign'];orr=anchors[(Rr['history'],Rr['cyclic_start'])]['dlog_jacobian_sign'];jl=int(r['log_jacobian']);sl=ol*(-1)**(L['coordinate']-1);sr=orr*jl*(-1)**(Rr['coordinate']-1);rows.append({**r,'left_seed_oriented_residue_sign':sl,'right_in_left_seed_orientation_sign':sr,'seed_oriented_residue_sum':sl+sr,'cancels':sl+sr==0})
checks={'all_needed_charts_anchored':len(anchors)==len(needed),'seventeen_pairs':len(rows)==17,'all_boundary_jacobians_plus_one':all(r['log_jacobian']=='1' for r in rows),'all_seed_oriented_residues_cancel':all(r['cancels'] for r in rows)};out={'schema':'marici.nima.n8-polygon-chart-orientation-anchors.v1','anchors':list(anchors.values()),'pairs':rows,'checks':checks,'passed':all(checks.values()),'claim_boundary':'Top-chart signs are exact dlog Jacobian signs at matched rational interior points. Constancy follows because both charts parameterize the same connected positive cell with nonvanishing canonical-coordinate Jacobian.'};p=R/'research/nima/results/n8-polygon-chart-orientation-anchors.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
