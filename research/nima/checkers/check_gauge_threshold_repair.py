"""Threshold diagnostics for common-trace three-coupling boundary.

Additive shifts D_i are in inverse couplings at MZ. Fixed illustrative
EM and strong inputs; weak angle is output. No target-fitting scan.
Writes no files.
"""
import math
A,S=127.95,8.5

def solve(dy=0.,d2=0.,d3=0.):
    ell=(3*(A-dy-d2)-8*(S-d3))/67
    t=((A-dy-d2)-(11/3)*ell)/16
    weak=(6*t-(19/6)*ell+d2)/A
    return ell,t,weak

ell,t,s0=solve()
# SM sterile right-handed neutrinos: Y=0, weak/color indices=0.
sterile_beta=(0.,0.,0.)
assert solve(*sterile_beta)==solve()
# Corrections along the common boundary vector are absorbed by its fitted t.
for c in [0.01,0.1,1.]:
    e,tt,s=solve(10*c,6*c,6*c)
    assert math.isclose(e,ell,abs_tol=1e-12)
    assert math.isclose(tt,t-c,abs_tol=1e-12)
    assert math.isclose(s,s0,abs_tol=1e-12)
# Degenerate complete SU5 multiplet threshold ratios in unrescaled Y convention.
for h in [0.1,1.,2.]:
    assert math.isclose(solve(5*h/3,h,h)[2],s0,abs_tol=1e-12)
# General linear response after refitting EM and strong inputs.
for dy,d2,d3 in [(1.,0.,0.),(0.,1.,0.),(0.,0.,1.),(.3,.7,.2)]:
    expected=(-23*dy/134+111*d2/134-109*d3/201)/A
    assert math.isclose(solve(dy,d2,d3)[2]-s0,expected,abs_tol=1e-14)
print(f'Baseline weak angle: {s0:.9f}')
print('Sterile singlet threshold: zero one-loop change.')
print('Common (10,6,6) boundary correction: absorbed by normalization, zero angle change.')
print('Degenerate complete SU5 multiplet threshold: zero angle change in this diagnostic.')
print('Response: delta sin^2 = [-23*DY/134 +111*D2/134 -109*D3/201]/127.95')
print('Exact singlet indices and numerical refit identities passed.')
