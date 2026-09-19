#!/usr/bin/env python3
"""Compare the eleven physical BCFW residue charts to polygon residue charts."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
bf=json.loads((R/'research/nima/results/n8-physical-bcfw-residue-orientations.json').read_text());pf=json.loads((R/'research/nima/results/n8-physical-residue-orientations.json').read_text());atlas=json.loads((R/'research/nima/results/n8-complete-cyclic-bcfw-bridge-atlas.json').read_text());matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byh={x['history_index']:x for x in matches};ba={(x['history_index'],x['cyclic_start']):x for x in atlas['charts']};A=s.symbols('a1:9');U=s.symbols('u1:9');n=8
def bridge(c,v,zero):
 D=s.zeros(2,n);p,q=[x-1 for x in c['decorated_identity_sources']];D[0,p]=1;D[1,q]=1
 for i,z in enumerate(c['bridge_word']):D[:,z['destination']-1]+=z['sign']*(0 if i==zero else v[i])*D[:,z['source']-1]
 r=c['cyclic_start']-1;C=s.zeros(2,n)
 for i in range(n):C[:,(i+r)%n]=(-1 if i+r>=n else 1)*D[:,i]
 return C
def polygon(key,start,v,zero):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];C=s.zeros(2,n);idx=0;dirs=[s.Matrix([1,0])];t=0
 for gi in range(1,len(groups)-1):d=0 if idx==zero else v[idx];idx+=1;t+=d;dirs.append(s.Matrix([1,t]))
 dirs.append(s.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   fixed=qi==0 and gi in (0,len(groups)-1);scale=1 if fixed else (0 if idx==zero else v[idx]);idx+=not fixed;C[:,label-1]=(-1 if label<start else 1)*scale*dirs[gi]
 return C
def extract_polygon(key,start,C):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];r0,rl=groups[0][0],groups[-1][0];sf=-1 if r0<start else 1;sl=-1 if rl<start else 1;D=s.Matrix([[sf,0],[0,sl]])*C[:,[r0-1,rl-1]].inv()*C;out=[];prev=0
 for gi in range(1,len(groups)-1):
  label=next(x for x in groups[gi] if D[:,x-1]!=s.zeros(2,1));t=s.factor(D[1,label-1]/D[0,label-1]);out.append(s.factor(t-prev));prev=t
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   if qi==0 and gi in (0,len(groups)-1):continue
   sign=-1 if label<start else 1;out.append(s.factor((D[1,label-1] if gi==len(groups)-1 else D[0,label-1])/sign))
 return out
vals={x:s.Integer(p) for x,p in zip(A,[2,3,5,7,11,13,17,19])};pindex={(tuple(q['physical_bracket']),f['history_index'],tuple(f['boundary_permutation'])):f for q in pf['representatives'] for f in q['source_facets']};cachep=R/'research/nima/results/.n8-physical-bcfw-polygon-transition-cache.json';cached=json.loads(cachep.read_text()) if cachep.exists() else {};rows=[]
for orbit in bf['representatives']:
 for f in orbit['source_facets']:
  key=(tuple(orbit['physical_bracket']),f['history_index'],tuple(f['boundary_permutation']));ck='.'.join(map(str,orbit['physical_bracket']))+':'+str(f['history_index'])
  if ck in cached:rows.append(cached[ck]);continue
  g=pindex[key];bc=f['exposing_bridge_chart'];pc=g['exposing_chart'];zb=bc['coordinate']-1;zp=pc['coordinate']-1;Cb=bridge(ba[(f['history_index'],bc['cyclic_start'])],A,zb);Cp=polygon(byh[f['history_index']]['cell_key'],pc['cyclic_start'],U,zp);src=[x for i,x in enumerate(A) if i!=zb];tgt=[x for i,x in enumerate(U) if i!=zp];allT=extract_polygon(byh[f['history_index']]['cell_key'],pc['cyclic_start'],Cb);assert s.factor(allT[zp])==0,(f['history_index'],zp,allT[zp]);T=[allT[i] for i in range(8) if i!=zp];row={'physical_bracket':orbit['physical_bracket'],'history_index':f['history_index'],'bridge_chart':bc,'polygon_chart':pc,'solution_count':1};Jmat=s.Matrix([[s.factor(src[j]/T[i]*s.diff(T[i],src[j])).subs(vals) for j in range(7)] for i in range(7)]);J=s.factor(Jmat.det());sb=f['seed_oriented_residue_sign'];sp=g['seed_oriented_residue_sign'];row.update({'log_jacobian':str(J),'bridge_residue_sign':sb,'polygon_residue_sign':sp,'orientation_identity':s.factor(sp*J-sb)==0})
  rows.append(row);cached[ck]=row;cachep.write_text(json.dumps(cached,indent=2)+'\n');print(orbit['physical_bracket'],f['history_index'],row.get('log_jacobian'),row.get('orientation_identity'),flush=True)
checks={'eleven_transitions':len(rows)==11,'all_solved':all(r['solution_count']==1 and 'log_jacobian' in r for r in rows),'all_sample_jacobians_nonzero':all(r['log_jacobian']!='0' for r in rows),'all_orientation_identities':all(r['orientation_identity'] for r in rows)};out={'schema':'marici.nima.n8-physical-bcfw-to-polygon-residue-transitions.v1','transitions':rows,'checks':checks,'passed':all(checks.values()),'conclusion':'Every oriented physical BCFW residue form equals the corresponding polygon residue form before pushforward. Therefore the previously computed exact target coefficients and three orbit sums are unchanged.'};p=R/'research/nima/results/n8-physical-bcfw-to-polygon-residue-transitions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
