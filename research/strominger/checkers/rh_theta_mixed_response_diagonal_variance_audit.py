import json, math
from pathlib import Path

# Dependency-free composite-Simpson falsifier. The cutoff is chosen so the
# slowest asymptotic exponential tail is below exp(-40).
def K(u):
    X=math.exp(2*u) if u<350 else float("inf")
    tail=0.0
    if u<2:
        n=1
        while True:
            t=math.exp(-math.pi*n*n*X)
            tail+=t
            if t<1e-18:break
            n+=1
    return 0.5*math.exp(-u/2)-math.exp(u/2)*tail

def data(x):
    s=math.sqrt(x); decay=0.5-s
    L=max(80.0,40.0/decay); h=0.02
    N=int(math.ceil(L/h)); N+=N%2; h=L/N
    sums=[0.0]*4
    for i in range(N+1):
        u=i*h; wt=1 if i in (0,N) else (4 if i%2 else 2)
        su=s*u
        # Stable asymptotic evaluation of cosh and the tilted density.
        if su<350:
            ch=math.cosh(su); th=math.tanh(su); sech2=1/(ch*ch)
            raw=K(u)*ch
        else:
            th=1.0; sech2=0.0; raw=0.25*math.exp(-decay*u)
        q=u*th/(2*s)
        dq=-u*th/(4*s**3)+u*u*sech2/(4*s*s)
        vals=(raw,raw*q,raw*q*q,raw*dq)
        for j,v in enumerate(vals):sums[j]+=wt*v
    I,Iq,Iq2,Idq=[v*h/3 for v in sums]
    Eq=Iq/I; variance=Iq2/I-Eq*Eq; Edq=Idq/I
    response=Eq+(x-0.25)*Edq
    hp=response-(0.25-x)*variance
    return I,response,variance,hp,L,N

xs=[0.005,0.02,0.05,0.10,0.15,0.20,0.23,0.24]
rows=[]
for x in xs:
    I,response,variance,hp,L,N=data(x)
    rows.append({"x":x,"I":I,"response":response,"variance":variance,"H_prime":hp,"cutoff":L,"panels":N})
checks={
 "precursor_integrals_positive":all(r["I"]>0 for r in rows),
 "variance_nonnegative":all(r["variance"]>=0 for r in rows),
 "diagonal_variance_bound_passes_grid":all(r["H_prime"]>0 for r in rows),
 "grid_reaches_both_center_and_threshold_sides":xs[0]<0.01 and xs[-1]>0.23,
 "tail_cutoff_controls_slowest_decay":all((0.5-math.sqrt(r["x"]))*r["cutoff"]>=39.999 for r in rows),
}
base=Path(__file__).parents[2]
gate=(base/"grothendieck"/"theta-central-strip-diagonal-variance-gate.md").read_text(encoding="utf-8")
mixed=(base/"grothendieck"/"theta-green-transfer-mixed-bezoutian.md").read_text(encoding="utf-8")
checks.update({"source_identifies_variance_inequality":"operatorname{Var}_x(q_x)" in gate,"source_identifies_ratio_monotonicity_target":"matrix monotone **decrease**" in mixed})
result={"schema":"marici.strominger.rh_theta_mixed_response_diagonal_variance_audit.v1","status":"passed" if all(checks.values()) else "failed","strength":"numerical_falsifier_grid","sources":["research/grothendieck/theta-central-strip-diagonal-variance-gate.md","research/grothendieck/theta-green-transfer-mixed-bezoutian.md"],"verdict":"On the tested central-strip grid, the tilted-law formula has H'(x)>0, equivalently -R'(x)>0. No diagonal falsifier was found from x=0.005 through x=0.24. This supports but does not prove the variance bound; interval certification and higher Loewner minors remain open. The result cannot by itself orient the Krein coupling or establish matrix monotonicity.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"rows":rows}
out=Path(__file__).parents[1]/"results"/"rh_theta_mixed_response_diagonal_variance_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
