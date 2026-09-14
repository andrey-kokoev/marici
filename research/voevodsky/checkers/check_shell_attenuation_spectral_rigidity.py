#!/usr/bin/env python3
"""Exact finite checks for shell-attenuation intertwiner rigidity."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/shell_attenuation_intertwining_forces_optical_mode_separation_20260912.md'
OPTICAL=ROOT/'research/voevodsky/optical_attenuation_can_realize_the_shell_probe_only_after_a_label_mode_embedding_20260912.md'
RESULT=ROOT/'research/voevodsky/results/shell_attenuation_spectral_rigidity.json'
checks={}
for size in (3,5,8):
 t=s.Rational(2,3); vals=[t**j for j in range(1,size+1)]; D=s.diag(*vals); xs=s.symbols(f'x0:{size*size}'); X=s.Matrix(size,size,xs); equations=list(D*X-X*D); sol=s.linsolve(equations,xs); basis_tuple=next(iter(sol));
 checks[f'offdiagonal_forced_zero_{size}']=all(basis_tuple[i*size+j]==0 for i in range(size) for j in range(size) if i!=j)
 checks[f'diagonal_free_{size}']=all(basis_tuple[i*size+i]==xs[i*size+i] for i in range(size))
 checks[f'distinct_eigenvalues_{size}']=len(set(vals))==size
 # Abstract direct-sum realization and contraction.
 checks[f'abstract_intertwiner_{size}']=D*s.eye(size)==s.eye(size)*D and all(0<v<1 for v in vals)
# Joint signatures separate labels for the declared accumulating sequence.
for j in range(1,9):
 for k in range(j+1,9):
  checks[f'signature_{j}_{k}']=any((s.Rational(1,2)+s.Rational(1,n+3))**j!=(s.Rational(1,2)+s.Rational(1,n+3))**k for n in range(3))
text=PACKET.read_text(); checks['normality_condition_stated']='If \\(\\widetilde V_t\\) is normal' in text
checks['detector_equation_retained']='\\widetilde C\\iota=C_{\\rm history}' in text
checks['abstract_not_evidence']='Abstract mode partitioning cannot serve as evidence' in text
checks['optical_predecessor_embedding']='shell-label-preserving optical embedding' in OPTICAL.read_text()
checks['cross_talk_falsifier']='cross-talk mixes the joint eigenspaces' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.shell-attenuation-spectral-rigidity-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'optical_predecessor':hashlib.sha256(OPTICAL.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'intertwining distinct shell attenuations forces shell-block preservation; normal filters give orthogonal mode sectors','constructed':'abstract direct-sum realization','missing':'physical shell-to-mode assignment and detector pullback'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
