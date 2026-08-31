import json
from fractions import Fraction
from pathlib import Path

def outer(x,y): return [[x[i]*y[j] for j in range(len(y))] for i in range(len(x))]
def add(A,B,c=1): return [[A[i][j]+c*B[i][j] for j in range(len(A))] for i in range(len(A))]
def rank(A):
    M=[[Fraction(x) for x in row] for row in A]
    r=0
    for c in range(len(M[0])):
        p=next((i for i in range(r,len(M)) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        v=M[r][c]; M[r]=[x/v for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]:
                v=M[i][c]; M[i]=[M[i][j]-v*M[r][j] for j in range(len(M[0]))]
        r+=1
    return r

# Basis (P(z),P(-z),Q(z),Q(-z)), Q=a times the first moment transform.
ea=[1,1,-1,1]   # E_a = X + i a X'
em=[1,1,1,-1]   # E_-a = X - i a X'
S=[1,1,0,0]      # X
R=[0,0,-1,1]     # i a X'
M=add(outer(ea,ea),outer(em,em),-1)
expected=add(outer(S,R),outer(R,S))
expected=[[2*x for x in row] for row in expected]
checks={
  "bilateral_expansion_exact":M==expected,
  "mixed_current_rank_two":rank(M)==2,
  "mixed_current_trace_zero":sum(M[i][i] for i in range(4))==0,
  "mixed_current_not_positive_semidefinite":sum(M[i][j]*ea[i]*ea[j] for i in range(4) for j in range(4))>0 and sum(M[i][j]*em[i]*em[j] for i in range(4) for j in range(4))<0,
}
result={
 "schema":"marici.strominger.rh_bilateral_mixed_sewing_kernel_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "source":"research/nima/theta-prime-scale-recursive-clark-repair.md",
 "identity":"E_a E_a^* - E_-a E_-a^* = 2[(i a X')X^* + X(i a X')^*], with the conjugation signs giving the de Branges Wronskian current",
 "verdict":"Completed bilateral sewing cancels the one-sided sheet-odd norm line, but the right-left cross terms assemble into a rank-two trace-zero mixed current. Algebraic sewing makes this current exact; it does not make it positive. A sign claim is equivalent to orienting the X,X' Bezoutian and cannot be inferred from sampled shear alone.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"matrix":M
}
out=Path(__file__).parents[1]/"results"/"rh_bilateral_mixed_sewing_kernel_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
