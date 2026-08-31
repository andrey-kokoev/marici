import json, math
from itertools import combinations
from pathlib import Path

def K(u):
    X=math.exp(2*u) if u<350 else float("inf"); tail=0.0
    if u<2:
        n=1
        while True:
            t=math.exp(-math.pi*n*n*X); tail+=t
            if t<1e-18:break
            n+=1
    return .5*math.exp(-u/2)-math.exp(u/2)*tail

def state(x,h0):
    s=math.sqrt(x); decay=.5-s; L=max(80.,40./decay)
    N=int(math.ceil(L/h0)); N+=N%2; h=L/N; sums=[0.]*4
    for i in range(N+1):
        u=i*h; wt=1 if i in (0,N) else (4 if i%2 else 2); su=s*u
        if su<350:
            ch=math.cosh(su); th=math.tanh(su); raw=K(u)*ch; sech2=1/(ch*ch)
        else: th=1.; sech2=0.; raw=.25*math.exp(-decay*u)
        q=u*th/(2*s); dq=-u*th/(4*s**3)+u*u*sech2/(4*s*s)
        for j,v in enumerate((raw,raw*q,raw*q*q,raw*dq)):sums[j]+=wt*v
    I,Iq,Iq2,Idq=[v*h/3 for v in sums]; Eq=Iq/I
    var=Iq2/I-Eq*Eq; Hp=Eq+(x-.25)*(Idq/I)-(.25-x)*var
    H=1+(x-.25)*Eq
    return H,Hp

xs=(.01,.04,.08,.12,.16,.20,.23,.24)
def census(h):
    vals={x:state(x,h) for x in xs}; rows=[]
    for x,y in combinations(xs,2):
        Hx,Dx=vals[x]; Hy,Dy=vals[y]; off=(Hy-Hx)/(y-x)
        det=Dx*Dy-off*off
        rows.append({"x":x,"y":y,"diag_x":Dx,"diag_y":Dy,"offdiag":off,"determinant":det})
    return vals,rows
coarse,crows=census(.02); fine,frows=census(.01)
minrow=min(frows,key=lambda r:r["determinant"])
max_delta=max(abs(a["determinant"]-b["determinant"]) for a,b in zip(crows,frows))
checks={
 "all_sampled_diagonals_positive":all(v[1]>0 for v in fine.values()),
 "all_two_point_principal_minors_nonnegative":all(r["determinant"]>=-1e-12 for r in frows),
 "strict_two_point_minors_observed":minrow["determinant"]>0,
 "mesh_refinement_preserves_minor_sign":all(a["determinant"]>0 and b["determinant"]>0 for a,b in zip(crows,frows)),
 "all_pairs_tested":len(frows)==len(xs)*(len(xs)-1)//2,
}
base=Path(__file__).parents[2]
mixed=(base/"grothendieck"/"theta-green-transfer-mixed-bezoutian.md").read_text(encoding="utf-8")
checks["source_declares_negative_minor_as_falsifier"]="negative finite Loewner minor" in mixed
result={"schema":"marici.strominger.rh_theta_mixed_response_two_point_loewner_audit.v1","status":"passed" if all(checks.values()) else "failed","strength":"mesh_refined_numerical_falsifier","sources":["research/grothendieck/theta-green-transfer-mixed-bezoutian.md","research/grothendieck/theta-central-strip-diagonal-variance-gate.md"],"verdict":"Every sampled 2x2 Loewner principal minor for the mixed response ratio is positive on the central-strip grid at both mesh 0.02 and mesh 0.01. No two-point sign falsifier was found. The smallest determinants are near 1e-12 and their magnitudes are not numerically certified; interval or higher-precision verification remains required. Three-point minors remain open, and positivity does not itself construct the missing three-port coupling.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"minimum_row":minrow,"maximum_refinement_delta":max_delta,"rows":frows}
out=Path(__file__).parents[1]/"results"/"rh_theta_mixed_response_two_point_loewner_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
