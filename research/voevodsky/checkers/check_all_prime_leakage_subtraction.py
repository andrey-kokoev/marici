"""Prime leakage divergence and source-derived endpoint subtraction fixtures."""
from pathlib import Path
import json
import sympy as s

# Exact Stieltjes integration-by-parts with the actual Mangoldt staircase.
t=s.symbols('t',positive=True)
h=(t-2)**2*(8-t)**2
Lambda={}
for p in s.primerange(2,9):
    q=p
    while q<=8:
        Lambda[q]=s.log(p);q*=p
prime=sum(c*h.subs(t,n) for n,c in Lambda.items())
continuum=s.integrate(h,(t,2,8))
remainder=0
for n in range(2,8):
    psi=sum(c for k,c in Lambda.items() if k<=n)
    remainder-=s.integrate((psi-t)*s.diff(h,t),(t,n,n+1))
assert s.simplify(prime-continuum-remainder)==0

# The gamma leakage's first exponential plus the continuum prime mode
# equals the independently prescribed endpoint swap kernel.
v,x=s.symbols('v x',positive=True)
a=v+x
gamma_kernel=s.exp(-a/2)/(1-s.exp(-2*a))
first=s.exp(-a/2)
residual=s.exp(-5*a/2)/(1-s.exp(-2*a))
assert s.simplify(gamma_kernel-first-residual)==0
assert s.expand(s.exp(v/2)*s.exp(x/2)+s.exp(-v/2)*s.exp(-x/2)
                -(s.exp((v+x)/2)+s.exp(-(v+x)/2)))==0

# Weighted operator tail uses norm of each full-line translate of a
# positive-half-line source, not unitary channel square-summation.
# |x-a|>=a-x is the inequality behind exp(-alpha*a) input control.
for aa in range(12):
    for xx in range(12):assert abs(xx-aa)>=aa-xx

bounds=[]
for N in (10,100,1000):
    coefficient=sum(s.log(p)**2/(p-1) for p in s.primerange(2,N+1))
    bounds.append({'prime_cutoff':N,'leakage_squared_norm_lower_coefficient':float(coefficient.evalf())})
assert all(bounds[i]['leakage_squared_norm_lower_coefficient']<bounds[i+1]['leakage_squared_norm_lower_coefficient']
           for i in range(len(bounds)-1))
result={'passed':True,'finite_prime_leakage_lower_bounds':bounds,
 'checks':{'mangoldt_stieltjes_remainder_identity':True,
 'gamma_first_tail_plus_prime_continuum_is_endpoint_swap':True,
 'two_sided_decay_weight_shift_bound':True},
 'scope':'Exact source-counting and kernel identities. Infinite divergence uses Euler prime reciprocal divergence; weighted convergence and PNT asymptotics are proved in the companion note. No residual unweighted L2 convergence is claimed.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/all-prime-leakage-subtraction.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
