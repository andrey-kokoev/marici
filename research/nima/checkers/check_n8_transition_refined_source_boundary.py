#!/usr/bin/env python3
"""Canonical n=8 source boundary with twisted cyclic signs and exact transition orientations."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
tr=json.loads((ROOT/'research/nima/results/n8-all-shared-boundary-transitions.json').read_text());matches=json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches'];a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
M={'F':s.Matrix([[1,A1+A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,1,A5,A6,A7,A8]]),'G':s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'H':s.Matrix([[1,A1,A2+A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]),'A':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'B':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'C':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,A4*A7,0],[0,0,0,1,A5,A6,A7,A8]]),'D':s.Matrix([[1,A1,A2,A3+A4,(A3+A4)*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]]),'E':s.Matrix([[1,A1,A2,A3+A4,A4*A5,A4*A6,0,0],[0,0,0,1,A5,A6,A7,A8]])}
def embed(q,X):
 e=q['embedding'];sup=list(range(1,9)) if isinstance(e,int) else e['support'];rot=e if isinstance(e,int) else e['rotation'];O=s.zeros(2,8)
 for j in range(X.cols):O[:,sup[(j+rot)%len(sup)]-1]=(-1 if j+rot>=len(sup) else 1)*X[:,j]
 return O
vals={x:s.Integer(p) for x,p in zip(a,[2,3,5,7,11,13,17,19])};rows=[]
for q in matches:
 C0=embed(q,M[q['seed_type']])
 for e,x in enumerate(a,1):
  C=C0.subs(x,0);free=[v for v in a if v!=x];piv=next((i,j) for i in range(8) for j in range(i+1,8) if s.det(C[:,[i,j]]).subs(vals)!=0);N=s.simplify(C[:,list(piv)].inv()*C);coords=[N[i,j] for i in range(2) for j in range(8) if j not in piv];rank=s.Matrix(coords).jacobian(free).subs(vals).rank();rows.append({'history_index':q['history_index'],'seed':q['seed_type'],'alpha':e,'raw_residue_orientation':(-1)**(e-1),'source_grassmannian_rank':rank})
by={(r['history_index'],r['alpha']):r for r in rows};pairs=[];adj={i:[] for i in range(20)};internal=set()
for r in tr['pairs']:
 if r.get('positive_orthant_classification')!='positive_to_positive':continue
 L=(r['left']['history'],r['left']['alpha']);R=(r['right']['history'],r['right']['alpha']);det=s.Integer(r['log_jacobian']);assert by[L]['source_grassmannian_rank']==by[R]['source_grassmannian_rank']==7
 # sL*oL + sR*oR*det=0.
 ratio=int(-by[L]['raw_residue_orientation']*by[R]['raw_residue_orientation']*det);adj[L[0]].append((R[0],ratio));adj[R[0]].append((L[0],ratio));internal|={L,R};pairs.append({'left':L,'right':R,'log_jacobian':str(det),'required_history_sign_ratio':ratio})
signs={};conflicts=[]
for start in range(20):
 if start in signs:continue
 signs[start]=1;stack=[start]
 while stack:
  u=stack.pop()
  for v,r in adj[u]:
   want=signs[u]*r
   if v in signs and signs[v]!=want:conflicts.append([u,v])
   elif v not in signs:signs[v]=want;stack.append(v)
for p in pairs:
 L,R=tuple(p['left']),tuple(p['right']);p['transported_residue_sum']=signs[L[0]]*by[L]['raw_residue_orientation']+signs[R[0]]*by[R]['raw_residue_orientation']*int(p['log_jacobian'])
external=[];degenerate=[]
for r in rows:
 rr=dict(r);rr['history_orientation_sign']=signs[r['history_index']];rr['coefficient']=signs[r['history_index']]*r['raw_residue_orientation']
 if r['source_grassmannian_rank']<7:degenerate.append(rr)
 elif (r['history_index'],r['alpha']) not in internal:external.append(rr)
checks={'all_160_coordinate_limits_ranked':len(rows)==160,'twentythree_internal_rank7_pairs':len(pairs)==23,'all_internal_residues_cancel':all(p['transported_residue_sum']==0 for p in pairs),'orientation_system_consistent':not conflicts,'fiftythree_rank6_chart_degenerations':len(degenerate)==53,'sixtyone_external_rank7_boundaries':len(external)==61,'partition_160':2*len(pairs)+len(degenerate)+len(external)==160}
out={'schema':'marici.nima.n8-transition-refined-source-boundary.v2','cyclic_embedding':'k=2 twisted cyclic wrap sign -1','internal_pairs':pairs,'history_orientation_signs':{str(k):v for k,v in signs.items()},'orientation_conflicts':conflicts,'coordinate_limit_rank_distribution':{str(k):sum(r['source_grassmannian_rank']==k for r in rows) for k in (6,7)},'rank6_chart_degenerations':degenerate,'external_branches':len(external),'external_chain_support':external,'checks':checks,'passed':all(checks.values()),'conclusion':'The canonical codimension-one source boundary has 61 branches after cancelling 23 exact positive rank-seven overlaps. Fifty-three rank-six coordinate limits are chart degenerations, not codimension-one positroid boundaries.'};p=ROOT/'research/nima/results/n8-transition-refined-source-boundary.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('external_chain_support','rank6_chart_degenerations','internal_pairs')},indent=2));raise SystemExit(0 if out['passed'] else 1)
