#!/usr/bin/env python3
"""Ranks shell-only, scale-only, and combined modulation probes on cycle space."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/'research/voevodsky/results/coarse_label_modulation_detection.json'
PACKET=ROOT/'research/voevodsky/coarse_shell_and_scale_modulations_detect_route_residue_20260912.md'
primes=(2,3,5,7,11,13,17); shells=list(zip(primes,primes[1:])); cutoffs=(120,240,480); checks={}; census={}
for L in cutoffs:
 E=sorted([(k*p*q,j,k,p,q) for j,(p,q) in enumerate(shells) for k in range(1,L+1) if k*p*q<=L]); V=sorted({k*p for w,j,k,p,q in E}|{k*q for w,j,k,p,q in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E))
 for col,(w,j,k,p,q) in enumerate(E): B[vi[k*p],col]-=1; B[vi[k*q],col]+=1
 F=s.Matrix.hstack(*B.nullspace()); beta=F.cols
 def stack_for(index):
  values=sorted({e[index] for e in E}); blocks=[]
  for val in values:
   D=s.diag(*[1 if e[index]==val else 0 for e in E]); blocks.append(B*D*F)
  return s.Matrix.vstack(*blocks),len(values)
 shell,ns=stack_for(1); scale,nk=stack_for(2); both=s.Matrix.vstack(shell,scale)
 # One generic integer-coded modulation in each class.
 Ds=s.diag(*[e[1]+1 for e in E]); Dk=s.diag(*[e[2] for e in E]); generic=s.Matrix.vstack(B*Ds*F,B*Dk*F)
 ranks={'beta':beta,'shell':shell.rank(),'scale':scale.rank(),'combined':both.rank(),'generic_shell':(B*Ds*F).rank(),'generic_scale':(B*Dk*F).rank(),'two_generic':generic.rank(),'shell_channels':ns,'scale_channels':nk,'edges':len(E)}; census[str(L)]=ranks
 checks[f'shell_family_faithful_{L}']=ranks['shell']==beta
 checks[f'scale_family_faithful_{L}']=ranks['scale']==beta
 checks[f'combined_family_faithful_{L}']=ranks['combined']==beta
 checks[f'generic_shell_faithful_{L}']=ranks['generic_shell']==beta
 checks[f'generic_scale_faithful_{L}']=ranks['generic_scale']==beta
 checks[f'two_generic_faithful_{L}']=ranks['two_generic']==beta
 # Any family rank cannot exceed stacked output rank.
 checks[f'ranks_bounded_{L}']=all(0<=ranks[k]<=beta for k in ('shell','scale','combined','generic_shell','generic_scale','two_generic'))
text=PACKET.read_text() if PACKET.exists() else ''
if text:
 checks['packet_matches_census']='finite-cutoff census' in text
 checks['no_unbounded_promotion']='does not prove one fixed finite probe family detects the unbounded completion' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.coarse-label-modulation-detection-check.v1','input_digest':hashlib.sha256(PACKET.read_bytes()).hexdigest() if PACKET.exists() else None,'checks':checks,'passed':all(checks.values()),'census':census,'disposition':{}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'census':census})); raise SystemExit(0 if result['passed'] else 1)
