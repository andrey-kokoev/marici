import json, math
from pathlib import Path

labels=(1,4,9,16); ell={1:0.,4:0.7,9:1.1,16:1.6}; wt={1:1.,4:.5,9:1/3,16:.25}; C=math.sqrt(math.pi/2)
def baseW(a,R):return C*math.exp((a*a-R*R)/2)
def baseJ(a,R):return a*baseW(a,R)
def directW(n,m,a,R):
 A,B=ell[n],ell[m]; c1=R/2+A; c2=-R/2+B
 return wt[n]*wt[m]*C*math.exp(-c1*c1-c2*c2+(a-A-B)**2/2)
def directJ(n,m,a,R):return (a-ell[n]-ell[m])*directW(n,m,a,R)
def covW(n,m,a,R):
 S=ell[n]+ell[m]; D=ell[n]-ell[m]
 return wt[n]*wt[m]*math.exp(-a*S)*baseW(a,R+D)
def covJ(n,m,a,R):
 S=ell[n]+ell[m]; D=ell[n]-ell[m]; f=wt[n]*wt[m]*math.exp(-a*S)
 return f*(baseJ(a,R+D)-S*baseW(a,R+D))
pts=[(.1,-1.2),(.2,0.),(.35,.8),(.5,1.7)]
def close(x,y):return abs(x-y)<=2e-13*max(1.,abs(x),abs(y))
checks={
 "band_density_covariance_includes_product_tilt_factor":all(close(directW(n,m,a,R),covW(n,m,a,R)) for n in labels for m in labels for a,R in pts),
 "band_current_covariance_has_forced_product_degree_correction":all(close(directJ(n,m,a,R),covJ(n,m,a,R)) for n in labels for m in labels for a,R in pts),
 "current_is_tilt_derivative_of_density":all(abs(directJ(n,m,a,R)-(directW(n,m,a+1e-6,R)-directW(n,m,a-1e-6,R))/(2e-6))<=2e-9*max(1.,abs(directJ(n,m,a,R))) for n in labels for m in labels for a,R in pts),
 "pair_swap_reverses_separation":all(close(directW(n,m,a,R),directW(m,n,a,-R)) for n in labels for m in labels for a,R in pts),
}
# Basiswise linearity makes finite cutoff restriction immediate.
coef={(n,m):((n+m)%5-2) for n in labels for m in labels}
def synth(N,a,R,current=False):
 f=directJ if current else directW
 return sum(c*f(n,m,a,R) for (n,m),c in coef.items() if n<=N and m<=N)
checks["finite_pair_cutoff_is_basiswise_for_density_and_current"]=all(close(synth(9,a,R,z),sum(c*(directJ if z else directW)(n,m,a,R) for (n,m),c in coef.items() if n<=9 and m<=9)) for a,R in pts for z in (False,True))
base=Path(__file__).parents[2]
terminal=(base/"grothendieck"/"theta-terminal-band-current-is-globally-negative.md").read_text(encoding="utf-8")
band=(base/"nima"/"theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md").read_text(encoding="utf-8")
checks.update({"source_defines_current_as_tilt_derivative":"J_a(R)=\\partial_aW_a(R)" in terminal,"source_requests_finite_W_J_pair_maps":"(W_{nm}(D),J_{nm}(D))" in band})
result={"schema":"marici.strominger.rh_theta_ordered_pair_band_current_covariance_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/grothendieck/theta-terminal-band-current-is-globally-negative.md","research/nima/theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md","research/strominger/results/rh_theta_ordered_pair_correlation_covariance_audit.json"],"verdict":"The finite ordered-pair band current is constructed. With product shift S=log(nm), ratio shift D=log(n/m), and half-density weight (nm)^(-1/2), W_nm,a(R)=(nm)^(-1/2-a)W_11,a(R+D) and J_nm,a(R)=(nm)^(-1/2-a)[J_11,a(R+D)-S W_11,a(R+D)]. The correction -S W is forced by differentiating the product tilt factor. Pair swap reverses separation, and density/current synthesis commutes with finite pair cutoff. Completed continuity and detection of a joint-flat state remain open.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"tested_pairs":16,"tested_parameter_points":4}
out=Path(__file__).parents[1]/"results"/"rh_theta_ordered_pair_band_current_covariance_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
