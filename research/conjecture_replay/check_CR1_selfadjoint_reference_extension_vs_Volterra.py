#!/usr/bin/env python3
"""Finite interval no-go: selfadjoint first-derivative extension is not pure Volterra."""
import cmath,json
# -i d/dt extensions have boundary u(b)=omega*u(a), |omega|=1.
# Any inhomogeneous solution is Volterra_part + c*homogeneous; with endpoint
# monodromy r and Volterra terminal value F, c=F/(omega-r).
def correction(F,r,omega): return F/(omega-r)
samples=[]
for z,omega,F in [(0.4+0.7j,1+0j,2-1j),(-0.3+0.5j,1j,1+2j),(0.2-0.6j,-1+0j,3+1j)]:
 r=cmath.exp(1j*z);c=correction(F,r,omega)
 ub=F+r*c;ua=c
 samples.append({'z':str(z),'omega':str(omega),'F':str(F),'correction_abs':abs(c),'boundary_residual_abs':abs(ub-omega*ua)})
 assert abs(ub-omega*ua)<1e-12 and abs(c)>1e-8
# Pure Volterra has ua=0 and ub=F, so a unitary boundary condition forces F=0.
assert all(abs(complex(x['F']))>0 for x in samples)
out={'schema':'marici.conjecture-replay.CR1-selfadjoint-reference-vs-Volterra.v1','passed':True,'outcome':'--','identity':'u=V_z f+c h_z; selfadjoint boundary u(b)=omega u(a), |omega|=1, forces c=F_z(f)/(omega-exp(i z L))','conclusion':'For generic forcing F_z(f)!=0, c!=0. No selfadjoint endpoint extension has the pure causal Volterra resolvent on all sources.','samples':samples,'admissible_retypes':['use a maximal dissipative causal extension and its selfadjoint dilation','retain both causal and anti-causal histories so the doubled boundary correction closes','treat Volterra as a gamma/Poisson block, not as the resolvent of the selfadjoint reference extension']};print(json.dumps(out,indent=2))
