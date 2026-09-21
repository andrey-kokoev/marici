"""Exact one-slot prime-shift identities and weighted-domain conventions."""
from pathlib import Path
import json
import sympy as s
z,wb,a,gamma=s.symbols('z wbar a gamma', real=False)
u=s.symbols('u',real=True)
sz=s.Rational(1,2)-s.I*z
tw=s.Rational(1,2)+s.I*wb
d=sz+tw-1
assert s.simplify(d+s.I*(z-wb))==0
# The source-defined shift e^(-a/2) f(u+a) acts on k_z by e^(-a*s_z).
assert s.simplify(s.exp(-a/2)*s.exp(s.I*z*(u+a))
                  -s.exp(-a*sz)*s.exp(s.I*z*u))==0
# Polarization uses the UNWEIGHTED integral although H_gamma controls domain.
assert s.simplify((s.exp(-a*sz)+s.exp(-a*tw))/d
                  -(s.exp(-a*sz)+s.exp(-a*tw))/(-s.I*(z-wb)))==0
assert s.simplify(1/d-1/(d-2*gamma))!=0

A=(s.I*s.Matrix([[-1,1,1,1],[-1,1,-1,-1]])/2)*s.diag(s.I,-s.I,s.I,-s.I)
# Fixed sheet sum, not a chosen kernel fit.
assert s.Matrix([[1,1]])*A==s.Matrix([[1,1,0,0]])

# Exact prime-power coefficients for a finite independent shift constructor.
N=64
terms={}
for p in s.primerange(2,N+1):
    q=p
    while q<=N:
        terms[q]=s.log(p)
        q*=p
assert terms[4]==s.log(2) and terms[27]==s.log(3) and 6 not in terms
# The elementary tail integral used for operator-norm convergence.
x=s.symbols('x',positive=True)
cut=s.symbols('N',positive=True)
sigma=s.symbols('sigma',positive=True)
F=x**(1-sigma)*(s.log(x)/(sigma-1)+1/(sigma-1)**2)
assert s.simplify(s.diff(F,x)+s.log(x)*x**(-sigma))==0
result={'passed':True,'prime_power_shifts_at_cutoff_64':len(terms),
 'checks':{'source_shift_eigenvalue_matches_n_to_minus_s':True,
 'unweighted_green_denominator_retained':True,
 'weighted_inner_product_substitution_rejected':True,
 'fixed_sheet_projection_extracts_even_trace':True,
 'operator_tail_integral_identity':True},
 'scope':'Exact source-shift and polarization identities. Weighted operator convergence and the full-theta prime-channel comparison are proved in the companion note; no full Tate operator equivalence.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/euler-prime-shift-operator.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
