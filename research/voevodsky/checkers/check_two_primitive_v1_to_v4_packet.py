#!/usr/bin/env python3
"""Minimal two-primitive V1 -> V4 positive/signed packet fixture."""
import json, math
from pathlib import Path


def z(r,c): return [[0.0]*c for _ in range(r)]
def eye(n):
    a=z(n,n)
    for i in range(n): a[i][i]=1.0
    return a
def tr(a): return [list(x) for x in zip(*a)]
def mm(a,b):
    bt=tr(b); return [[sum(x*y for x,y in zip(ar,bc)) for bc in bt] for ar in a]
def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b): return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sc(c,a): return [[c*x for x in r] for r in a]
def vs(*xs): return [r[:] for x in xs for r in x]
def block(a,b,c,d): return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def gram(x): return mm(tr(x),x)
def mx(a): return max(abs(x) for r in a for x in r)
def det2(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def abs_symmetric_2x2(a):
    # |A|=sqrt(A^2); closed formula for the positive square root of a 2x2 PSD matrix.
    a2=mm(a,a); rootdet=abs(det2(a))
    den=math.sqrt(a2[0][0]+a2[1][1]+2*rootdet)
    return sc(1/den,add(a2,[[rootdet,0.0],[0.0,rootdet]]))
def psd2(a,tol=1e-12):
    return a[0][0]>=-tol and a[1][1]>=-tol and det2(a)>=-tol

n=4; I=eye(n); Z=z(n,n)
P=z(n,n); P[0][0]=P[1][1]=1.0
Q0=[r[:] for r in P]; QT=z(n,n)
for a,b in ((0,2),(1,3)):
    QT[a][a]=9/25; QT[a][b]=QT[b][a]=12/25; QT[b][b]=16/25
DQ=sub(QT,Q0)
J2=block(I,Z,Z,sc(-1,I))
FT=vs(QT,sub(I,QT)); F0=vs(Q0,sub(I,Q0))
Psi=sc(1/math.sqrt(2),vs(FT,F0)); Z2=z(2*n,2*n)
J4=block(J2,Z2,Z2,sc(-1,J2))
Theta=sc(1/math.sqrt(2),vs(mm(Psi,P),Psi)); Z4=z(4*n,4*n)
K8=block(Z4,J4,J4,Z4)

# Two source primitives: e1 and e3. Their polarized readout has a nonzero cross term.
A=z(n,2); A[0][0]=1.0; A[2][1]=1.0
XA=mm(Theta,A)
G4=gram(XA)
D4=mm(mm(tr(XA),K8),XA)
expected=mm(mm(tr(A),sc(.5,add(mm(P,DQ),mm(DQ,P)))),A)

# A separate affine volume coordinate, retained positively rather than silently centered.
volume=6.0
Xvol=sc(math.sqrt(volume),A)
Gvol=gram(Xvol)
Gtotal=add(G4,Gvol)
AbsD=abs_symmetric_2x2(D4)
Dplus=sc(.5,add(AbsD,D4))
Dminus=sc(.5,sub(AbsD,D4))
Common=sub(Gtotal,AbsD)
GT=add(Common,Dplus)
G0=add(Common,Dminus)
# The negative polarity is rank one here; factor it as the odd endpoint column b.
b0=math.sqrt(Dminus[0][0])
b=[[b0],[Dminus[1][0]/b0]]
bbt=mm(b,tr(b))
# One lossless k-refinement, applied to each primitive coordinate.
c=3/5; s=4/5
R=[[c,0.0],[0.0,c],[s,0.0],[0.0,s]]

checks={
 "v4_positive_gram": psd2(Gtotal),
 "signed_readout_exact": mx(sub(D4,expected)) < 1e-12,
 "cross_polarization_visible": abs(D4[0][1]) > 1e-12,
 "source_volume_positive": psd2(Gvol),
 "absolute_signed_gram_positive": psd2(AbsD),
 "fixture_common_remainder_positive": psd2(Common),
 "common_plus_absolute_recovers_total": mx(sub(add(Common,AbsD),Gtotal)) < 1e-12,
 "positive_polarity_gram": psd2(Dplus),
 "negative_polarity_gram": psd2(Dminus),
 "odd_endpoint_factorization": mx(sub(bbt,Dminus)) < 1e-12,
 "two_seams_have_common_bulk": mx(sub(sub(GT,Dplus),sub(G0,Dminus))) < 1e-12,
 "polarity_difference_recovers_signed_face": mx(sub(sub(GT,G0),D4)) < 1e-12,
 "schur_margin_positive": psd2(sub(Common,bbt)),
 "k_analysis_isometry": mx(sub(gram(R),eye(2))) < 1e-12,
}
out={
 "schema":"marici.voevodsky.two-primitive-v1-v4-packet.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "source_primitives":["e1","e3"],
 "v1_gram":gram(A),
 "v4_positive_gram":Gtotal,
 "v4_signed_relative_readout":D4,
 "absolute_signed_gram":AbsD,
 "fixture_common_remainder":Common,
 "positive_polarity_gram":Dplus,
 "negative_polarity_gram":Dminus,
 "tate_seam_gram":GT,
 "reference_seam_gram":G0,
 "odd_endpoint_column":b,
 "schur_margin":sub(Common,bbt),
 "k_refinement_analysis":R,
 "checks":checks,
 "claim_boundary":"Exact finite projection fixture. It realizes the two polarity seams, their common-bulk square, rank-one endpoint Schur filler, and one isometric k-refinement. It does not prove their uniform physical or arithmetic realization."
}
path=Path(__file__).resolve().parents[1]/'results/two_primitive_v1_to_v4_packet.json'
path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(out['status']!='passed')
