#!/usr/bin/env python3
"""Exact functorial cancellation of the 15 nonstandard and one quartic image."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
ori=json.loads((R/'research/nima/results/n8-polygon-chart-orientation-anchors.json').read_text());hidden=json.loads((R/'research/nima/results/n8-hidden-internal-facet-resolution.json').read_text());matches=json.loads((R/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];byh={x['history_index']:x for x in matches};wanted={tuple(x['boundary_permutation']):x for x in hidden['one_sided_internal_facets']};A=s.symbols('a1:9');B=s.symbols('b1:9');n=8
def chart(key,start,v,zero):
 groups=[list(g) for g in key['parallel_classes']];pos=lambda x:(x-start)%n;groups.sort(key=lambda g:min(pos(x) for x in g));groups=[sorted(g,key=pos) for g in groups];C=s.zeros(2,n);idx=0;dirs=[s.Matrix([1,0])];t=0
 for gi in range(1,len(groups)-1):d=0 if idx==zero else v[idx];idx+=1;t+=d;dirs.append(s.Matrix([1,t]))
 dirs.append(s.Matrix([0,1]))
 for gi,g in enumerate(groups):
  for qi,label in enumerate(g):
   fixed=qi==0 and gi in (0,len(groups)-1);scale=1 if fixed else (0 if idx==zero else v[idx]);idx+=not fixed;C[:,label-1]=(-1 if label<start else 1)*scale*dirs[gi]
 return C
rows=[]
for r in ori['pairs']:
 f=tuple(r['boundary_permutation'])
 if f not in wanted:continue
 L,Q=r['left'],r['right'];e1=L['coordinate']-1;e2=Q['coordinate']-1;C1=chart(byh[L['history']]['cell_key'],L['cyclic_start'],A,e1);C2=chart(byh[Q['history']]['cell_key'],Q['cyclic_start'],B,e2);sub={x:s.sympify(r['transition'][str(x)],locals={str(y):y for y in A}) for i,x in enumerate(B) if i!=e2};C2=C2.subs(sub);piv=next((i,j) for i in range(n) for j in range(i+1,n) if s.det(C1[:,[i,j]])!=0 and s.det(C2[:,[i,j]])!=0);N1=C1[:,list(piv)].inv()*C1;N2=C2[:,list(piv)].inv()*C2;equal=all(s.factor(N1[i,j]-N2[i,j])==0 for i in range(2) for j in range(n));sl=r['left_seed_oriented_residue_sign'];sr=r['right_in_left_seed_orientation_sign'];rows.append({'boundary_permutation':list(f),'histories':[L['history'],Q['history']],'visible_branch':wanted[f]['visible_branches'][0],'common_source_pivot':[x+1 for x in piv],'exact_same_source_facet_map':equal,'left_oriented_residue_sign':sl,'right_oriented_residue_sign':sr,'residue_sum':sl+sr,'transported_residue_cancels':equal and sl+sr==0});print(L['history'],Q['history'],equal,sl,sr,flush=True)
checks={'sixteen_nonphysical_internal_images':len(rows)==16,'fifteen_nonstandard_plus_one_quartic':sum(x['visible_branch'].get('nonstandard',False) for x in rows)==15 and sum(x['visible_branch'].get('unlabelled',False) for x in rows)==1,'exact_same_source_maps':all(x['exact_same_source_facet_map'] for x in rows),'opposite_oriented_residues':all(x['residue_sum']==0 for x in rows),'all_transported_residues_cancel':all(x['transported_residue_cancels'] for x in rows)};out={'schema':'marici.nima.n8-nonphysical-transported-residue-cancellation.v1','pairs':rows,'checks':checks,'passed':all(checks.values()),'argument':'For each pair the exact transition identifies the normalized C matrices, hence identifies Y=CZ for arbitrary Z. Pushforward is linear on oriented forms. Equal source-facet canonical forms with opposite residue signs therefore have identically cancelling transported rational differential forms.'};p=R/'research/nima/results/n8-nonphysical-transported-residue-cancellation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
