#!/usr/bin/env python3
"""Anchor the 34 hidden-facet BCFW charts to original seed dlog orientations."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
tr=json.loads((R/'research/nima/results/n8-hidden-bcfw-bridge-transitions.json').read_text());physical=json.loads((R/'research/nima/results/n8-physical-bcfw-residue-representatives.json').read_text());atlas=json.loads((R/'research/nima/results/n8-complete-cyclic-bcfw-bridge-atlas.json').read_text());polyanc=json.loads((R/'research/nima/results/n8-polygon-chart-orientation-anchors.json').read_text());matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byh={x['history_index']:x for x in matches};ba={(x['history_index'],x['cyclic_start']):x for x in atlas['charts']};pa={(x['history'],x['cyclic_start']):x for x in polyanc['anchors']};A=s.symbols('a1:9');U=s.symbols('u1:9');vals={x:s.Integer(p) for x,p in zip(A,[2,3,5,7,11,13,17,19])};n=8
def bridge(c,v):
 D=s.zeros(2,n);p,q=[x-1 for x in c['decorated_identity_sources']];D[0,p]=1;D[1,q]=1
 for i,z in enumerate(c['bridge_word']):D[:,z['destination']-1]+=z['sign']*v[i]*D[:,z['source']-1]
 r=c['cyclic_start']-1;C=s.zeros(2,n)
 for i in range(n):C[:,(i+r)%n]=(-1 if i+r>=n else 1)*D[:,i]
 return C
def polygon(key,start,v):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];C=s.zeros(2,n);idx=0;dirs=[s.Matrix([1,0])];t=0
 for gi in range(1,len(groups)-1):t+=v[idx];idx+=1;dirs.append(s.Matrix([1,t]))
 dirs.append(s.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   fixed=qi==0 and gi in (0,len(groups)-1);scale=1 if fixed else v[idx];idx+=not fixed;C[:,label-1]=(-1 if label<start else 1)*scale*dirs[gi]
 return C
def extract(key,start,C):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];r0,rl=groups[0][0],groups[-1][0];sf=-1 if r0<start else 1;sl=-1 if rl<start else 1;D=s.Matrix([[sf,0],[0,sl]])*C[:,[r0-1,rl-1]].inv()*C;out=[];prev=0
 for gi in range(1,len(groups)-1):label=groups[gi][0];t=s.factor(D[1,label-1]/D[0,label-1]);out.append(s.factor(t-prev));prev=t
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   if qi==0 and gi in (0,len(groups)-1):continue
   sign=-1 if label<start else 1;out.append(s.factor((D[1,label-1] if gi==len(groups)-1 else D[0,label-1])/sign))
 return out
needed_hidden={(z['history'],z['cyclic_start']) for r in tr['pairs'] for z in (r['left'],r['right'])};needed_physical={(f['history_index'],f['exposing_bridge_chart']['cyclic_start']) for q in physical['representatives'] for f in q['source_facets']};needed=sorted(needed_hidden|needed_physical);anchors={}
for h,start in needed:
 Cb=bridge(ba[(h,start)],A);Cp=polygon(byh[h]['cell_key'],start,U);Cb0=Cb.subs(vals);uv=dict(zip(U,extract(byh[h]['cell_key'],start,Cb0)));piv=next((i,j) for i in range(n) for j in range(i+1,n) if s.det(Cb[:,[i,j]])!=0 and s.det(Cp[:,[i,j]])!=0);Nb=Cb[:,list(piv)].inv()*Cb;Np=Cp[:,list(piv)].inv()*Cp;coordsb=[Nb[i,j] for i in range(2) for j in range(n) if j not in piv];coordsp=[Np[i,j] for i in range(2) for j in range(n) if j not in piv];Jb=s.Matrix(coordsb).jacobian(A)*s.diag(*A);Jp=s.Matrix(coordsp).jacobian(U)*s.diag(*U);Jbn=Jb.subs(vals);chosen=[]
 for q in range(len(coordsb)):
  if s.Matrix([Jbn[i,:] for i in chosen+[q]]).rank()>len(chosen):chosen.append(q)
  if len(chosen)==8:break
 db=s.factor(s.Matrix([Jbn[i,:] for i in chosen]).det());dp=s.factor(s.Matrix([Jp.subs(uv)[i,:] for i in chosen]).det());ratio=s.factor(db/dp);sgn=int(s.sign(ratio));seedsgn=sgn*pa[(h,start)]['dlog_jacobian_sign'];anchors[(h,start)]={'history':h,'cyclic_start':start,'bridge_to_polygon_jacobian_at_sample':str(ratio),'bridge_to_polygon_sign':sgn,'polygon_to_seed_sign':pa[(h,start)]['dlog_jacobian_sign'],'bridge_to_seed_sign':seedsgn};print(h,start,sgn,seedsgn,flush=True)
rows=[]
for r in tr['pairs']:
 L,Q=r['left'],r['right'];ol=anchors[(L['history'],L['cyclic_start'])]['bridge_to_seed_sign'];oq=anchors[(Q['history'],Q['cyclic_start'])]['bridge_to_seed_sign'];J=int(r['log_jacobian']);sl=ol*(-1)**(L['coordinate']-1);sr=oq*J*(-1)**(Q['coordinate']-1);rows.append({**r,'left_seed_oriented_residue_sign':sl,'right_in_left_seed_orientation_sign':sr,'cancels':sl+sr==0})
checks={'all_needed_charts':len(anchors)==len(needed),'seventeen_pairs':len(rows)==17,'all_bridge_jacobians_unit_sign':all(abs(x['bridge_to_polygon_sign'])==1 for x in anchors.values()),'all_oriented_residues_cancel':all(x['cancels'] for x in rows)};out={'schema':'marici.nima.n8-bcfw-bridge-orientation-anchors.v1','anchors':list(anchors.values()),'pairs':rows,'checks':checks,'passed':all(checks.values())};p=R/'research/nima/results/n8-bcfw-bridge-orientation-anchors.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
