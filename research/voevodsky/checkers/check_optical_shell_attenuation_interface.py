#!/usr/bin/env python3
"""Finite operator checks for the optical shell-attenuation interface."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/optical_attenuation_can_realize_the_shell_probe_only_after_a_label_mode_embedding_20260912.md'
ASPECT=ROOT/'research/aspect/continuous-mode-optical-attachment-pullback.md'
RESULT=ROOT/'research/voevodsky/results/optical_shell_attenuation_interface.json'
checks={}
for labels in ((1,2,3),(1,1,2,3,5)):
 t=s.Rational(2,3); V=s.diag(*[t**j for j in labels]); I=s.eye(len(labels)); loss=I-V.T*V
 checks[f'contraction_{len(labels)}']=all(0<V[i,i]<1 for i in range(V.rows))
 checks[f'loss_positive_{len(labels)}']=loss.is_positive_definite is True
 checks[f'normalization_{len(labels)}']=V.T*I*V+loss==I
 # Conjugation composition with a second passive diagonal map.
 W=s.diag(*[s.Rational(3,4)**j for j in labels]); E=s.diag(*[s.Rational(i+1,len(labels)+1) for i in range(len(labels))])
 checks[f'contravariant_composition_{len(labels)}']=(W*V).T*E*(W*V)==V.T*(W.T*E*W)*V
 # Exact intertwiner example exists only when an explicit label-preserving embedding is supplied.
 iota=s.eye(len(labels)); checks[f'typed_identity_example_{len(labels)}']=V*iota==iota*V
aspect=ASPECT.read_text(); text=PACKET.read_text()
checks['aspect_contraction_source']='Lossy passive propagation is represented by a contraction' in aspect
checks['aspect_loss_source']='E_{\\rm loss}=I_{H_p}-V^*V' in aspect
checks['loss_retained']='no-detection events are retained' in text
checks['embedding_is_missing']='No such embedding is currently sourced' in text
checks['two_intertwining_equations']='These two commuting equations are the acceptance test' in text
checks['dimension_not_authority']='Equal dimensions, a tunable filter, or a formally similar attenuation curve do not construct \\(\\iota\\)' in text
checks['conditioning_warning']='Renormalizing only detected events would condition on survival' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.optical-shell-attenuation-interface-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'aspect_source':hashlib.sha256(ASPECT.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'compatible':'finite shell modulation is a passive contraction with explicit loss effect','missing':'source-derived shell-label-preserving optical embedding and detector intertwiner','not_established':'laboratory realization or physical cycle covariance'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
