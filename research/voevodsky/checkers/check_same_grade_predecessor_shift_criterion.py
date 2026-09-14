#!/usr/bin/env python3
"""Verify the exact predecessor-shift characterization of same-grade cofaces."""
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/same_grade_cofaces_are_predecessor_shifts.md';RESULT=ROOT/'research/voevodsky/results/same_grade_predecessor_shift_criterion.json'
BASE=ROOT/'research/voevodsky/checkers/check_global_filtered_morse_preflight.py';scope={'__file__':str(BASE)};exec(BASE.read_text(encoding='utf-8').split('predictions={};sectors={}')[0],scope);build=scope['build'];PS=scope['PS'];LIMIT=scope['LIMIT']
def test(D):
 birth,cells,faces=build(D);cellset=set(birth);actual={c:set() for d in range(1,D) for c in cells[d]};same_lower=[]
 for d in range(2,D+1):
  for uppercell in cells[d]:
   base,J=uppercell
   for r,j in enumerate(J):
    I=J[:r]+J[r+1:];uf=(base*PS[j]//PS[j-1],I);lf=(base,I)
    if uf in actual and birth[uf]==birth[uppercell]:actual[uf].add(uppercell)
    if lf in birth and birth[lf]==birth[uppercell]:same_lower.append((lf,uppercell,j))
 mismatches=[];branchings=[];eligible_total=0
 for d in range(1,D):
  for c in cells[d]:
   base,I=c;m=max(I);pred=set()
   for j in range(1,m):
    if j not in I and base%PS[j]==0:
     candidate=(base*PS[j-1]//PS[j],tuple(sorted(I+(j,))))
     if candidate in cellset:pred.add(candidate)
   eligible_total+=len(pred)
   if pred!=actual[c]:mismatches.append({'cell':[base,list(I)],'predicted':len(pred),'actual':len(actual[c])})
   if len(pred)>1:branchings.append({'cell':[base,list(I)],'grade':birth[c],'eligible_directions':[next(iter(set(x[1])-set(I))) for x in sorted(pred,key=lambda x:x[1])]})
 return {'positive_cells':sum(len(cells[d]) for d in range(1,D+1)),'same_grade_upper_cofaces':eligible_total,'criterion_mismatches':len(mismatches),'same_grade_lower_cofaces':len(same_lower),'branching_cells':len(branchings),'maximum_branching':max((len(x['eligible_directions']) for x in branchings),default=0),'first_five_branchings':branchings[:5]}
sectors={str(D):test(D) for D in range(2,6)};checks={}
for D,r in ((int(k),v) for k,v in sectors.items()):checks[f'criterion_exact_D{D}']=r['criterion_mismatches']==0;checks[f'no_same_grade_lower_D{D}']=r['same_grade_lower_cofaces']==0
checks['nontrivial_branching_retained']=sum(r['branching_cells'] for r in sectors.values())>0;checks['scope_retained']='does not by itself prove that simultaneous choices form a complete acyclic matching' in PACKET.read_text(encoding='utf-8');checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.same-grade-predecessor-shift.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'sectors':sectors,'checks':checks,'passed':all(checks.values()),'disposition':{'theorem':'same-grade cofaces are exactly integral predecessor shifts below max shell','residual':'prove confluence of competing predecessor shifts'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'sectors':sectors,'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
