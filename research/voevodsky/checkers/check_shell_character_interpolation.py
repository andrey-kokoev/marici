#!/usr/bin/env python3
"""Exact-rational hostile for shell-character Vandermonde faithfulness."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/character_probe_kernel_as_shell_polynomial_interpolation.md'
RESULT=ROOT/'research/voevodsky/results/shell_character_interpolation.json'
SETTINGS=(Fraction(1),Fraction(5,6),Fraction(3,4),Fraction(7,10),Fraction(2,3))

def rank(a):
 a=[row[:] for row in a];r=0
 for c in range(len(a[0]) if a else 0):
  pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  r+=1
 return r

def determinant(a):
 a=[row[:] for row in a];d=Fraction(1)
 for c in range(len(a)):
  pivot=next((i for i in range(c,len(a)) if a[i][c]),None)
  if pivot is None:return Fraction(0)
  if pivot!=c:a[c],a[pivot]=a[pivot],a[c];d=-d
  q=a[c][c];d*=q
  for i in range(c+1,len(a)):
   factor=a[i][c]/q
   for j in range(c,len(a)):a[i][j]-=factor*a[c][j]
 return d

cases={};checks={}
for n in range(2,6):
 entries=[]
 for m in range(1,n+1):
  matrix=[[t**j for j in range(1,n+1)] for t in SETTINGS[:m]]
  actual=rank(matrix);entries.append({'evaluations':m,'rank':actual,'expected':m})
  checks[f'n{n}_m{m}_prefix_rank']=actual==m
 square=[[t**j for j in range(1,n+1)] for t in SETTINGS[:n]]
 det=determinant(square)
 checks[f'n{n}_determinant_nonzero']=det!=0
 cases[str(n)]={'prefixes':entries,'determinant':f'{det.numerator}/{det.denominator}'}
# Deliberate failure: duplicate the final setting in the five-by-five matrix.
bad=list(SETTINGS);bad[-1]=bad[-2]
bad_matrix=[[t**j for j in range(1,6)] for t in bad]
bad_rank=rank(bad_matrix);bad_det=determinant(bad_matrix)
checks['duplicate_setting_loses_rank']=bad_rank==4
checks['duplicate_setting_zero_determinant']=bad_det==0
text=PACKET.read_text(encoding='utf-8')
checks['augmentation_identification_not_claimed']='not yet an identification' in text
checks['prime_value_derivative_excluded']='not differentiation of the prime values' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.shell-character-interpolation.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'settings':[f'{x.numerator}/{x.denominator}' for x in SETTINGS],'cases':cases,'deliberate_failure':{'settings':[f'{x.numerator}/{x.denominator}' for x in bad],'rank':bad_rank,'determinant':f'{bad_det.numerator}/{bad_det.denominator}'},'checks':checks,'passed':all(checks.values()),'disposition':{'established':'exact interpolation faithfulness through five shell directions','residual':'comparison map from cubical boundary classes to an augmentation-graded object'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'checks':len(checks),'five_shell_determinant':cases['5']['determinant'],'duplicate_rank':bad_rank}))
raise SystemExit(0 if result['passed'] else 1)
