"""Exact Clark matrix algebra plus Gaussian smooth-source regression."""
from pathlib import Path
import json
import sympy as s
import mpmath as mp
I=s.I
S=I*s.Matrix([[-1,1,1,1],[-1,1,-1,-1]])/2
D=s.diag(I,-I,I,-I)
H=s.simplify(S.conjugate().T*s.diag(1,-1)*S)
C=s.simplify(D.conjugate().T*H*D)
assert C==s.Matrix([[0,0,-1,1],[0,0,-1,1],[-1,-1,0,0],[1,1,0,0]])/2
assert H.rank()==2 and H.eigenvals()=={-1:1,1:1,0:2}
# Summing first-slot coefficients over the repeated source f0 or f1.
assert C[0,:]+C[1,:]==s.Matrix([[0,0,-1,1]])
assert C[2,:]+C[3,:]==s.zeros(1,4)
mp.mp.dps=40
z=mp.mpc('.4','.2'); w=mp.mpc('-.3','.1')
signs=(1,-1,1,-1); degrees=(0,0,1,1)
phi=lambda x:mp.exp(-x*x)
def G(j,a,x):
    g0=mp.sqrt(mp.pi)/2*mp.exp(-a*x+a*a/4)*mp.erfc(x-a/2)
    return g0 if j==0 else (mp.exp(-x*x)+a*g0)/2

def tail(k,z,x): return G(degrees[k],signs[k]*1j*z,x)
def quad(f): return mp.quad(f,[0,1,3,7,mp.inf])
N=mp.mpc(0); bulk=mp.mpc(0); reservoir=mp.mpc(0)
for a in range(4):
    for b in range(4):
        coefficient=mp.mpf(str(C[a,b])) if C[a,b].q==1 else mp.mpf(int(C[a,b].p))/int(C[a,b].q)
        if not coefficient: continue
        endpoint=mp.conj(tail(a,w,0))*tail(b,z,0)
        gram=quad(lambda x:mp.conj(tail(a,w,x))*tail(b,z,x))
        forcing=quad(lambda x:x**degrees[a]*phi(x)*tail(b,z,x)
                     +mp.conj(tail(a,w,x))*x**degrees[b]*phi(x))
        factor=1j*(signs[b]*z-signs[a]*mp.conj(w))
        assert abs(endpoint-factor*gram-forcing)<mp.mpf('1e-32')
        N+=coefficient*endpoint
        bulk+=coefficient*factor*gram
        reservoir+=coefficient*forcing
reduced=quad(lambda x:phi(x)*(tail(3,z,x)-tail(2,z,x))
             +mp.conj(tail(3,w,x)-tail(2,w,x))*phi(x))
assert abs(reservoir-reduced)<mp.mpf('1e-32')
assert abs(N-bulk-reduced)<mp.mpf('1e-32')
assert abs(reduced)>mp.mpf('.001')
# Analytic expectation on the real diagonal: the reciprocal tails conjugate.
r=mp.mpf('.4')
real_diagonal=quad(lambda x:2*mp.re(phi(x)*(tail(3,r,x)-tail(2,r,x))))
assert abs(real_diagonal)<mp.mpf('1e-32')
result={'schema':'marici.grothendieck.clark-polarized-forcing-sewing.v1','passed':True,
        'checks':{'exact_signature_matrix':True,'inertia_positive_negative_null':[1,1,2],
                  'first_moment_forcing_cancels':True,'all_nonzero_local_green_entries':True,
                  'sewn_identity':True,'reservoir_generically_nonzero':True,
                  'real_diagonal_reservoir_zero':True},
        'gaussian_reservoir':mp.nstr(reduced,25),
        'scope':'Exact fixed-sewing matrix algebra and analytic identity for admitted tails. Gaussian regression does not establish theta-kernel positivity.'}
p=Path(__file__).resolve().parents[1]/'results/clark-polarized-forcing-sewing.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
