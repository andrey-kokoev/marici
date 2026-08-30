import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1024=json.loads((ROOT/"results"/"wp1024_minimal_landau_small_cp_no_go.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert wp1024["status"]=="PASS"

r=sp.symbols("r",real=True,positive=True)
P=(12878670000*r**8+16583280000*r**7+10789212400*r**6+
   4331604000*r**5+1454241747*r**4+398819200*r**3+
   90718200*r**2+10800000*r+1687500)
J2=sp.factor(400*r**6/(3*P))
dJ2=sp.factor(sp.diff(J2,r))
B=(4292890000*r**8+2763880000*r**7-721934000*r**5-
   484747249*r**4-199409600*r**3-60478800*r**2-
   9000000*r-1687500)
assert sp.factor(dJ2)==sp.factor(-800*r**5*B/P**2)
assert sp.polys.polytools.count_roots(B,0,sp.Rational(1,4))==0
assert B.subs(r,0)<0
endpoint=sp.factor(J2.subs(r,sp.Rational(1,4)))
assert endpoint==sp.Rational(400,369161163681)

Js=[abs(sp.Rational(str(row["J"]))) for row in ensemble["records"]]
assert len(Js)==1210
assert all(j*j>0 and j*j<endpoint for j in Js)

# Exact rational bisection on the strictly increasing perturbative branch.
brackets=[]
for j in Js:
    target=j*j
    lo,hi=sp.Integer(0),sp.Rational(1,4)
    for _ in range(40):
        mid=(lo+hi)/2
        if J2.subs(r,mid)<target:
            lo=mid
        else:
            hi=mid
    assert J2.subs(r,lo)<target<J2.subs(r,hi)
    brackets.append((lo,hi))
global_lo=min(lo for lo,_ in brackets)
global_hi=max(hi for _,hi in brackets)
width=max(hi-lo for lo,hi in brackets)
assert width==sp.Rational(1,2**42)

result={
 "schema":"marici.flavor.wp1025.v1","status":"PASS",
 "source_domain":"WP90 finite-threshold ray restricted to 0<r<=1/4",
 "faithful_readout":"normalized physical J^2 reconstructed from Gram spectral discriminants",
 "exact_response":str(J2),
 "endpoint_J_squared":str(endpoint),
 "monotonicity_certificate":"derivative has no zero on (0,1/4] and is positive there by exact Sturm count",
 "ensemble_sheets_tested":len(Js),"ensemble_sheets_with_unique_branch_inverse":len(brackets),
 "reconstructed_r_outer_bracket":{"lower":str(global_lo),"upper":str(global_hi),
                                  "lower_float":float(global_lo),"upper_float":float(global_hi)},
 "per_sheet_bracket_width":str(width),
 "contextual_partition":"each fitted J magnitude has one r on the chosen perturbative branch; CP sign remains the conjugate-vacuum branch",
 "classification":"cubic hierarchy amplifier and faithful inverse readout on a declared branch; neither selector nor source normalization",
 "smallest_exact_falsifier":"two freely chosen r values on the same admitted source ray give different J while preserving the source grammar",
 "instrument":"CKM/Jarlskog readout reconstructs r only conditional on the WP90 coefficient packet and branch",
 "claim_boundary":"does not identify r outside the chosen branch, derive r from the source, or validate the WP90 coefficients and mediator experimentally",
 "remaining_gate":"an independent source equation selecting r in the reconstructed interval before CKM readout",
}
out=ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1025 PASS: unique r brackets",float(global_lo),float(global_hi),"width",width)
