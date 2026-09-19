#!/usr/bin/env python3
"""BCFW-bridge proof of cancellation for 15 nonstandard plus one quartic image."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'));import sympy as s
ori=json.loads((R/'research/nima/results/n8-bcfw-bridge-orientation-anchors.json').read_text());hidden=json.loads((R/'research/nima/results/n8-hidden-internal-facet-resolution.json').read_text());atlas=json.loads((R/'research/nima/results/n8-complete-cyclic-bcfw-bridge-atlas.json').read_text());wanted={tuple(x['boundary_permutation']):x for x in hidden['one_sided_internal_facets']};lookup={(x['history_index'],x['cyclic_start']):x for x in atlas['charts']};A=s.symbols('a1:9');B=s.symbols('b1:9');n=8
def matrix(c,v,zero):
 D=s.zeros(2,n);p,q=[x-1 for x in c['decorated_identity_sources']];D[0,p]=1;D[1,q]=1
 for i,z in enumerate(c['bridge_word']):D[:,z['destination']-1]+=z['sign']*(0 if i==zero else v[i])*D[:,z['source']-1]
 r=c['cyclic_start']-1;C=s.zeros(2,n)
 for i in range(n):C[:,(i+r)%n]=(-1 if i+r>=n else 1)*D[:,i]
 return C
rows=[]
for r in ori['pairs']:
 f=tuple(r['boundary_permutation'])
 if f not in wanted:continue
 L,Q=r['left'],r['right'];C1=matrix(lookup[(L['history'],L['cyclic_start'])],A,L['coordinate']-1);C2=matrix(lookup[(Q['history'],Q['cyclic_start'])],B,Q['coordinate']-1);sub={x:s.sympify(r['transition'][str(x)],locals={str(y):y for y in A}) for i,x in enumerate(B) if i!=Q['coordinate']-1};C2=C2.subs(sub);piv=next((i,j) for i in range(n) for j in range(i+1,n) if s.det(C1[:,[i,j]])!=0 and s.det(C2[:,[i,j]])!=0);N1=C1[:,list(piv)].inv()*C1;N2=C2[:,list(piv)].inv()*C2;equal=all(s.factor(N1[i,j]-N2[i,j])==0 for i in range(2) for j in range(n));sl=r['left_seed_oriented_residue_sign'];sr=r['right_in_left_seed_orientation_sign'];rows.append({'boundary_permutation':list(f),'histories':[L['history'],Q['history']],'visible_branch':wanted[f]['visible_branches'][0],'exact_same_C_map':equal,'left_sign':sl,'right_sign':sr,'transported_residue_cancels':equal and sl+sr==0})
checks={'sixteen_images':len(rows)==16,'fifteen_nonstandard_one_quartic':sum(x['visible_branch'].get('nonstandard',False) for x in rows)==15 and sum(x['visible_branch'].get('unlabelled',False) for x in rows)==1,'all_exact_C_maps_equal':all(x['exact_same_C_map'] for x in rows),'all_opposite_signs':all(x['left_sign']+x['right_sign']==0 for x in rows),'all_transported_forms_cancel':all(x['transported_residue_cancels'] for x in rows)};out={'schema':'marici.nima.n8-nonphysical-bcfw-transported-cancellation.v1','pairs':rows,'checks':checks,'passed':all(checks.values()),'argument':'Exact bridge transitions identify C modulo GL(2), hence Y=CZ for arbitrary Z. Opposite anchored canonical residues therefore push forward to identically cancelling rational differential forms.'};p=R/'research/nima/results/n8-nonphysical-bcfw-transported-cancellation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
