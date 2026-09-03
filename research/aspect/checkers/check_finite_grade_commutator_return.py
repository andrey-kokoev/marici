"""Exact finite grade-derivation audit on the primitive-square Pauli plane."""
from pathlib import Path
import json

I=[[1+0j,0j],[0j,1+0j]]
N=[[1+0j,0j],[0j,2+0j]]
X=[[0j,1+0j],[1+0j,0j]]
Y=[[0j,1j],[-1j,0j]]
Pplus=[[1+0j,0j],[0j,0j]]
Pminus=[[0j,0j],[0j,1+0j]]
R=X

def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(2)),0j) for j in range(2)] for i in range(2)]
def sub(a,b): return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
def scale(c,a): return [[c*a[i][j] for j in range(2)] for i in range(2)]
def eq(a,b): return all(a[i][j]==b[i][j] for i in range(2) for j in range(2))
def encode(a): return [[str(a[i][j]) for j in range(2)] for i in range(2)]

adX=sub(mm(N,X),mm(X,N))
adY=sub(mm(N,Y),mm(Y,N))
reverse=mm(mm(Pminus,R),Pplus)
checks={
 "grade_commutator_maps_X_to_iY":eq(adX,scale(1j,Y)),
 "grade_commutator_maps_Y_to_minus_iX":eq(adY,scale(-1j,X)),
 "pauli_frame_is_exact":eq(mm(X,X),I) and eq(mm(Y,Y),I),
 "same_finite_plane_allows_reverse_return":not eq(reverse,[[0j,0j],[0j,0j]]),
 "return_fails_grade_commutation":not eq(sub(mm(N,R),mm(R,N)),[[0j,0j],[0j,0j]]),
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"exact Gaussian integers","checks":checks,"ad_N_X":encode(adX),"ad_N_Y":encode(adY),"reverse_block":encode(reverse),"conclusion":"the source grade operator canonically rotates the finite Pauli ports, but reverse-triangularity requires an additional law that the Green return preserve the grade filtration"}
out=Path("research/aspect/results/finite_grade_commutator_return.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
