#!/usr/bin/env python3
"""Reproducible Simpson pilot for raw Gaussian window energies at p=2,3."""
import json, math
from pathlib import Path
from evidence_policy import write_result
R=Path(__file__).resolve().parents[2]
def W(t,q): return -.5*(math.erf(math.sqrt(math.pi)*(q+t))-math.erf(math.sqrt(math.pi)*(q-t)))
def simpson(f,b=8.0,n=400000):
    h=b/n;s=f(0.0)+f(b)
    s+=4*sum(f(i*h) for i in range(1,n,2));s+=2*sum(f(i*h) for i in range(2,n,2))
    return 2*h*s/3
def energies(p):
    L=math.log(p)
    a=simpson(lambda q: W(L,q)**2*math.exp(-math.pi*q*q))
    d=simpson(lambda q: (W(2*L,q)-W(L,q))**2*math.exp(-math.pi*q*q))
    cross=simpson(lambda q: W(L,q)*(W(2*L,q)-W(L,q))*math.exp(-math.pi*q*q))
    return {'L':L,'a_p':a,'g_win_p':d,'wall_window_cross_raw':cross}
vals={str(p):energies(p) for p in (2,3)}
out={'schema':'marici.conjecture-replay.CR1-window-energy-p2-p3.v1','passed':True,'claim_status':'supported','evidence':[{'class':'NUMERICAL','claim':'A 400000-panel symmetric Simpson calculation on [-8,8] of the exact error-function windows gives reproducible pilot values for p=2,3.','checker':'research/conjecture_replay/check_CR1_window_energy_p2_p3.py'},{'class':'SOURCE_DERIVED','claim':'The raw window energy is the Gaussian integral of |W_2L-W_L|^2, equivalently a correlated-normal annular rectangle probability.','source':'research/nima/the-prime-two-gaussian-integrals-are-one-correlated-normal-rectangle-problem.md'}],'outcome':'numerical p=2,3 raw window table; not interval-certified','definition':'W_t(q)=-1/2[erf(sqrt(pi)(q+t))-erf(sqrt(pi)(q-t))]','measure':'exp(-pi q^2)dq','quadrature':'symmetric Simpson, 400000 panels on [0,8] doubled','values':vals,'interpretation':'g_win,p is the odd diagonal of K_p^*G_win,pK_p when G_win,p is this raw Gaussian window form.','cross_warning':'The raw wall-window cross integral is nonzero but belongs to an unsaturated scalar/window realization; it is not C_wt of the Fourier-saturated joint Green form.','certification':'Digits are numerical evidence only. A proof should use outward-rounded correlated-normal rectangle bounds.','next':'interval_certify_via_correlated_normal_rectangles_if_proof_level_values_are_needed'}
write_result(R/'research/conjecture_replay/results/CR1_window_energy_p2_p3.json',out);print(json.dumps(vals))
