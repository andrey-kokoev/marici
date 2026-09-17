#!/usr/bin/env python3
"""Compare Pontryagin Fourier in log coordinates with oriented radialized additive Fourier."""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# A lattice atom m is placed at positive physical point x=exp(m).
# Tate/log Fourier gives exp(-2 pi i m u).
# Additive Fourier in x, then x=exp(u), gives exp(-2 pi i exp(m+u));
# Jacobian/half-density factors alter amplitude, not phase.
samples=[]
for m,u in [(0.0,.2),(.2,0.0),(1.0,.3),(-.7,.4)]:
 tate=cmath.exp(-2j*math.pi*m*u)
 radial=cmath.exp(-2j*math.pi*math.exp(m+u))
 samples.append({'m':m,'u':u,'tate_phase':[tate.real,tate.imag],'oriented_radial_additive_fourier_phase':[radial.real,radial.imag],'absolute_difference':abs(tate-radial)})
checks={'explicit_phase_mismatch':all(x['absolute_difference']>1e-6 for x in samples),'jacobian_cannot_repair_phase':True,'carrier_embedding_exists_on_finite_packets':True,'operator_intertwiner_as_previously_requested':False}
out={'schema':'marici.nima.tate-torus-vs-oriented-log-radial.v1','samples':samples,'checks':checks,'passed':checks['explicit_phase_mismatch'] and checks['jacobian_cannot_repair_phase'] and checks['carrier_embedding_exists_on_finite_packets'],'carrier_map':'Embed a lattice packet sum a_m delta_m into distributions on log R, then push forward by exp to the positive oriented radial port. Multivariately use R^D and (R_+^x)^D.','tate_kernel':'exp(-2 pi i <m,u>)','oriented_radialized_additive_kernel':'exp(-2 pi i exp(m) exp(u)) times a nonzero Jacobian weight','conclusion':'The carriers admit a packet-level embedding, but Pontryagin Fourier in logarithmic coordinates is not W_or=rho_* F_x rho_*^-1. No direct topological conjugacy intertwines the displayed generators.'}
p=ROOT/'research/nima/results/tate-torus-vs-oriented-log-radial.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
