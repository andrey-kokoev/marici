"""Exact finite Taylor controls for the completion phase norm proof."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parents[1]
checks = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)
def c(n):
    return F((-1)**(n//2), factorial(n)) if n%2 == 0 else F(0)
def s(n):
    return F((-1)**((n-1)//2), factorial(n)) if n%2 else F(0)
def coefficient(k, N):
    return sum((c(j)*c(k-j)+s(j)*s(k-j) for j in range(max(0,k-N),min(N,k)+1)), F(0))

for n in range(128):
    check(f'derivative-recurrence/{n}',(n+1)*c(n+1)==-s(n) and (n+1)*s(n+1)==c(n))
for k in range(129):
    check(f'full-coefficient/{k}',coefficient(k,k)==(1 if k==0 else 0))
rows=[]
for B in (1,2,4,8):
    N=4*B
    for precision in (8,16,32):
        while 2*F((2*B)**(N+1),factorial(N+1)) > F(1,2**precision):
            N+=1
        bound=2*F((2*B)**(N+1),factorial(N+1))
        residual=sum(abs(coefficient(k,N))*B**k for k in range(1,2*N+1))
        check(f'low-degree-cancellation/{B}/{N}',all(coefficient(k,N)==0 for k in range(1,N+1)))
        check(f'coefficient-majorant/{B}/{N}',all(abs(coefficient(k,N))<=F(2**k,factorial(k)) for k in range(N+1,2*N+1)))
        check(f'geometric-tail/{B}/{N}',F(2*B,N+2)<=F(1,2))
        check(f'uniform-defect-bound/{B}/{N}',residual<=bound<=F(1,2**precision))
        rows.append({'radius':B,'precision_bits':precision,'degree':N,'norm_defect_bound':str(bound)})
result={'status':'pass','checks_passed':len(checks),'checks':checks,'bounds':rows,
        'claim':'For |x|<=B, |C_N(x)^2+S_N(x)^2-1| <= 2*(2B)^(N+1)/(N+1)! when N+2>=4B.',
        'proof_note':'research/nima/phase-pythagorean-series.md',
        'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ('checkers/check_phase_pythagorean_series.py', 'phase-pythagorean-series.md')},
        'remaining':'Transfer the series identity to the operational Cauchy completion in Agda.'}
(ROOT/'results/phase-pythagorean-series.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
