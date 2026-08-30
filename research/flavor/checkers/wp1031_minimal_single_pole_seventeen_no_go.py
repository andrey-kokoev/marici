import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp1025=json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
lo=sp.Rational(wp1025["reconstructed_r_outer_bracket"]["lower"])
hi=sp.Rational(wp1025["reconstructed_r_outer_bracket"]["upper"])

N=sp.symbols("N",integer=True,positive=True)
lam,g,f,rho,S=sp.symbols("lam g f rho S",positive=True)

# Canonical O(N) vector potential restricted to the radial coordinate rho.
Vrad=lam/4*(rho**2-f**2)**2
mrad2=sp.simplify(sp.diff(Vrad,rho,2).subs(rho,f))
assert mrad2==2*lam*f**2
assert sp.diff(mrad2,N)==0
rrad=sp.simplify(f/sp.sqrt(mrad2))
assert rrad==1/sp.sqrt(2*lam)

# One spectator pole receiving N equal condensate contributions.
Vport=g*S**2*N*f**2/2
mport2=sp.diff(Vport,S,2)
rport=sp.simplify(f/sp.sqrt(mport2))
assert mport2==N*g*f**2
assert rport==1/sp.sqrt(N*g)
response=sp.diff(rport,g)
assert response==-1/(2*sp.sqrt(N)*g**sp.Rational(3,2))
assert response!=0

r17=sp.simplify(rport.subs({N:17,g:1}))
assert lo<r17<hi
assert not (lo<rport.subs({N:17,g:2})<hi)

# Exact fitted range for g if N=17 is granted.  It is a continuous interval,
# so the data-compatible integer does not select the portal normalization.
g_lo=sp.factor(1/(17*hi**2))
g_hi=sp.factor(1/(17*lo**2))
assert g_lo<1<g_hi

result={
 "schema":"marici.flavor.wp1031.v1","status":"PASS",
 "question":"Does the minimal symmetry-derived single-pole scalar grammar produce m_pole^2=17 f^2 without a free normalization?",
 "radial_constructor":{"mass_squared":str(mrad2),"ratio":str(rrad),"multiplicity_response":"0"},
 "spectator_constructor":{"mass_squared":str(mport2),"ratio":str(rport),"coupling_response":str(response)},
 "N17_data_compatible_g_interval":{"lower":str(g_lo),"upper":str(g_hi)},
 "unit_coupling_candidate":"r=1/sqrt(17) lies inside the WP1025 interval",
 "hostile_coupling":"g=2 gives r=1/sqrt(34), outside the WP1025 interval",
 "classification":"O(N) radial symmetry does not transmit N into curvature; an N-fold spectator sum transmits N but retains the free portal coupling g",
 "smallest_exact_falsifier":"at fixed N=17, changing g from 1 to 2 preserves the source representation and moves r outside the fitted interval",
 "instrument":"pole mass and source vev can measure Ng, but no current instrument or Ward identity decomposes the product and fixes g=1",
 "claim_boundary":"closes the minimal renormalizable O(N) radial and equal-condensate spectator constructors, not protected supersymmetric, gauge, or topological mass identities",
 "disposition":"negative: the single-pole route relocates rather than removes continuous normalization"
}
(ROOT/"results"/"wp1031_minimal_single_pole_seventeen_no_go.json").write_text(
 json.dumps(result,indent=2)+"\n")
print("WP1031 PASS:",mrad2,mport2,float(g_lo),float(g_hi))
