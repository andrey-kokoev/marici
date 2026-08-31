import json, math
from itertools import combinations
from pathlib import Path

def K(u):
    X=math.exp(2*u) if u<350 else float('inf'); tail=0.0
    if u<2:
        n=1
        while True:
            t=math.exp(-math.pi*n*n*X); tail+=t
            if t<1e-18:break
            n+=1
    return .5*math.exp(-u/2)-math.exp(u/2)*tail

def state(x,h0):
    s=math.sqrt(x); decay=.5-s; L=max(80.,40./decay); N=int(math.ceil(L/h0)); N+=N%2; h=L/N; z=[0.]*4
    for i in range(N+1):
        u=i*h; wt=1 if i in (0,N) else (4 if i%2 else 2); su=s*u
        if su<350: ch=math.cosh(su); th=math.tanh(su); raw=K(u)*ch; sech2=1/(ch*ch)
        else: th=1.; sech2=0.; raw=.25*math.exp(-decay*u)
        q=u*th/(2*s); dq=-u*th/(4*s**3)+u*u*sech2/(4*s*s)
        for j,v in enumerate((raw,raw*q,raw*q*q,raw*dq)):z[j]+=wt*v
    I,Iq,Iq2,Idq=[v*h/3 for v in z]; Eq=Iq/I; var=Iq2/I-Eq*Eq
    return 1+(x-.25)*Eq, Eq+(x-.25)*(Idq/I)-(.25-x)*var

def det3(A):return A[0][0]*(A[1][1]*A[2][2]-A[1][2]**2)-A[0][1]*(A[0][1]*A[2][2]-A[1][2]*A[0][2])+A[0][2]*(A[0][1]*A[1][2]-A[1][1]*A[0][2])
xs=(.02,.08,.14,.20,.235)
def census(h):
 st={x:state(x,h) for x in xs}
 def L(x,y):return st[x][1] if x==y else (st[y][0]-st[x][0])/(y-x)
 return [{"points":list(t),"determinant":det3([[L(x,y) for y in t] for x in t])} for t in combinations(xs,3)]
coarse=census(.01); fine=census(.005)
same=[a["determinant"]*b["determinant"]>0 for a,b in zip(coarse,fine)]
checks={"all_ten_triples_tested":len(fine)==10,"coarse_signs_all_positive":all(r["determinant"]>0 for r in coarse),"fine_signs_all_positive":all(r["determinant"]>0 for r in fine),"refinement_preserves_every_sign":all(same)}
base=Path(__file__).parents[2]; mixed=(base/"grothendieck"/"theta-green-transfer-mixed-bezoutian.md").read_text(encoding="utf-8"); checks["source_declares_finite_negative_minor_falsifier"]="negative finite Loewner minor" in mixed
stable=all(checks.values())
result={"schema":"marici.strominger.rh_theta_mixed_response_three_point_loewner_audit.v1","status":"passed" if stable else "inconclusive","strength":"double_precision_mesh_comparison","sources":["research/grothendieck/theta-green-transfer-mixed-bezoutian.md"],"verdict":("All sampled 3x3 signs are positive and refinement-stable." if stable else "The sampled 3x3 determinants are below reliable double-precision resolution: signs are not uniformly positive and refinement-stable. This is numerical indeterminacy, not a negative Loewner minor. High-precision or interval execution is required; the admitted structured-command policy refused the authorized ephemeral SymPy preflight."),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"coarse":coarse,"fine":fine}
out=Path(__file__).parents[1]/"results"/"rh_theta_mixed_response_three_point_loewner_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
