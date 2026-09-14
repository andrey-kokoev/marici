#!/usr/bin/env python3
"""Exact finite models for history pullback geometry and cycle radical."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/history_induces_a_canonical_hilbert_geometry_only_on_the_cycle_quotient_20260912.md'
INJECT=ROOT/'research/voevodsky/the_completed_theta_correlation_is_injective_on_the_arithmetic_interval_range_20260912.md'
GLOBAL=ROOT/'research/voevodsky/a_symmetric_arithmetic_grade_constructs_an_all_ratio_history_carrier_20260912.md'
RESULT=ROOT/'research/voevodsky/results/history_cycle_quotient_geometry.json'
checks={}
# Connected graph incidence is a finite model of a history map with cycle kernel.
for n,B in ((3,s.Matrix([[-1,0,-1],[1,-1,0],[0,1,1]])),(4,s.Matrix([[-1,0,0,-1,0],[1,-1,0,0,-1],[0,1,-1,0,0],[0,0,1,1,1]]))):
 G=B.T*B; kernel=B.nullspace(); checks[f'positive_semidefinite_{n}']=all(ev>=0 for ev in G.eigenvals())
 checks[f'radical_equals_cycle_{n}']=G.nullspace()==kernel
 checks[f'quotient_rank_{n}']=G.rank()==B.rank()
 # Adding a cycle changes neither the history vector nor pullback pairing.
 if kernel:
  z=kernel[0]; c=s.ones(B.cols,1); checks[f'quotient_well_defined_{n}']=B*(c+z)==B*c and ((c+z).T*G*(c+z))[0]==(c.T*G*c)[0]
 # Positive cycle norm cannot be obtained by restricting the pullback form.
 checks[f'cycle_has_zero_history_length_{n}']=all((z.T*G*z)[0]==0 for z in kernel)
text=PACKET.read_text()
inject_text=INJECT.read_text(); checks['kernel_theorem_dependency']=all(token in inject_text for token in ('\\ker\\widehat B_D','\\ker J','\\ker\\partial'))
checks['global_hilbert_dependency']='\\mathcal H_{\\mathrm{all}}' in GLOBAL.read_text()
checks['closed_range_not_promoted']='does not assert that the image is closed' in text
checks['quotient_completion_identified']='Hilbert completion of this normed quotient is canonically isometric' in text
checks['no_cycle_covariance_fabricated']='does not determine a metric on the kernel' in text
checks['acceptance_test_typed']='compatible with reciprocal action, cutoff inclusions, and completed forest changes' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.history-cycle-quotient-geometry-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'injectivity':hashlib.sha256(INJECT.read_bytes()).hexdigest(),'global_history':hashlib.sha256(GLOBAL.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'derived':'canonical pre-Hilbert norm on source quotient by cycles and Hilbert completion as history-range closure','radical':'exactly completed cycle space','not_derived':'positive cycle covariance or orthogonal augmented decomposition'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
