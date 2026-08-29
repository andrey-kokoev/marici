import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp1028=json.loads((ROOT/"results"/"wp1028_integer_mass_norm_window.json").read_text())
assert wp1028["status"]=="PASS"

N=17
m=sp.symbols("m",positive=True)
H=m*sp.eye(N)
ones=sp.ones(N,1)
unit=ones/sp.sqrt(N)
Hinv=H.inv()

normalized_match=sp.factor((unit.T*Hinv*unit)[0])
unnormalized_match=sp.factor((ones.T*Hinv*ones)[0])
frobenius_mass=sp.sqrt(sp.trace(H.T*H))
aggregate_substitution=sp.factor(1/frobenius_mass)

assert normalized_match==1/m
assert unnormalized_match==sp.Rational(N,1)/m
assert frobenius_mass==sp.sqrt(N)*m
assert aggregate_substitution==1/(sp.sqrt(N)*m)
# Deliberate exact obstruction: the inverse operator response is neither the
# inverse Frobenius norm nor generated from it.
assert sp.simplify(
 normalized_match-aggregate_substitution-(17-sp.sqrt(17))/(17*m)
)==0
assert normalized_match!=aggregate_substitution
assert unnormalized_match!=aggregate_substitution

# Basis changes preserve the pole spectrum and normalized response, while the
# port vectors transform covariantly.
Q=sp.eye(N)
Q[0,0]=0;Q[0,1]=1;Q[1,0]=1;Q[1,1]=0
assert Q.T*Q==sp.eye(N)
assert sp.simplify(((Q.T*unit).T*(Q.T*H*Q).inv()*(Q.T*unit))[0])==1/m

result={
 "schema":"marici.flavor.wp1030.v1","status":"PASS",
 "question":"Does a rank-17 equal-mass mediator frame make the WP90 pole denominator equal to its aggregate Gram norm?",
 "admitted_domain":"seventeen degenerate orthogonal heavy mediators with mass block H=m I_17 and aligned source/readout ports",
 "normalized_exact_schur_response":str(normalized_match),
 "unnormalized_exact_schur_response":str(unnormalized_match),
 "frobenius_mass":str(frobenius_mass),
 "incorrect_aggregate_inverse":str(aggregate_substitution),
 "exact_obstruction":str(sp.factor(normalized_match-aggregate_substitution)),
 "classification":"Schur matching is controlled by the inverse pole operator, not the Frobenius mass norm; mediator multiplicity changes port contraction, not m to sqrt(17)m",
 "smallest_exact_falsifier":"for normalized equal ports the exact response is 1/m rather than 1/(sqrt(17)m)",
 "surviving_wp1028_domain":"one physical pole whose mass-squared receives seventeen independently normalized positive contributions",
 "instrument":"pole spectroscopy and residues must distinguish one composite pole from seventeen degenerate poles and calibrate the port vectors",
 "claim_boundary":"closes the rank-17 mediator-frame and tight-frame interpretations, not a single-pole additive mass-squared constructor",
 "disposition":"WP1028 narrowed: the rank/projector successor proposed by WP1029 is invalid for the WP90 Schur denominator"
}
(ROOT/"results"/"wp1030_schur_pole_vs_gram_norm.json").write_text(
 json.dumps(result,indent=2)+"\n")
print("WP1030 PASS:",normalized_match,aggregate_substitution)
