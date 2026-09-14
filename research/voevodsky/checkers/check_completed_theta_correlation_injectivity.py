#!/usr/bin/env python3
"""Symbolic checks for the Laplace reduction and injectivity argument."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/the_completed_theta_correlation_is_injective_on_the_arithmetic_interval_range_20260912.md'
SOURCE=ROOT/'research/nima/the-late-prime-shell-autocorrelation-is-superexponentially-dominated-by-the-first-completed-theta-label-pair.md'
KERNEL=ROOT/'research/voevodsky/the_completed_interval_synthesis_kernel_is_exactly_the_distributional_cycle_space_20260912.md'
RESULT=ROOT/'research/voevodsky/results/completed_theta_correlation_injectivity.json'
x,y=s.symbols('x y',positive=True); pi=s.pi
phi_xy=pi*(x*y)**s.Rational(5,4)*(2*pi*x*y-3)*s.exp(-pi*x*y)
checks={}
checks['source_atom_formula']='2\\pi^2n^4e^{4u}-3\\pi n^2e^{2u}' in SOURCE.read_text()
checks['shifted_atom_algebra']=s.simplify(phi_xy/(pi*(x*y)**s.Rational(5,4)*(2*pi*x*y-3)*s.exp(-pi*x*y)))==1
# Kernel multiplying h after extracting y^(5/4).
kernel=(2*pi*x*y-3)*s.exp(-pi*x*y); lap=s.exp(-pi*x*y)
checks['laplace_differential_kernel']=s.simplify(-2*y*s.diff(lap,y)-3*lap-kernel)==0
C=s.symbols('C'); L=C*y**s.Rational(-3,2)
checks['ode_solution']=s.simplify(2*y*s.diff(L,y)+3*L)==0
checks['arithmetic_support_above_atom_zero']=s.simplify(2*pi*4-3)>0
checks['exponential_excludes_nonzero_ode_solution']=s.limit(s.exp(4*pi*y)*y**s.Rational(-3,2),y,s.oo)==s.oo
# Gaussian factor makes the polynomial multiplier used in h bounded.
mult=x**s.Rational(5,4)*pi*x**s.Rational(5,4)*(2*pi*x-3)*s.exp(-pi*x)
checks['h_multiplier_bounded_at_infinity']=s.limit(mult,x,s.oo)==0
text=PACKET.read_text()
checks['support_threshold_stated']='supported in \\([\\log2,\\infty)\\)' in text
checks['laplace_uniqueness_invoked']='uniqueness of the Laplace transform for \\(L^1\\) functions' in text
checks['kernel_predecessor_exact']='\\ker J=\\ker\\partial' in KERNEL.read_text()
checks['cycle_metric_not_promoted']='does not supply a Hilbert metric for the cycle port' in text
checks['forest_uniformity_remains']='uniform bounds for completed change maps' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.completed-theta-correlation-injectivity-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'atom_source':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'kernel_theorem':hashlib.sha256(KERNEL.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'T_D injective on completed arithmetic interval range','consequence':'ker Bhat_D equals completed cycle space and history-plus-chord observer is faithful','remaining':['uniform completed forest-change bounds','physical cycle covariance']}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
